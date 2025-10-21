import pandas as pd
from tkinter import filedialog, Tk

# Oculta la ventana principal de Tkinter
Tk().withdraw()

print("Selecciona el archivo con la lista de asesores (el archivo pequeño)...")
asesores_path = filedialog.askopenfilename()

print("Selecciona el archivo base de datos (el archivo grande)...")
base_path = filedialog.askopenfilename()

# Carga ambos archivos
asesores_df = pd.read_excel(asesores_path, header=None)
base_df = pd.read_excel(base_path)

# Muestra las columnas disponibles en el archivo base
print("🔍 Columnas detectadas en el archivo base:")
print(base_df.columns.tolist())

# Detecta automáticamente la columna que contiene "asesor"
asesor_col = [col for col in base_df.columns if 'asesor' in col.lower()]
if not asesor_col:
    print("❌ No se encontró ninguna columna que contenga 'asesor'. Revisa los encabezados.")
    exit()
asesor_col_name = asesor_col[0]

# Normaliza nombres en la base
base_df[asesor_col_name] = (
    base_df[asesor_col_name]
    .astype(str)
    .str.upper()
    .str.replace(r'\s+', ' ', regex=True)
    .str.strip()
)

# Extrae nombres de asesores desde el archivo pequeño (cada 2 filas: nombre, fecha)
asesores_nombres = asesores_df.iloc[::2, 0].tolist()
asesores_nombres = [str(nombre).upper().replace('\n', ' ').replace('\r', '').strip() for nombre in asesores_nombres]

# Detecta columnas de evaluación
columnas_evaluacion = [col for col in base_df.columns if col.upper() in ['IRENE SERVICIO', 'IRENE ASESOR']]
if not columnas_evaluacion:
    print("❌ No se encontraron columnas 'IRENE SERVICIO' o 'IRENE ASESOR'.")
    exit()

# Inicializa resultados
resultados = []

for asesor in asesores_nombres:
    # Filtra filas donde el nombre del asesor aparece parcialmente
    filas_asesor = base_df[base_df[asesor_col_name].str.contains(asesor, case=False, na=False)]

    if filas_asesor.empty:
        print(f"⚠️ Asesor no encontrado en base: {asesor}")
        continue

    # Cuenta PROMOTOR y DETRACTOR con expresiones robustas
    promotores = filas_asesor[columnas_evaluacion].apply(
        lambda col: col.astype(str).str.upper().str.contains(r'\bPROMOTOR\b', regex=True).sum(), axis=0
    ).sum()

    detractores = filas_asesor[columnas_evaluacion].apply(
        lambda col: col.astype(str).str.upper().str.contains(r'\bDETRACTOR\b', regex=True).sum(), axis=0
    ).sum()

    resultados.append({
        'Asesor': asesor,
        'Promotores': promotores,
        'Detractores': detractores
    })

# Crea DataFrame con resultados
resultados_df = pd.DataFrame(resultados)

# Exporta a Excel
output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", title="Guardar resultados como...")
resultados_df.to_excel(output_path, index=False)

print("✅ Archivo generado con éxito:", output_path)
