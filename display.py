import pygame


Sudoku = [
        [4, 3, 2, 1],
        [2, 1, 3, 4],
        [1, 2, 4, 3],
        [3, 4, 1, 2]
    ]
"""
def draw_background():
    # white background
    backgroud = (255, 255, 255)  # 背景色
    screen.fill(backgroud)
    # draw game board
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 800), 5)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 800), 1)
    pygame.draw.rect(screen, (0, 0, 0), (400, 0, 400, 800), 5)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 800), 1)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 400), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (800, 200), 1)
    pygame.draw.rect(screen, (0, 0, 0), (0, 400, 800, 400), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (800, 600), 1)


def draw_number():
    for i in range(len(Sudoku)):
        for j in range(len(Sudoku[0])):
            txt = font80.render(str(Sudoku[i][j] if Sudoku[i][j] not in [0, '0'] else ''), True, (0, 0, 0))
            x, y = j * 200 + 80, i * 200 + 70
            screen.blit(txt, (x, y))

"""
def main():
    # init pygame
    pygame.init()

    # contant
    SIZE = [400, 450]
    font80 = pygame.font.SysFont('Times', 40)
    font100 = pygame.font.SysFont('Times', 15)

    # create screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sudoku-game solution")

    # main loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        # background
        #draw_background()
        # white background
        backgroud = (255, 255, 255)  # 背景色
        screen.fill(backgroud)
        # draw game board

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 200, 400), 3)
        pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 400), 1)
        pygame.draw.rect(screen, (0, 0, 0), (200, 0, 200, 400), 3)
        pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 400), 1)

        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 200), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, 100), (400, 100), 1)
        pygame.draw.rect(screen, (0, 0, 0), (0, 200, 400, 300), 3)
        pygame.draw.line(screen, (0, 0, 0), (0, 300), (400, 300), 1)
        pygame.draw.line(screen, (0, 0, 0), (0, 450), (400, 450), 5)
        # numbers
        """
        #draw_number()
        for i in range(len(Sudoku)):
            for j in range(len(Sudoku[0])):
                txt = font80.render(str(Sudoku[i][j] if Sudoku[i][j] not in [0, '0'] else ''), True, (0, 0, 0))
                x, y = j * 100 + 40, i * 100 + 35
                screen.blit(txt, (x, y))
        """
        txt1 = font100.render(('Project: Sudoku '), True, (0, 0, 0))
        txt2 = font100.render(('Members: Rebecca'), True, (0, 0, 0))
        x, y = 10, 408
        x1, y1 = 10, 430
        screen.blit(txt1, (x, y))
        screen.blit(txt2, (x1, y1))
        # flip
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()