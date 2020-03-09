import pygame, random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRID_COLOR = (99, 97, 95)
NUMBER_COLOR = (128, 125, 122)
BACKGROUND = (38, 37, 36)
HIGHLIGHT = (75, 75, 75)
HIGHLIGHT_DARK = (50, 50, 50)
RED_SQUARE = (209, 25, 25)
BLUE_SQUARE = (25, 135, 209)
GOLD_SQUARE = (255, 196, 0)
GREEN_SQUARE = (20, 150, 18)
NTABLE = (156, 156, 156)
square_list = [RED_SQUARE, BLUE_SQUARE, GOLD_SQUARE, GREEN_SQUARE]
square_color = random.choice(square_list)
random_RGB = []
for i in range(3):
    color = random.randint(0, 255)
    random_RGB.append(color)


pygame.init()

grid_size = [12, 12]
cell_size = 100
table_offset = [0, 100]
screen_size = (cell_size*(grid_size[0])+table_offset[0], cell_size*(grid_size[1])+table_offset[1])
text_offset = [10, 10]
scroll_up = False
scroll_down = False
first = 2
second = 2
result = first*second
reduced = False

screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("------------ Advanced Multiplication Table Deluxe Master ------------")

done = False
reopen = False
pre_mouse = [0,0]
 

clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            reopen = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scroll_up = True
            elif event.button == 5:
                scroll_down = True
        elif event.type == pygame.KEYDOWN:
            pass
            '''if event.key == pygame.K_UP:
                grid_size += 1
                screen_size = (cell_size*(grid_size-1), cell_size*(grid_size-1))
                screen = pygame.display.set_mode(screen_size)
            elif event.key == pygame.K_DOWN:
                if grid_size > 14:
                    grid_size -= 1
                    screen_size = (cell_size*(grid_size-1), cell_size*(grid_size-1))
                    screen = pygame.display.set_mode(screen_size)'''


    # --- Game logic should go here
    mouse = pygame.mouse.get_pos()
    '''if pre_mouse != mouse:
        grid_size = 14
        screen_size = (cell_size*(grid_size-1), cell_size*(grid_size-1))
        screen = pygame.display.set_mode(screen_size)
        pre_mouse = mouse'''

    square_position = int(mouse[0]/cell_size), int(mouse[1]/cell_size)

    if square_position[0]+1 > 1 and square_position[1] > 1:
        first, second = square_position[0]+1, square_position[1]
    elif square_position[0] == 0 and square_position[1] == 0:
        if scroll_up:
            first += 1
        elif scroll_down:
            first -= 1
    elif square_position[0] == 1 and square_position[1] == 0:
        if scroll_up:
            second += 1
        elif scroll_down:
            second -= 1

    if square_position[1] > 1:
        grid_size[0] = 12
        grid_size[1] = 12
        screen_size = (cell_size*(grid_size[0])+table_offset[0], cell_size*(grid_size[1])+table_offset[1])
        screen = pygame.display.set_mode(screen_size)
    if first >= 12:
        grid_size[0] = first
        screen_size = (cell_size*(grid_size[0])+table_offset[0], cell_size*(grid_size[1])+table_offset[1])
        screen = pygame.display.set_mode(screen_size)
    if second >= 12:
        grid_size[1] = second
        screen_size = (cell_size*(grid_size[0])+table_offset[0], cell_size*(grid_size[1])+table_offset[1])
        screen = pygame.display.set_mode(screen_size)
    
    if first < 2:
        first = 2
    if second < 2:
        second = 2

    result = first*second

    scroll_up = False
    scroll_down = False

    print(square_position, first, second)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND)

    # --- Drawing code should go here


    # text drawing

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 100, False, False)
        
    # text, anti-aliased, color
    text = font.render(f"{first} x {second} = {result}",True,NUMBER_COLOR)
    
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [text_offset[0], text_offset[1]])


    # position highlighting
    if square_position[1] <= 1 or square_position[0] == 0:
        for x in range(1, first-1):
            pygame.draw.rect(screen, HIGHLIGHT_DARK, [x*cell_size, second*cell_size, cell_size, cell_size],0)

        for y in range(2, second):
            pygame.draw.rect(screen, HIGHLIGHT_DARK, [(first-1)*cell_size, y*cell_size, cell_size, cell_size],0)

        pygame.draw.rect(screen, HIGHLIGHT, [(first-1)*cell_size, second*cell_size, cell_size, cell_size],0)
    else:
        for x in range(1, square_position[0]):
            pygame.draw.rect(screen, HIGHLIGHT_DARK, [x*cell_size, second*cell_size, cell_size, cell_size],0)

        for y in range(2, square_position[1]):
            pygame.draw.rect(screen, HIGHLIGHT_DARK, [square_position[0]*cell_size, y*cell_size, cell_size, cell_size],0)

        pygame.draw.rect(screen, HIGHLIGHT, [square_position[0]*cell_size, square_position[1]*cell_size, cell_size, cell_size],0)


    # number drawing

    for x in range(2, grid_size[0]+1):
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 100, False, False)
        
        # text, anti-aliased, color
        text = font.render(str(x),True,NUMBER_COLOR)
        
        # Put the image of the text on the screen at 250x250
        if x >= 10:
            screen.blit(text, [(x-1)*cell_size+10+table_offset[0], 10+table_offset[1]]) 
        else:
            screen.blit(text, [(x-1)*cell_size+30+table_offset[0], 10+table_offset[1]])
    
    for y in range(2, grid_size[1]+1):
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 100, False, False)
        
        # text, anti-aliased, color
        text = font.render(str(y),True,NUMBER_COLOR)
        
        # Put the image of the text on the screen at 250x250
        if y >= 10:
            screen.blit(text, [10+table_offset[0], (y-1)*cell_size+10+table_offset[1]]) 
        else:
            screen.blit(text, [30+table_offset[0], (y-1)*cell_size+10+table_offset[1]])

    for y in range(2, grid_size[1]+1):
        for x in range(2, grid_size[0]+1):
            number = str(x*y)
            # Select the font to use, size, bold, italics
            if int(number) >= 100:
                font = pygame.font.SysFont('Calibri', 70, False, False)
            elif int(number) >= 10:
                font = pygame.font.SysFont('Calibri', 90, False, False)
            else:
                font = pygame.font.SysFont('Calibri', 100, False, False)
            
            # text, anti-aliased, color
            if x == y:
                text = font.render(number,True,square_color)
            else:
                text = font.render(number,True,NUMBER_COLOR)
            
            # Put the image of the text on the screen at 250x250
            if int(number) >= 10:
                screen.blit(text, [(x-1)*cell_size+10+table_offset[0], (y-1)*cell_size+10+table_offset[1]]) 
            else:
                screen.blit(text, [(x-1)*cell_size+30+table_offset[0], (y-1)*cell_size+10+table_offset[1]])





    # grid drawing
    for x in range(1, grid_size[0]):
        pygame.draw.line(screen, GRID_COLOR, [x*cell_size+table_offset[0], 0+table_offset[1]], [x*cell_size+table_offset[0], screen_size[1]+table_offset[1]], 5)
    for y in range(1, grid_size[1]):
        pygame.draw.line(screen, GRID_COLOR, [0+table_offset[0], y*cell_size+table_offset[1]], [screen_size[0]+table_offset[0], y*cell_size+table_offset[1]], 5)

    pygame.draw.line(screen, NTABLE, [table_offset[0], table_offset[1]], [screen_size[0]+table_offset[0], table_offset[1]], 5)
    pygame.draw.line(screen, WHITE, [1*cell_size+table_offset[0], 0+table_offset[1]], [1*cell_size+table_offset[0], screen_size[1]+table_offset[1]], 5)
    pygame.draw.line(screen, WHITE, [0+table_offset[0], 1*cell_size+table_offset[1]], [screen_size[0]+table_offset[0], 1*cell_size+table_offset[1]], 5)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()