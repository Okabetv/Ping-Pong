from turtle import screensize
import pygame, sys, random


def animazioni_palla():
  global vel_palla_x, vel_palla_y, punteggio_player, punteggio_player2
  palla.x += vel_palla_x
  palla.y += vel_palla_y

  if palla.top <= 0 or palla.bottom >= screen_height:
    vel_palla_y *= -1
  if palla.left <= 0:
    punteggio_player += 1
    palla_restart()
    score_time = pygame.time.get_ticks()
  if palla.right >= screen_width:
    punteggio_player2 += 1
    palla_restart()

  #Collisioni
  if palla.colliderect(player) or palla.colliderect(player2):
    vel_palla_x *= -1

def animazioni_player():
  player.y += vel_player
  if player.top <= 0:
    player.top = 0
  if player.bottom >= screen_height:
    player.bottom = screen_height

def animazioni_player2():
  if player2.top < palla.y:
    player2.top += vel_player2
  if player2.bottom > palla.y:
    player2.bottom -= vel_player2
  if player2.top <= 0:
    player2.top = 0
  if player2.bottom >= screen_height:
    player2.bottom = screen_height

def palla_restart():
  global vel_palla_x, vel_palla_y
  palla.center = (screen_width/2, screen_height/2)
  vel_palla_y *= random.choice((1,-1))
  vel_palla_x *= random.choice((1,-1))

#setup generale
pygame.init()
clock = pygame.time.Clock()

#setup della finestra di gioco
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

#Rettangoli di gioco
palla = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
player2 = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#Colori
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#Animazioni
vel_palla_x = 7 * random.choice((1,-1))
vel_palla_y = 7 * random.choice((1,-1))
vel_player = 0
vel_player2 = 7

#Variabile di testo
punteggio_player = 0
punteggio_player2 = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

#Timer
score_time = None

def game():
  while True:
    global vel_palla_x, vel_palla_y, vel_player, vel_player2
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit()
        if event.key == pygame.K_DOWN:
          vel_player += 7
        if event.key == pygame.K_UP:
          vel_player -= 7
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
          vel_player -= 7
        if event.key == pygame.K_UP:
          vel_player += 7

    animazioni_palla()
    animazioni_player()
    animazioni_player2()

    #Visuale
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, palla)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    player_text = game_font.render(f"{punteggio_player}",False,light_grey)
    screen.blit(player_text,(660,470))

    player_text2 = game_font.render(f"{punteggio_player2}",False,light_grey)
    screen.blit(player_text2,(600,470))

    #Update della finestra
    pygame.display.flip()
    clock.tick(60)