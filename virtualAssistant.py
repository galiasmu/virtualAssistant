import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from pynput import keyboard as kb
import os
import subprocess
import ctypes
import sys
import winreg


# Estos son los ids de los idioma de voz instalados en la computadora
idSpanish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
idEnglish = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


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
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que se pudo reconocer lo que dije
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido
            #return transform_audio_to_text()

        # en caso de que no comprenda el audio

        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            speak('úps, no entendi, podrias volver a repetir la frase')
            print("error code: 002xfa")

            # volver a llamar a la función
            return transform_audio_to_text()


        # en caso de no poder resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"
            return transform_audio_to_text()

            # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"
            return transform_audio_to_text()


# transform_audio_to_text()

# funcion para que asistente pueda ser escuchado
def speak(message):
    # encender motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', idSpanish)

    # dira el mensaje
    engine.say(message)
    # corre nuevamente y escucha el proximo mensaje
    engine.runAndWait()


# consultar dias de la semana
def consultar_day():
    # crear variable con datos de hoy

    dia = datetime.date.today()
    print(dia)

    # crear variable para aislar dia de semana
    day_week = dia.weekday()
    print(day_week)

    # diccionario que contiene nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sabado',
                  6: 'Domingo'}
    # el lenguaje interpreta lo anterior
    speak(f'Hoy es {calendario[day_week]}')


# informar que hora es
def consultar_hora():
    # hacemos lo mismo que con fecha
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos, GALI'
    print(hora)

    # decir la hora correctamente
    speak(hora)


def hello_world():
    # crear variable con datos de hora

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas Tardes'

    speak(
        f'{momento} Gali, soy tu asistente personal. Dime, en que te puedo ayudar?')



def get_applications():
    application_dirs = ["C:\\Program Files (x86)", "C:\\Program Files", "C:\\"]
    applications = []
    for app_dir in application_dirs:
        for root, dirs, files in os.walk(app_dir):
            for file in files:
                if file.endswith('.exe'):
                    filepath = os.path.join(root, file)
                    applications.append(filepath)
    return applications

specific_apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "steam": "C:\\Program Files (x86)\\Steam\\steam.exe",
    "epic games": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\EpicGamesLauncher.exe"
}


def open_app(app_name):
    if app_name.lower() in specific_apps: # busca en variable global de apps especificas
        os.startfile(specific_apps[app_name.lower()]) # si esta ahi, que la abra
        return True
    else:
        for app in get_applications(): #sino lo buscara de la funcion obetener aplicaciones
            if app_name.lower() in app.lower():
                os.startfile(app)
                return True
    return False







def init():
    # activar saludo inicial
    hello_world()

    # variable de corte
    inicio = True

    # loop central
    while inicio:

        # activar el micro y guardar el pedido en un string
        pedido = transform_audio_to_text().lower()  # lower(convierte en minuscula el texto extraido)


        if 'abrir youtube' in pedido:
            speak('Con gusto, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir navegador' in pedido:
            speak('Como no, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abrir' in pedido:
                app_name = pedido.split("abrir")[-1].strip()
                speak(f"La aplicación {app_name} se esta abriendo.")
                if open_app(app_name):
                    print("se esta abriendo la aplicacion")
                else:
                    speak(f"No se pudo encontrar la aplicación {app_name}.")

                continue
        elif 'qué sabes hacer' in pedido:
            pedido = speak("puedo realizar muchahs tareas para la cual fui programada.")
            speak("Puedo decirte la fecha y hora del día de hoy, "
                  "puedo abrir aplicaciones, "
                  "reproducirte musica en youtube (no, no me paga Google para esto), "
                  "puedo realizar busquedas en wikipedia o en el navegador, "
                  "tambien puedo decirte un par de chistes,"
                  " y Con el tiempo tendre muchas mas funcionalidades")
            continue
        elif 'qué día es hoy' in pedido:
            consultar_day()
            continue
        elif 'qué hora es' in pedido:
            speak(consultar_hora())
            continue
        elif 'busca en wikipedia' in pedido:
            speak(f'Buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '') # para que no busque con la frase "buscar en wikipedia" sino que la omite
            wikipedia.set_lang('es') # define el idioma para buscar en wikipedia
            rta = wikipedia.summary(pedido, sentences=2) # obtiene un resumen de lo buscado de 2 parrafos.
            speak('Wikipedia dice lo siguiente:')
            speak(rta)
            continue
        elif 'busca en internet ' in pedido:
            speak('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            speak('Esto es lo que encontre')
            continue
        elif 'reproducir' in pedido:
            speak('ya te pongo un cumbion')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            speak(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'Apple': 'APPL',
                       'Amazon': 'AMZN',
                       'Google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                speak(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                speak("Perdón pero no la he encontrado")
                continue
        elif '' in pedido:
            pedido = speak("No entendi, podes volver a hablar por favor?")
            continue
        elif 'Chau' or 'ya no te necesito' in pedido:
            speak('Me voy a descansar, cualquier cosa me avisas')
        break



#get_applications()
#open_app("steam")
init()


# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)


# speak('hi, my name is galiAsisstant. i am programming for more thinks')

# consultar_day()
# hello_world()
# consultar_hora()
