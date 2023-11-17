import tkinter as tk
from PIL import Image, ImageTk
import pygame
import subprocess


def tocar_indie():
    pygame.init()
    pygame.mixer.music.load('play_indie.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

def tocar_rock():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('')
    pygame.music.play()
    pygame.event.wait()

def tocar_rap():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('McPoze.mp3')
    pygame.music.play()
    pygame.event.wait()

def tocar_pop():
    pass

def iniciar_jogo():
    def start_snake_game():
        subprocess.call(["python", "snake.py"])

    if __name__ == "__main__":
        start_snake_game()

# Criar a janela principal
janela = tk.Tk()
janela.title("SNAKEFY GAME")
janela.geometry("800x600")
janela.configure(bg="black")

# Carregar uma label
logo = Image.open("logo_snakefy.png")
logo_tk = ImageTk.PhotoImage(logo)

# Carregar a imagem para o botão
rk = Image.open("button_rock.png")
rkie = ImageTk.PhotoImage(rk)

ind = Image.open("button_indie.png")
indi = ImageTk.PhotoImage(ind)

rap = Image.open("button_rap.png")
rp = ImageTk.PhotoImage(rap)

pop = Image.open("button_pop.png")
pp = ImageTk.PhotoImage(pop)

jogar = Image.open("button_jogar.png")
jg = ImageTk.PhotoImage(jogar)

# Criar os botões com espaçamento
espaco = 10

logotipo = tk.Label(janela, bg="black", image=logo_tk)
logotipo.pack(pady=espaco)

button_rock = tk.Button(janela, image=rkie, bg="black", borderwidth=0, command=tocar_rock)
button_rock.pack(pady=espaco)

button_indie = tk.Button(janela, image=indi, bg="black", borderwidth=0, command=tocar_indie)
button_indie.pack(pady=espaco)

button_rap = tk.Button(janela, image=rp, bg="black", borderwidth=0, command=tocar_rap)
button_rap.pack(pady=espaco)

button_pop = tk.Button(janela, image=pp, bg="black", borderwidth=0, command=tocar_pop)
button_pop.pack(pady=espaco)

button_jogar = tk.Button(janela, image=jg, bg="black", borderwidth=0, command=iniciar_jogo)
button_jogar.pack(pady=espaco)

# Iniciar o loop da interface gráfica
janela.mainloop()
