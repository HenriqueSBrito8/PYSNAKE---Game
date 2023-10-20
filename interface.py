import tkinter as tk
import subprocess
import radio
def tocar_pagode():



    pass

def tocar_funk():


    pass

def tocar_rock():


    pass

def tocar_sertanejo():



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
janela.title("Music Snake")
janela.geometry("800x600")
janela.configure(bg="black")

# Criar os botões com espaçamento
espaco = 10  # Define o espaçamento entre os botões

botao_pagode = tk.Button(janela, text="Tocar Pagode", fg="white", bg="black", command=tocar_pagode)
botao_funk = tk.Button(janela, text="Tocar Funk", fg="white", bg="black", command=tocar_funk)
botao_rock = tk.Button(janela, text="Tocar Rock", fg="white", bg="black", command=tocar_rock)
botao_sertanejo = tk.Button(janela, text="Tocar Sertanejo", fg="white", bg="black", command=tocar_sertanejo)
botao_pop = tk.Button(janela, text="Tocar Pop", fg="white", bg="black", command=tocar_pop)
botao_iniciar = tk.Button(janela, text="Iniciar Jogo", fg="white", bg="black", command=iniciar_jogo)

# Posicionar os botões com espaçamento usando o método pack()
botao_pagode.pack(pady=espaco)
botao_funk.pack(pady=espaco)
botao_rock.pack(pady=espaco)
botao_sertanejo.pack(pady=espaco)
botao_pop.pack(pady=espaco)
botao_iniciar.pack(pady=espaco)

# Iniciar o loop da interface gráfica
janela.mainloop()
