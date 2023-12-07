from typing import Any
import pygame
from config import *

# Classe do player.
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Importando o sprite do player.
        self.image = pygame.image.load(player_image).convert_alpha()
        # Posicionando o sprite na tela com base na posição passada como parâmetro quando a classe for iniciada.
        self.rect = self.image.get_rect(midbottom = pos)
        # Velocidade com que o sprite vai se mover.
        self.speed = player_speed
        # Variáveis para fazer o player atirar o laser somente uma vez ao pressionar o botão de espaço.
        self.ready = True
        self.laser_time = 0
        self.laser_recharged_time = recharge_time
        # Adicionando uma variável que vai armazenar o sprite do laser.
        self.laser = pygame.sprite.Group()
        
    # Método que pega as entradas do usuário, no caso aqui as teclas pressionadas.    
    def get_input(self):
        keys = pygame.key.get_pressed()

        # Teste se a tecla direita está pressionada e se o valor da posição direita do sprite é menor que a largura da tela (Para limitar o movimento dele dentro da tela). Se sim, ele pega a posição do sprite do player e o move pelo eixo X.
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x = self.rect.x + self.speed

        # Teste se a tecla esquerda está pressionada e se o valor da posição esquerda do sprite é maior que 0 (o valor mínimo da largura da tela).
        elif keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x = self.rect.x - self.speed
    
        # Teste se o botão se espaço está pressionado para atirar o laser.
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            # Mudando o estado de pronto pra ter um intervalo de tiros.
            self.ready = False
            # Marca o tempo do tiro.
            self.laser_time = pygame.time.get_ticks()

    # Método que faz o sprite atirar o laser.
    def shoot_laser(self):
        # Criando uma instância da classe Laser toda vez que o laser é disparado.
        self.laser.add(Laser(self.rect.center))

    # Método de recarga do laser.
    def recharge_laser(self):
        if not self.ready:
            # Verifica o tempo atual e subtrai pelo tempo do tiro anterior pra saber se já se passou o tempo necessário de recarga do laser.
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_recharged_time:
                self.ready = True

    # Método que atualiza o sprite com bases nas teclas pressionadas.
    def update(self):
        self.get_input()
        self.recharge_laser()
        self.laser.update()

# Classe do laser.
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Criando o sprite do laser.
        self.image = pygame.Surface((laser_width, laser_height))
        self.image.fill(laser_color)
        # Posicionando o centro em uma dada posição.
        self.rect = self.image.get_rect(center = pos)
        # Definindo a velocidade do laser.
        self.speed = laser_speed

    # Método para excluir os lasers assim que eles saem da tela.
    def delete(self):
        if self.rect.y >= screen_height or self.rect.y < 0:
            self.kill()

    # Atualizando a posição do laser no eixo y, pra fazer o sprite se movimentar.
    def update(self):
        self.rect.y = self.rect.y - self.speed
        self.delete()
        
# Classe dos inimigos:
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        # Especificando a imagem do sprite de acordo com a cor passada.
        enemy_image = "img/" + color + "_enemy" + ".png"
        # Importando o sprite do enemy.
        self.image = pygame.image.load(enemy_image).convert_alpha()
        # Posicionando o sprite na tela com base na posição passada como parâmetro quando a classe for iniciada.
        self.rect = self.image.get_rect(topleft = pos)

    # Método que atualiza o movimento do inimigo ao longo do eixo x.
    def update(self, speed):
        self.rect.x = self.rect.x + speed

# Classe do botão de start:
class Button:
    def __init__(self, x, y, width, height, foreground_color, background_color, content, font_size):
        pass
