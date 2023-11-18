import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from pygame import mixer
class InterfacePrincipalApp:
    def __init__(self, root, nome):
        self.root = root
        self.root.title("Snakefy Game")
        self.root.geometry("1280x920")
        self.root.configure(bg="black")
        mixer.init()

        # Carregar imagem do logo
        logo_image = self.load_image("logo_snakefy.png")

        # Adicionar a imagem acima do texto de boas-vindas
        self.logo_label = tk.Label(root, image=logo_image, bg="black")
        self.logo_label.image = logo_image
        self.logo_label.pack(pady=20)

        self.label = tk.Label(root, text=f"Bem-vindo, {nome}!", font=("Arial", 24), fg="white", bg="black")
        self.label.pack(pady=20)

        # Carregar imagens
        image_indie = self.load_image("button_indie.png")
        image_pop = self.load_image("button_pop.png")
        image_rock = self.load_image("button_rock.png")
        image_rap = self.load_image("button_rap.png")
        image_jogar = self.load_image("button_jogar.png")

        # Botões para tocar música e iniciar o jogo com imagens
        self.button_indie = tk.Button(root, image=image_indie, bg="black", borderwidth=0,command=self.tocar_indie, bd=0)
        self.button_indie.image = image_indie  # Para evitar que a imagem seja coletada pelo garbage collector
        self.button_indie.pack(pady=10)

        self.button_pop = tk.Button(root, image=image_pop, bg="black", borderwidth=0,command=self.tocar_pop, bd=0)
        self.button_pop.image = image_pop
        self.button_pop.pack(pady=10)

        self.button_rock = tk.Button(root, image=image_rock, bg="black", borderwidth=0,command=self.tocar_rock, bd=0)
        self.button_rock.image = image_rock
        self.button_rock.pack(pady=10)

        self.button_rap = tk.Button(root, image=image_rap, bg="black", borderwidth=0, command=self.tocar_rap, bd=0)
        self.button_rap.image = image_rap
        self.button_rap.pack(pady=10)

        self.button_iniciar_jogo = tk.Button(root, image=image_jogar, bg="black", borderwidth=0, command=self.iniciar_jogo, bd=0)
        self.button_iniciar_jogo.image = image_jogar
        self.button_iniciar_jogo.pack(pady=20)

    def load_image(self, path):
        img = Image.open(path)

        return ImageTk.PhotoImage(img)

    def tocar_indie(self):
        mixer.music.load("play_indie.mp3")  # Substitua pelo caminho real do seu arquivo MP3
        mixer.music.play()

    def tocar_pop(self):
        mixer.music.load("play_pop.mp3")  # Substitua pelo caminho real do seu arquivo MP3
        mixer.music.play()

    def tocar_rock(self):
        mixer.music.load("play_rock.mp3")  # Substitua pelo caminho real do seu arquivo MP3
        mixer.music.play()

    def tocar_rap(self):
        mixer.music.load("play_rap.mp3")  # Substitua pelo caminho real do seu arquivo MP3
        mixer.music.play()

    def iniciar_jogo(self):
        subprocess.call(["python", "snake.py"])

if __name__ == "__main__":
    # Substitua 'NomePadrao' pela variável que contém o nome capturado
    nome_padrao = "NomePadrao"

    root = tk.Tk()
    app = InterfacePrincipalApp(root, nome_padrao)
    root.mainloop()
