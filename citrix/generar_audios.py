import os
from gtts import gTTS

def generate_better_audio():
    """Genera audios con configuración mejorada de gTTS"""
    
    if not os.path.exists('mp3'):
        os.makedirs('mp3')
    
    # Textos optimizados para mejor pronunciación
    audio_texts = {
        #'welcome': 'Simulador Citrix. Aprende a utilizar la plataforma Citrix de forma interactiva y práctica. Domina todas las funciones con nuestro curso paso a paso.',
        #'feature_contenido': 'Contenido Completo',
        #'feature_simulaciones': 'Simulaciones Interactivas', 
        #'feature_certificacion': 'Certificación',
        #'boton_curso': 'Comenzar Curso',
        #'confirmacion': 'Iniciando curso Citrix'
        #******************************************************************#
        #'page1_bienvenida': 'Plataforma de Acceso Seguro. Citrix es una plataforma que proporciona a los asesores del Contact Center, un Acceso Seguro y Unificado a aplicaciones, escritorios, y datos desde su PC en su posición de trabajo. Herramientas Centralizadas. Los asesores accederán a las herramientas necesarias, para realizar sus tareas desde su lugar de trabajo, garantizando seguridad, eficiencia y productividad en todas sus operaciones.',
        #'boton_siguiente': 'Siguiente',
        #'boton_atras': 'Atras'
        #******************************************************************#
        #'page2_bienvenida' : 'Acceso a la Plataforma. Para acceder a la plataforma Citrix, ingresa a la siguiente liga oficial:'
        #******************************************************************#
        'page3_bienvenida' : 'Acceso BBVA. Una vez dentro de la aplicacion, ingresaremos nuestros datos correspondientes, para acceder al contenido. Sigue las instrucciones que te muestra la imagen.'
        #******************************************************************#
        #******************************************************************#
        #******************************************************************#
        #******************************************************************#
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