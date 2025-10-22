import os
from gtts import gTTS

def generate_better_audio():
    """Genera audios con configuración mejorada de gTTS"""
    
    if not os.path.exists('mp3'):
        os.makedirs('mp3')
    
    # Textos optimizados para mejor pronunciación
    audio_texts = {
        'welcome': 'Simulador Citrix. Aprende a utilizar la plataforma Citrix de forma interactiva y práctica. Domina todas las funciones con nuestro curso paso a paso.',
        'feature_contenido': 'Contenido Completo',
        'feature_simulaciones': 'Simulaciones Interactivas', 
        'feature_certificacion': 'Certificación',
        'boton_curso': 'Comenzar Curso',
        'confirmacion': 'Iniciando curso Citrix'
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