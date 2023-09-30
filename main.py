import random
import pygame
import time

snake_speed = 15

# fruit_spawned variable
fruit_spawned = False

#Window Size
window_x = 720
window_y = 480

#defind colors
black = pygame.Color(0, 0, 0)
white =pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#init pygame
pygame. init()

# Initiatise game window
pygame.display.set_caption( ' P Y Snakes ' )
game_window = pygame.display.set_mode((window_x, window_y))

#FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

#defining first 4 blocks of snake body
snake_body = [[100,50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

#fruit position
fruit_position = [
    random.randrange(start=1, stop=(window_x // 10)) * 10,
    random.randrange(start=1, stop=(window_y // 10)) * 10
]

#setting snake direction
#right
direction = "RIGHT"
change_to = direction

#initial score
score = 0

#score disp func
def show_score(choice, color, font, size):
    # Creating font object
    score_font = pygame.font.SysFont(font, size)
    # Surface obj
    score_surface = score_font.render("Score : " + str(score), True, color)
    # Object for text
    score_rect = score_surface.get_rect()
    # Disp text
    game_window.blit(score_surface, score_rect)


#game over
def game_over():
    #creat font obj
    my_font = pygame.font.SysFont(name="times new roman", size=50)
    #text sur on which text
    game_over_surface = my_font.render("Your Score is : " + str(score), True, red)
    #rectangular obj
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    #after 2 second quit
    time.sleep(2)
    #deact pygame Lib
    pygame.quit()
    #quit prog
    quit()

# Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawned = False
    else:
        snake_body.pop()

    if not fruit_spawned:
        fruit_position = [random.randrange(start=1, stop=(window_x // 10)) * 10,
                           random.randrange(start=1, stop=(window_y // 10)) * 10]
        fruit_spawned = True

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, white, "times new roman", 20)

    pygame.display.update()

    fps.tick(snake_speed)
