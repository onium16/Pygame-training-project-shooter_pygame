import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 50)

screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width,  screen_height))

pygame.display.set_caption('Space raid 1.0.0')


screen_image = pygame.image.load('images/screen.png')
screen_width, screen_heigth = screen_image.get_size()
screen_image_x, screen_image_y = 0, 0



FIGHTER_STEP = 0.5
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_heigth = fighter_image.get_size()
fighter_x, fighter_y = screen_width / 2 - fighter_width/2, screen_height - fighter_heigth
fighter_is_moving_left, fighter_is_moving_right = False, False

ROCKET_STEP = 0.5
rocket_image = pygame.image.load('images/rocket.png')
rocket_wight, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = 0, 0
rocket_was_fired = False

ALIEN_STEP = 0.03
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')
alien_wight, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_wight), 0


game_is_running = True

game_score = 0

while game_is_running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x, rocket_y = fighter_x + fighter_width/2 - rocket_wight/2, \
                fighter_y + fighter_heigth/2 - rocket_height*1.8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >=  FIGHTER_STEP:
        fighter_x -=  FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x +=  FIGHTER_STEP
  
    alien_y += alien_speed

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False
    if rocket_was_fired:
        rocket_y -= ROCKET_STEP

    screen.fill(screen_fill_color)
    screen.blit(screen_image, (screen_image_x, screen_image_y))
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    game_score_text = game_font.render(f"Your score is: {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()
   
    if alien_y + alien_height > fighter_y:
        game_is_running = False


    if rocket_was_fired and \
            alien_x < rocket_x < alien_x + alien_wight - rocket_wight and \
            rocket_y < alien_y + alien_height - rocket_height:
        rocket_was_fired = False
        alien_x, alien_y = randint(0, screen_width - alien_wight), 0
        alien_speed += ALIEN_STEP /2
        game_score += 1

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle =  game_over_text.get_rect()
game_over_rectangle.center = (screen_width/2, screen_height/2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
 
pygame.quit()