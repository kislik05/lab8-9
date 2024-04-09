import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
COLOR = red

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1

figyra = None

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def square_rect(x1, x2, y1, y2):
    side_length = min(abs(x1 - x2), abs(y1 - y2))
    return pygame.Rect(min(x1, x2), min(y1, y2), side_length, side_length)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print("Выберите цвет: white, black, red, green, blue")
            COLOR = str(input())
            print("Выберите фигуру: prim tr, prim tr, kv, romb,")
            figyra = input() 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB was clicked!")
            print(event.pos)
            figyra = "prim"  
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if figyra:  # Изменено на проверку на истинность строки
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB was released!")
            print(event.pos)
            figyra = None 
            baseLayer.blit(screen, (0, 0))
            currX = event.pos[0]
            currY = event.pos[1]

    # Проверка на выбор фигуры и рисование соответствующей фигуры
    if figyra == "prim":
        screen.blit(baseLayer, (0, 0))
        pygame.draw.rect(screen, COLOR, calculate_rect(prevX, currX, prevY, currY), 2)
    elif figyra == "kv":
        screen.blit(baseLayer, (0, 0))
        pygame.draw.rect(screen, COLOR, square_rect(prevX, currX, prevY, currY), 2)

    pygame.display.flip()
