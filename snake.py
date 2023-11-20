import pygame
import random

pygame.init()

pygame.display.set_caption("Pysnake")

largura, altura = 1200, 800

background = pygame.image.load("background.png")

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

tamanho_quadrado = 20
velocidade_jogo = 15

comida_x, comida_y = 0, 0

comida_imagem = pygame.image.load("food.png")
snake_head = pygame.transform.scale(pygame.image.load("cobra.png"), (tamanho_quadrado, tamanho_quadrado))
snake_body = pygame.transform.scale(pygame.image.load("corpo.png"), (tamanho_quadrado, tamanho_quadrado))

def gerar_comida():
    global comida_x, comida_y
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

def desenhar_comida(comida_x, comida_y):
    tela.blit(comida_imagem, (comida_x, comida_y))

def desenhar_cobra(pixels):
    tela.blit(snake_head, (pixels[0][0], pixels[0][1]))

    for pixel in pixels[1:]:
        tela.blit(snake_body, (pixel[0], pixel[1]))

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Maçãs: {pontuacao}", True, vermelha)
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
    global comida_x, comida_y, velocidade_jogo

    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    macas = 0
    pixels = []

    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        x += velocidade_x
        y += velocidade_y

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            gerar_comida()
            macas += 1

        pixels.insert(0, [x, y])

        while len(pixels) > tamanho_cobra:
            del pixels[-1]

        for pixel in pixels[1:]:
            if pixel == [x, y]:
                fim_jogo = True

        tela.blit(background, (0, 0))
        desenhar_comida(comida_x, comida_y)
        desenhar_cobra(pixels)
        desenhar_pontuacao(macas)

        pygame.display.update()
        relogio.tick(velocidade_jogo)

    pygame.quit()

gerar_comida()
rodar_jogo()
