import tkinter as tk
import subprocess
from PIL import Image, ImageTk

def tocar_indie():


    pass

def tocar_rock():


    pass

def tocar_rap():



    pass

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

# Carregue uma label

logo = Image.open("logo_snakefy.png")
logo_tk = ImageTk.PhotoImage(logo)

# Carregue a imagem para o botão
rk = Image.open("button_rock.png")  # Substitua "nome_da_imagem.jpg" pelo nome da sua imagem
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
espaco = 10  # Define o espaçamento entre os botões

logotipo = tk.Label(janela, bg="black", image=logo_tk)
button_rock = tk.Button(janela, image=rkie, bg="black", borderwidth=0, command=tocar_rock)
button_indie = tk.Button(janela, image=indi, bg="black", borderwidth=0, command=tocar_indie)
button_rap = tk.Button(janela, image=rp, bg="black", borderwidth=0, command=tocar_rap)
button_pop = tk.Button(janela, image=pp, bg="black", borderwidth=0, command=tocar_pop)
button_jogar = tk.Button(janela, image=jg, bg="black", borderwidth=0, command=iniciar_jogo)

logotipo.pack(pady=espaco)
button_rock.pack(pady=espaco)
button_indie.pack(pady=espaco)
button_rap.pack(pady=espaco)
button_pop.pack(pady=espaco)
button_jogar.pack(pady=espaco)




# Iniciar o loop da interface gráfica
janela.mainloop()
