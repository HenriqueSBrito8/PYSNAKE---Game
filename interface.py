import tkinter as tk

def tocar_pagode():
    # Coloque aqui o código para tocar música de pagode
    pass

def tocar_funk():
    # Coloque aqui o código para tocar música de funk
    pass

def tocar_rock():
    # Coloque aqui o código para tocar música de rock
    pass

def tocar_sertanejo():
    # Coloque aqui o código para tocar música sertaneja
    pass

def tocar_pop():
    # Coloque aqui o código para tocar música pop
    pass

def iniciar_jogo():
    import pygame

    import random

    pygame.init()

    pygame.display.set_caption("Pysnake")

    largura, altura = 1200, 800

    tela = pygame.display.set_mode((largura, altura))

    relogio = pygame.time.Clock()

    preta = (0, 0, 0)

    branca = (255, 255, 255)

    vermelha = (255, 0, 0)

    verde = (0, 255, 0)

    tamanho_quadrado = 20

    velocidade_jogo = 15

    def gerar_comida():

        comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
            tamanho_quadrado)

        comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(
            tamanho_quadrado)

        return comida_x, comida_y

    def desenhar_comida(tamanho, comida_x, comida_y):

        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

    def desenhar_cobra(tamanho, pixels):

        for pixel in pixels:
            pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

    def desenhar_pontuacao(pontuacao):

        fonte = pygame.font.SysFont("Helvetica", 35)

        texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)

        tela.blit(texto, [1, 1])

    def selecionar_velocidade(tecla):

        if tecla == pygame.K_DOWN:

            velocidade_x = 0

            velocidade_y = tamanho_quadrado

        elif tecla == pygame.K_UP:

            velocidade_x = 0

            velocidade_y = -tamanho_quadrado

        elif tecla == pygame.K_RIGHT:

            velocidade_x = tamanho_quadrado

            velocidade_y = 0

        elif tecla == pygame.K_LEFT:

            velocidade_x = -tamanho_quadrado

            velocidade_y = 0

        return velocidade_x, velocidade_y

    def rodar_jogo():

        fim_jogo = False

        x = largura / 2

        y = altura / 2

        velocidade_x = 0

        velocidade_y = 0

        tamanho_cobra = 1

        pixels = []

        comida_x, comida_y = gerar_comida()

        while not fim_jogo:

            tela.fill(preta)

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:

                    fim_jogo = True

                elif evento.type == pygame.KEYDOWN:

                    velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

            desenhar_comida(tamanho_quadrado, comida_x, comida_y)

            # atualizar a posicao da cobra

            if x < 0 or x >= largura or y < 0 or y >= altura:
                fim_jogo = True

            x += velocidade_x

            y += velocidade_y

            pixels.append([x, y])

            if len(pixels) > tamanho_cobra:
                del pixels[0]

            for pixel in pixels[:-1]:

                if pixel == [x, y]:
                    fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels)

            desenhar_pontuacao(tamanho_cobra - 1)

            pygame.display.update()

            if x == comida_x and y == comida_y:
                tamanho_cobra += 1

                comida_x, comida_y = gerar_comida()

            relogio.tick(velocidade_jogo)

    rodar_jogo()
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
