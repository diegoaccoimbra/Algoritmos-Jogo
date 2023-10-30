from typing import Any
import pygame
from sprites import *
from config import *

# Criando a classe do nosso player.
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Importando o sprite do player.
        self.image = pygame.image.load("img/player.png").convert_alpha()
        # Posicionando o sprite na tela com base na posição passada como parâmetro quando a classe for iniciada.
        self.rect = self.image.get_rect(midbottom = pos)
        # Velocidade com que o sprite vai se mover.
        self.speed = 5
        
    # Método que pega as entradas do usuário, no caso aqui as teclas pressionadas.    
    def get_input(self):
        keys = pygame.key.get_pressed()

        # Teste se a tecla direita está pressionada e se o valor da posição direita do sprite é menor que a largura da tela (Para limitar o movimento dele dentro da tela). Se sim, ele pega a posição do sprite do player e o move pelo eixo X.
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x = self.rect.x + self.speed

        # Teste se a tecla esquerda está pressionada e se o valor da posição esquerda do sprite é maior que 0 (o valor mínimo da largura da tela).
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x = self.rect.x - self.speed
    
    # Método que atualiza o sprite com bases nas teclas pressionadas.
    def update(self):
        self.get_input()
