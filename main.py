"""
A construção desse jogo tem como referência o vídeo abaixo:
Creating Space Invaders in Pygame/Python. Disponível em: <https://www.youtube.com/watch?v=o-6pADy5Mdg>. 
"""
import pygame
import sys
from sprites import *
from config import *
from random import choice

# Classe que contém toda a lógica do jogo.
class Game:
    # Método construtor que inicia a classe. Adicionamos os grupos de sprites aqui.
    def __init__(self):
        # Criando uma instância da classe Player e adicionando no seu grupo de sprite.
        player_sprite = Player(player_position)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Sistema de vidas do player.
        self.lives = player_lives
        self.lives_img = pygame.image.load(player_lives_image).convert_alpha()
        self.lives_position = screen_width - (self.lives_img.get_size()[0] * 2 + 15)

        # Criando um grupo de sprite pras instâncias da classe Enemy.
        self.enemy = pygame.sprite.Group()
        # Chamando a função pra posicionar os inimigos
        self.enemy_position(rows_number, cols_number)
        # Velocidade de movimento dos inimigos.
        self.enemy_speed =  enemy_speed
        # Grupo de sprites do laser dos inimigos.
        self.enemy_laser = pygame.sprite.Group()

        # Fonte que vai ser usada na tela de fim de jogo.
        self.font = pygame.font.Font(game_font, 50)
        # Atributo pra verificar se o jogo foi encerrado.
        self.playing = True

    # Método que posiciona os inimigos em determinada posição.
    def enemy_position(self, rows, cols, x_distance = 60, y_distance = 50, window_distance = 40):
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

    # Método para movimentar os inimigos na tela.
    def enemies_movement(self):
        # Verifica se qualquer um dos inimigos atingiu o limite da tela, pra assim movimentar todos.
        all_enemies = self.enemy.sprites()
        for enemy in all_enemies:
            if enemy.rect.right >= screen_width:
                self.enemy_speed = -1

            elif enemy.rect.left <= 0:
                self.enemy_speed = 1

    # Método para os inimigos atirar o laser.
    def enemies_shoot(self):
        # Só ocorre se houver inimigos no grupo de sprites.
        if self.enemy.sprites():
            # Selecionando um inimigo aleatório de todos os inimigos pra atirar.
            random_enemy = choice(self.enemy.sprites())
            # Instância da classe Laser pro inimigo.
            laser_sprite = Laser(random_enemy.rect.center)
            laser_sprite.image.fill(enemy_laser_color)   
            laser_sprite.speed = - laser_speed
            self.enemy_laser.add(laser_sprite)      

    # Método para verificar se um alvo recebeu o tiro.
    def shoot_check(self):
        # Lasers do player.
        # Checa se cada laser do grupo de sprites dos lasers atingiu algum inimigo, fazendo o sprite do inimigo e do laser sumirem.
        if self.player.sprite.laser:
            for laser in self.player.sprite.laser:
                if pygame.sprite.spritecollide(laser, self.enemy, True):
                    laser.kill()

        # Lasers dos inimigos
        if self.enemy_laser:
            # Checa se o laser de algum inimigo atingiu o player e diminui o número de vidas.
            for laser in self.enemy_laser:
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives = self.lives - 1

    # Método pra mostrar as vidas restantes na tela.
    def display_lives(self):
        for live in range(self.lives - 1):
            position = (self.lives_position + (live * (self.lives_img.get_size()[0] + 10)), 5)
            screen.blit(self.lives_img, position)

    # Método pra exibir a mensagem ao fim do jogo.
    def game_over(self):
        # Mensagem em caso de vitória.
        if not self.enemy.sprites():
            message = self.font.render("VOCÊ VENCEU!", False, "green")
            message_rect = message.get_rect(center = game_over_message_position)
            screen.blit(background, (0, 0))
            screen.blit(message, message_rect)
            # Encerrando o jogo.
            self.playing = False
            
        # Mensagem em caso de derrota.
        elif self.lives == 0:
            message = self.font.render("VOCÊ PERDEU!", False, "red")
            message_rect = message.get_rect(center = game_over_message_position)
            screen.blit(background, (0, 0))
            screen.blit(message, message_rect)
            # Encerrando o jogo.
            self.playing = False

    # Método que verifica se o jogo ainda está em andamento.
    def is_playing(self):
        pygame.display.flip()
        if self.playing == False:
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
            

    # Método que desenha e atualiza todos os grupos de sprites.
    def run(self):
        # Desenhando o sprite do jogador na tela.
        self.player.draw(screen)
        # Desenhando o sprite dos lasers.
        self.player.sprite.laser.draw(screen)
        self.enemy_laser.draw(screen)
        # Desenhando os sprites dos inimigos.        
        self.enemy.draw(screen)
        # Método que checa se o laser atingiu.
        self.shoot_check()
        # Método que mostra as vidas na tela.
        self.display_lives()
        # Método que mostra a tela de fim de jogo.
        self.game_over()
        # Verifica se o jogo ainda está em andamento.
        self.is_playing()
        # Atualizando os sprites.
        self.player.update()
        self.enemy.update(self.enemy_speed)
        self.enemies_movement()
        self.enemy_laser.update()
        

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

    # Timer dos tiros dos lasers dos inimigos.
    enemylaser = pygame.USEREVENT + 1
    pygame.time.set_timer(enemylaser, 700)

    # Loop do jogo que é encerrado quando é fechado.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == enemylaser:
                game.enemies_shoot()
        
        # Desenhando o fundo com uma cor e adicionando a imagem de fundo.
        screen.fill((15, 15, 15))
        screen.blit(background, (0, 0))
        
        # Desenhando e atualizando os sprites
        game.run()

        # Desenhando tudo que tiver sido desenhado no loop.
        pygame.display.flip()
        clock.tick(60)
