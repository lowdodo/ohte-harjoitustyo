import pygame
import sys
from imagepath import imagepath
from button import Button
from sprites.child import Child
from sprites.petal import Petal
from game_loop import GameLoop 

pygame.init()
SCREEN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Main menu")

BG = (0, 0, 0)

def main_menu():
    while True:
        SCREEN.fill(BG)
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = pygame.font.SysFont(None, 100).render("MAIN MENU", True, (255, 255, 255))
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=imagepath("button.png"), pos=(500, 250), 
                            text="PLAY", font=pygame.font.SysFont(None, 75))
        QUIT_BUTTON = Button(image=imagepath("button.png"), pos=(500, 400), 
                            text="QUIT", font=pygame.font.SysFont(None, 75))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
                    main()
                if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def main(): 
    pygame.display.set_caption("prescreen")
    child_sprite = Child((50, 350))

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill(BG)
        PLAY_TEXT = pygame.font.SysFont(None, 25).render("Whats that? Oh. a child.... come here", True, (255, 255, 255))
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(child_sprite.image, child_sprite.rect)

        PLAY_NEXT = Button(image=imagepath("nextbutton.png"), pos=(800, 500), text=None, font=None )
        PLAY_NEXT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_NEXT.check_for_input(PLAY_MOUSE_POS):
                    while child_sprite.rect.x <= 1000:
                        child_sprite.rect.x += 1
                        SCREEN.fill(BG)
                        PLAY_TEXT = pygame.font.SysFont(None, 25).render("Whats that? Oh. a child.... come here", True, (255, 255, 255))
                        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
                        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
                        SCREEN.blit(child_sprite.image, child_sprite.rect)
                        pygame.display.update()
                    level1()
                    
        pygame.display.update()


def level1():
    pygame.display.set_caption("level1")
    SCREEN.fill(BG)
    child_sprite = Child((50, 350))
    petal_sprite = Petal((800, 450))
    clock = pygame.time.Clock()
    SCREEN.blit(child_sprite.image, child_sprite.rect)
    SCREEN.blit(petal_sprite.image, petal_sprite.rect)
    game_loop = GameLoop(renderer=None, event_queue=pygame.event, clock=clock, child_sprite=child_sprite, petal_sprite=petal_sprite)
    pygame.display.update()
    game_loop.start()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def saved():
    pass
    #TODO

main_menu()

pygame.quit()
