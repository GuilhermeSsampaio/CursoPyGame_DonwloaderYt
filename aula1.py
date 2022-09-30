import  pygame
from pygame.locals import *
from sys import exit


pygame.init() #inicia as funções da biblioteca pygame
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')

#todo jogos se passa dentro de um loop principal

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50)) #passa a tela como parametro, a cor, a posição no plano cartesiano e as medidas do retângulo, nessa ordem respectivamente
    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40) ##indica a tela, a cor, a posição e o raio do circulo
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    pygame.display.update() #essa linha atualiza o jogo, a tela no caso