import speech_recognition as sr
import tkinter as tk
from PIL import Image, ImageTk

def capturar_nome():
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as source:
        print("Diga seu nome:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        nome = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Nome capturado: {nome}")
        return nome
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro na requisição ao Google: {e}")
        return None

class CapturaNomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captura de Nome")
        self.root.geometry("600x150")
        self.root.configure(bg="black")

        self.label = tk.Label(root, font=("Arial", 18), fg="white", bg="black",
                              text="Pressione o botão e diga seu nome para iniciar o jogo.")
        self.label.pack()

        # Carrega e exibe a imagem do ícone do microfone
        image_microfone = Image.open("icone_microfone.png")
        image_microfone = ImageTk.PhotoImage(image_microfone)

        # Cria um botão com a imagem do ícone do microfone
        self.button = tk.Button(root, image=image_microfone, bg="black", borderwidth=0,command=self.capturar_nome, bd=0)
        self.button.image = image_microfone
        self.button.pack()

        # Atributo para armazenar o nome capturado
        self.nome_capturado = None

    def capturar_nome(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Diga seu nome:")
            audio = recognizer.listen(source)

        try:
            nome = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Nome capturado: {nome}")
            self.nome_capturado = nome

            # Fechar a janela após capturar o nome
            self.root.destroy()
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
        except sr.RequestError as e:
            print(f"Erro na requisição ao Google: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CapturaNomeApp(root)
    root.mainloop()
