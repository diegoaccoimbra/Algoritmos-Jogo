"""
A construção desse jogo tem como referência o vídeo abaixo:
Creating Space Invaders in Pygame/Python. Disponível em: <https://www.youtube.com/watch?v=o-6pADy5Mdg>. 
"""
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

        # Criando um grupo de sprite pras instâncias da classe Enemy.
        self.enemy = pygame.sprite.Group()
        # Chamando a função pra posicionar os inimigos
        self.enemy_position(rows_number, cols_number)

    # Método que posiciona os inimigos em determinada posição.
    def enemy_position(self, rows, cols, x_distance = 60, y_distance = 48, window_distance = 20):
        for row_index in range(rows):
            for col_index in range(cols):
                # Incremento dos index com a distância necessária pra separar os sprites
                x = col_index * x_distance + window_distance
                y = row_index * y_distance + window_distance

                # Testes que criam uma instância da classe Enemy com variação de cores de acordo com a linha e coluna.
                if row_index % 2 == 0:
                    if col_index % 2 == 0:
                        enemy_sprite = Enemy((x, y), "red")
                    elif col_index % 3 == 0:
                        enemy_sprite = Enemy((x, y), "green")
                    else:
                        enemy_sprite = Enemy((x, y), "yellow")

                else:
                    if col_index % 2 == 0:
                        enemy_sprite = Enemy((x, y), "yellow")
                    elif col_index % 3 == 0:
                        enemy_sprite = Enemy((x, y), "red")
                    else:
                        enemy_sprite = Enemy((x, y), "green")

                
                # Adicionando ao grupo de sprites.
                self.enemy.add(enemy_sprite)

    # Método que desenha e atualiza todos os grupos de sprites.
    def run(self):
        # Desenhando o sprite do jogador na tela.
        self.player.draw(screen)
        # Desenhando o sprite dos lasers.
        self.player.sprite.laser.draw(screen)
        # Desenhando os sprites dos inimigos.        
        self.enemy.draw(screen)
        # Atualizando os sprites.
        self.player.update()
        self.enemy.update()


# Iniciando o pygame.
if __name__ == "__main__":
    pygame.init()
    # Definindo o tamanho da janela do jogo.
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Definindo o "frame rate" (quantas vezes o jogo atualiza por segundo).
    clock = pygame.time.Clock()
    # Instância da classe Game
    game = Game()
    # Imagem de fundo do jogo.
    background = pygame.image.load(background_image).convert_alpha()

    # Loop do jogo que é encerrado quando é fechado.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Desenhando o fundo com uma cor e adicionando a imagem de fundo.
        screen.fill((30, 30, 30))
        screen.blit(background, (0, 0))
        
        # Desenhando e atualizando os sprites
        game.run()

        # Desenhando tudo que tiver sido desenhado no loop.
        pygame.display.flip()
        clock.tick(60)
