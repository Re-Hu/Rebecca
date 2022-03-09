import pygame
import tkinter as tk
import solve as solution


#def showinput():
class Board():
    def __init__(self, board = None):
#        super().__init__()
        self.input = tk.Tk()
        self.input.geometry('800x150')
        self.input.title("Input Sudoku question")
        self.entry = tk.Entry()
        self.but = tk.Button(text='submit', command = self.getinput)
        self.but2 = tk.Button(text='quit', command = self.turnoff)
        self.label = tk.Label(self.input, text = "Please enter your sudoku question on the box above. ")
        self.label.pack()
        self.label.place(x = 200, y = 70)
        
        self.label1 = tk.Label(self.input, text = "You should enter the question line by line, the empty blank should be 0. ")
        self.label1.pack()
        self.label1.place(x = 200, y = 90)
        
        self.label2 = tk.Label(self.input, text = "The example format is (2, 0, 4, 0, 3, 4, 1, 0, 0, 0, 0, 4, 4, 3, 0, 0), you should not include the brackets and the white between numbers.")
        self.label2.pack()
        self.label2.place(x = 10, y = 110)
        
        self.entry.pack()
        self.but.pack()
        self.but2.pack()
        
        self.sudoku_li = [[], [], [], []]
        
#    Get the input puzzle, swtich it to list
    def getinput(self):
        self.entry_get = self.entry.get()
        entry_li = self.entry_get.split(",")
        count = 0
        index = 0
        for i in entry_li:
#            print("i", i)
#            print("index", count, index, int(i))
            if count < 4:
                self.sudoku_li[index].append(int(i))
            else:
                count = 0
                index += 1
                self.sudoku_li[index].append(int(i))
            count += 1
#            print(self.sudoku_li)
        self.get_solution(self.sudoku_li)

    def get_solution(self, sudoku):
        print("get solution", sudoku)
        solu = solution.solve(sudoku)
        print("solu", sudoku)
        self.showsolution(solu)
        
                    
# Show the result in a new window
    def showsolution(self, Sudoku):
        self.input.quit
        print("solution")
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
            #draw_number()
            
            for i in range(len(Sudoku)):
                for j in range(len(Sudoku[0])):
                    txt = font80.render(str(Sudoku[i][j] if Sudoku[i][j] not in [0, '0'] else ''), True, (0, 0, 0))
                    x, y = j * 100 + 40, i * 100 + 35
                    screen.blit(txt, (x, y))
            
            txt1 = font100.render(('Project: Sudoku '), True, (0, 0, 0))
            txt2 = font100.render(('Members: Rebecca'), True, (0, 0, 0))
            x, y = 10, 408
            x1, y1 = 10, 430
            screen.blit(txt1, (x, y))
            screen.blit(txt2, (x1, y1))
            # flip
            pygame.display.flip()
        
        pygame.quit()

# Start the system
    def turnon(self):
        self.input.mainloop()

# Terminate the system
    def turnoff(self):
        self.input.quit()
            
    

if __name__ == "__main__":
    board = Board()
    board.turnon()
    