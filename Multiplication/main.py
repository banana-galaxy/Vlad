import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRID_COLOR = (99, 97, 95)
NUMBER_COLOR = (128, 125, 122)
BACKGROUND = (38, 37, 36)
HIGHLIGHT = (75, 75, 75)
HIGHLIGHT_DARK = (50, 50, 50)


pygame.init()

grid_size = 14
cell_size = 100
screen_size = (cell_size*(grid_size-1), cell_size*(grid_size-1))

screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("------------ Advanced Multiplication Table ------------")

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                grid_size += 1
                screen_size = (cell_size*(grid_size-1), cell_size*(grid_size-1))
                screen = pygame.display.set_mode(screen_size)


    # --- Game logic should go here
    mouse = pygame.mouse.get_pos()
    if pre_mouse != mouse:
        grid_size = 14
        screen_size = (cell_size*(grid_size-1), cell_size*(grid_size-1))
        screen = pygame.display.set_mode(screen_size)
        pre_mouse = mouse

    square_position = int(mouse[0]/cell_size), int(mouse[1]/cell_size)

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND)

    # --- Drawing code should go here

    # mouse position highlighting

    if square_position[0] > 0 and square_position[1] > 0:
        for x in range(1, square_position[0]+1):
            pygame.draw.rect(screen, HIGHLIGHT_DARK, [x*cell_size, square_position[1]*cell_size, cell_size, cell_size],0)

        for y in range(1, square_position[1]+1):
            pygame.draw.rect(screen, HIGHLIGHT_DARK, [square_position[0]*cell_size, y*cell_size, cell_size, cell_size],0)

        pygame.draw.rect(screen, HIGHLIGHT, [square_position[0]*cell_size, square_position[1]*cell_size, cell_size, cell_size],0)

    # number drawing

    for x in range(1, grid_size):
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 100, False, False)
        
        # text, anti-aliased, color
        text = font.render(str(x),True,NUMBER_COLOR)
        
        # Put the image of the text on the screen at 250x250
        if x >= 10:
            screen.blit(text, [x*cell_size+10, 10]) 
        else:
            screen.blit(text, [x*cell_size+30, 10])
    
    for y in range(1, grid_size):
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 100, False, False)
        
        # text, anti-aliased, color
        text = font.render(str(y),True,NUMBER_COLOR)
        
        # Put the image of the text on the screen at 250x250
        if y >= 10:
            screen.blit(text, [10, y*cell_size+10]) 
        else:
            screen.blit(text, [30, y*cell_size+10])

    for y in range(1, grid_size):
        for x in range(1, grid_size):
            number = str(x*y)
            # Select the font to use, size, bold, italics
            if int(number) >= 100:
                font = pygame.font.SysFont('Calibri', 70, False, False)
            elif int(number) >= 10:
                font = pygame.font.SysFont('Calibri', 90, False, False)
            else:
                font = pygame.font.SysFont('Calibri', 100, False, False)
            
            # text, anti-aliased, color
            text = font.render(number,True,NUMBER_COLOR)
            
            # Put the image of the text on the screen at 250x250
            if int(number) >= 10:
                screen.blit(text, [x*cell_size+10, y*cell_size+10]) 
            else:
                screen.blit(text, [x*cell_size+30, y*cell_size+10])





    # grid drawing
    for x in range(1, grid_size):
        pygame.draw.line(screen, GRID_COLOR, [x*cell_size, 0], [x*cell_size, screen_size[1]], 5)
    for y in range(1, grid_size):
        pygame.draw.line(screen, GRID_COLOR, [0, y*cell_size], [screen_size[0], y*cell_size], 5)

    pygame.draw.line(screen, WHITE, [1*cell_size, 0], [1*cell_size, screen_size[1]], 5)
    pygame.draw.line(screen, WHITE, [0, 1*cell_size], [screen_size[0], 1*cell_size], 5)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()