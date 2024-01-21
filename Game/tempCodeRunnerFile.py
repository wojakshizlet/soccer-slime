import pygame

class drawRectangle:
    def __init__(self, screen, colour, x, y, width, height, text, text_colour, fontsize):
        self.screen = screen
        self.colour = pygame.Color(colour)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_colour = pygame.Color(text_colour)
        self.font = pygame.font.Font("freesansbold.ttf", fontsize)
        self.visible = True

    def draw(self):
        if self.visible:
            pygame.draw.rect(self.screen, self.colour, self.rect, 0)

            if self.text:
                text_surface = self.font.render(self.text, True, self.text_colour)
                text_rect = text_surface.get_rect(center=self.rect.center)
                self.screen.blit(text_surface, text_rect)

    def toggle_visibility(self):
        self.visible = False

# button1 = drawRectangle(screen, "#0c0182", 15, 100, 130, 40, "1 minute", "white", 18)
# button2 = drawRectangle(screen, "#0c0182", 175, 100, 130, 40, "2 minutes", "white", 18)
# button3 = drawRectangle(screen, "#0c0182", ((width - 130) // 2), 100, 130, 40, "3 minutes", "white", 18)
# button4 = drawRectangle(screen, "#0c0182", 495, 100, 130, 40, "8 minutes", "white", 18)
# button5 = drawRectangle(screen, "#0c0182", 655, 100, 130, 40, "Quit", "white", 18)



class soccerSlimeGame():
    def __init__(self, player1Score, player2Score):
        self.player1Score = 0
        self.player2Score = 0

        
    def renderGraphics(self):
        # Game loop starts here
        pygame.init()
        screen = pygame.display.set_mode((800, 430))  
        pygame.display.set_caption("Soccer Slime")
        font = pygame.font.Font("freesansbold.ttf", 18)
        height = screen.get_height()
        width = screen.get_width()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                screen.fill("blue")
            
                ground = drawRectangle(screen, "#808080", 0, height - 100, 800, 100, " ", "gray", 16)
                ground.draw()
            
            
                pygame.display.update()

if __name__ == "__main__":
    game = soccerSlimeGame(0, 0)
    game.renderGraphics()