import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar microfono para devolver el audio como texto
def transform_audio_to_text():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo recording
        print("ya puedes hablar")

        # guardar lo grabado
        audio = r.listen(origen)

        try:
            # buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language ="es-ar")

            # prueba de que se pudo reconocer lo que dije
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio

        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("Ups, no entendi")
            print("error code: 002xfa")

            # devolver error
            return "sigo esperando"

        # en caso de no poder resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("Ups, no se pudo resolver la tarea realizada o no entendi")
            print("error code: 007adx")

            # devolver error
            return "sigo esperando"

        #error inesperado
        except:
            print("ups, algo a salido mal, desesas mandar un informe?")

            return "code error 00xx2"

 # transform_audio_to_text()

#funcion para que asistente pueda ser escuchado
def speak(message):

    # encender motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', idEnglish)

    # dira el mensaje
    engine.say(message)
    # corre nuevamente y escucha el proximo mensaje
    engine.runAndWait()

# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)


# estos son los ids de los idioma de voz instalados en la computadora
idSpanish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
idEnglish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

speak('hi, my name is galiAsisstant. i am programming for more thinks')