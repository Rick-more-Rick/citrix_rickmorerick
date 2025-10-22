import os
from gtts import gTTS
import hashlib

def text_to_audio(text, filename, lang='es'):
    """Convierte texto a archivo de audio usando gTTS"""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)
        print(f"✅ Audio generado: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error generando {filename}: {e}")
        return False

def generate_audio_files():
    """Genera todos los archivos de audio necesarios"""
    
    # Crear carpeta mp3 si no existe
    if not os.path.exists('mp3'):
        os.makedirs('mp3')
    
    # Textos para convertir a audio
    audio_texts = {
        # Audio de bienvenida
        'welcome': 'Simulador Citrix. Aprende a utilizar la plataforma Citrix de forma interactiva y práctica. Domina todas las funciones con nuestro curso paso a paso.',
        
        # Audios de features (solo títulos)
        'feature_contenido': 'Contenido Completo',
        'feature_simulaciones': 'Simulaciones Interactivas', 
        'feature_certificacion': 'Certificación',
        
        # Audio del botón
        'boton_curso': 'Comenzar Curso',
        
        # Audio de confirmación
        'confirmacion': 'Iniciando curso'
    }
    
    # Generar archivos de audio
    generated_files = []
    
    for key, text in audio_texts.items():
        # Crear nombre de archivo único basado en el texto
        filename = f"mp3/{key}.mp3"
        if text_to_audio(text, filename):
            generated_files.append(filename)
    
    print(f"\n🎯 Archivos generados: {len(generated_files)}")
    for file in generated_files:
        print(f"   📁 {file}")
    
    return generated_files

if __name__ == "__main__":
    print("🎵 Generando archivos de audio...")
    generate_audio_files()
    print("🎉 Proceso completado!")