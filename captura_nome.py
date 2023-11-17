import tkinter as tk
import speech_recognition as sr
from interface import InterfaceJogoSnake

def capturar_nome():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Fale seu nome...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            nome = recognizer.recognize_google(audio)
            nome_var.set(nome)
            print("Nome reconhecido:", nome)

            # Após o reconhecimento do nome, abra a interface do jogo Snake
            abrir_interface_jogo_snake()
        except sr.UnknownValueError:
            print("Não foi possível reconhecer a fala.")
        except sr.RequestError as e:
            print("Erro na solicitação:", str(e))

def abrir_interface_jogo_snake():
    nome = nome_var.get()

    # Crie uma janela secundária para o jogo Snake
    janela_jogo_snake = tk.Toplevel()
    janela_jogo_snake.title("Jogo Snake")

    # Crie uma instância da classe InterfaceJogoSnake
    interface_snake = InterfaceJogoSnake(janela_jogo_snake, nome)

# Criar a janela principal para capturar o nome
janela_captura_nome = tk.Tk()
janela_captura_nome.title("Captura de Nome")

nome_var = tk.StringVar()

label_nome = tk.Label(janela_captura_nome, text="Fale seu nome:")
entry_nome = tk.Entry(janela_captura_nome, textvariable=nome_var)
botao_capturar = tk.Button(janela_captura_nome, text="Capturar Nome", command=capturar_nome)

label_nome.pack()
entry_nome.pack()
botao_capturar.pack()

janela_captura_nome.mainloop()
