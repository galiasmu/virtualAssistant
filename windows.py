import tkinter as tk
from virtualAssistant import init
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi asistente de voz")

        # Crea el botón y lo agrega a la ventana
        boton = tk.Button(self, text="Iniciar asistente", command=self.iniciar_asistente)
        boton.pack()

    def iniciar_asistente(self, por_voz=False):
        if por_voz:
            # Iniciar asistente por voz
            threading.Thread(target=init).start()
        else:
            # Iniciar asistente por botón
            init()


if __name__ == "__main__":
    app = App()
    app.geometry("400x200") # Cambiar tamaño de ventana
    app.mainloop()
