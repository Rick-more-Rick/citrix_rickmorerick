import os
from gtts import gTTS

def generate_better_audio():
    """Genera audios con configuración mejorada de gTTS"""
    
    if not os.path.exists('mp3'):
        os.makedirs('mp3')
    
    # Textos optimizados para mejor pronunciación
    audio_texts = {
        #'welcome_Simulador': 'Simulador Citrix.' ,
        #'feature_contenido': 'Contenido Completo',
        #'feature_simulaciones': 'Simulaciones Interactivas', 
        #'feature_certificacion': 'Certificación',
        #'boton_curso': 'Comenzar Curso',
        #'confirmacion': 'Iniciando curso Citrix'
        #******************************************************************#
        #'page1_bienvenida': '¿Que es citrix?. Es una plataforma que proporciona a los asesores del Contact Center, un Acceso Seguro y Unificado a aplicaciones, escritorios, y datos desde su PC en su posición de trabajo. Los asesores accederán a las herramientas necesarias, para realizar sus tareas desde su lugar de trabajo.',
        #'boton_siguiente': 'Siguiente',
        #'boton_atras': 'Atras'
        #******************************************************************#
        #'page2_bienvenida' : 'Ingresa a la siguiente liga oficial:'
        #******************************************************************#
        #'page3_bienvenida' : 'Acceso BBVA. Una vez dentro de la aplicacion, ingresaremos nuestros datos correspondientes, para acceder al contenido. Sigue las instrucciones que te muestra la imagen.'
        #******************************************************************#
        #'page4_bienvenida' : 'Dashboard principal:. Click en aplicaciones, para visualizar todas las ligas de acceso que tienes permitidas.'
        #******************************************************************#
        #'page5_bienvenida' : 'Aplicaciones:. Para acceder, unicamente deberas dar doble clic al aplicativo que se requiera.'
        #******************************************************************#
        #'page6_bienvenida' : 'Al ingresar a cada aplicación, mostrara un círculo de carga, después mostrará un mensaje de alerta el cual indica que ha encontrado los recursos necesarios, y comenzará con la apertura del aplicativo. Clic en el icono de engranaje'
        #******************************************************************#
        #'page6_bienvenida' : 'Cierre de Sesión',
        #'page6_para' : 'Para cerrar sesión correctamente:. Haz clic en el engrane y selecciona Cerrar Sesión.',
        'page6_recuerda' : 'Recuerda siempre, al término de tu jornada o descansos espaciosos, debes cerrar correctamente el aplicativo. Clic en *cerrar sesión*.'
        #******************************************************************#
        #******************************************************************#
    }
    
    print("🎵 Generando audios con voz mejorada...")
    
    for key, text in audio_texts.items():
        filename = f"mp3/{key}.mp3"
        
        try:
            # Configuración optimizada
            tts = gTTS(
                text=text, 
                lang='es', 
                slow=False,  # False = más natural y rápido
                lang_check=True  # Mejor detección del idioma
            )
            tts.save(filename)
            print(f"✅ {filename}")
            
        except Exception as e:
            print(f"❌ Error en {key}: {e}")
    
    print("🎉 Audios generados!")

if __name__ == "__main__":
    generate_better_audio()