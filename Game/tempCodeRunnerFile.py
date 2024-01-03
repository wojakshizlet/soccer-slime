import pygame

class DrawRectangle:
    def __init__(self, screen, colour, x, y, width, height, text, text_colour, fontsize):
        self.screen = screen
        self.colour = pygame.Color(colour)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_colour = pygame.Color(text_colour)
        self.font = pygame.font.Font("freesansbold.ttf", fontsize)

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect, 0)

        if self.text:
            text_surface = self.font.render(self.text, True, self.text_colour)
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.screen.blit(text_surface, text_rect)

pygame.init()
screen = pygame.display.set_mode((800, 430))  
pygame.display.set_caption("Soccer Slime")
font = pygame.font.Font("freesansbold.ttf", 18)
height = screen.get_height()
width = screen.get_width()

button1 = DrawRectangle(screen, "#0c0182", 15, 100, 130, 40, "1 minute", "white", 18)
button2 = DrawRectangle(screen, "#0c0182", 175, 100, 130, 40, "2 minutes", "white", 18)
button3 = DrawRectangle(screen, "#0c0182", ((width - 130) // 2), 100, 130, 40, "3 minutes", "white", 18)
button4 = DrawRectangle(screen, "#0c0182", 495, 100, 130, 40, "8 minutes", "white", 18)
button5 = DrawRectangle(screen, "#0c0182", 655, 100, 130, 40, "Quit", "white", 18)
ground = DrawRectangle(screen, "#808080", 0, height - 100, 800, 100, "Click on an option to play..", "gray", 18)

# Game loop starts here
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    screen.fill((0, 0, 255))  # Use an RGB tuple for the background color
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()
    ground.draw()

    pygame.display.update()
