import pygame

# Criando a classe do nosso player.
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Importando o sprite do player.
        self.image = pygame.image.load("img/player.png").convert_alpha()
        # Posicionando o sprite na tela com base na posição de quando a classe for iniciada.
        self.rect = self.image.get_rect(midbottom = pos)
        