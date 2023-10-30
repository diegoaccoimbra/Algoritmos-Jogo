import pygame
import sys
from sprites import *
from config import *

# Classe que contém toda a lógica do jogo.
class Game:
    # Método construtor que inicia a classe. Adicionamos os grupos de sprites aqui.
    def __init__(self):
        # Criando uma instância da classe Player e adicionando no seu grupo de sprite.
        player_sprite = Player((screen_width / 2, screen_height))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    # Método que desenha e atualiza todos os grupos de sprites.
    def run(self):
        # Desenhando o sprite do jogador na tela e o atualizando.
        self.player.draw(screen)
        self.player.update()



# Iniciando o pygame.
if __name__ == "__main__":
    pygame.init()
    # Definindo o tamanho da janela do jogo.
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Definindo o "frame rate" (quantas vezes o jogo atualiza por segundo).
    clock = pygame.time.Clock()
    # Instância da classe Game
    game = Game()

    # Loop do jogo que é encerrado quando é fechado.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Desenhando o fundo com uma cor.
        screen.fill((30, 30, 30))
        
        # Desenhando e atualizando os sprites
        game.run()

        # Desenhando tudo que tiver sido desenhado no loop.
        pygame.display.flip()
        clock.tick(60)
