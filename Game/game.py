import pygame
import math

# button1 = drawRectangle(screen, "#0c0182", 15, 100, 130, 40, "1 minute", "white", 18)
# button2 = drawRectangle(screen, "#0c0182", 175, 100, 130, 40, "2 minutes", "white", 18)
# button3 = drawRectangle(screen, "#0c0182", ((width - 130) // 2), 100, 130, 40, "3 minutes", "white", 18)
# button4 = drawRectangle(screen, "#0c0182", 495, 100, 130, 40, "8 minutes", "white", 18)
# button5 = drawRectangle(screen, "#0c0182", 655, 100, 130, 40, "Quit", "white", 18)



class soccerSlimeGame:
    def __init__(self, player1Score, player2Score):
        self.player1Score = 0
        self.player2Score = 0
        self.x = 0
        self.y = 0
        self.visible = True
        
    @staticmethod
    def createRect(screen, colour, x, y, width, height, text, text_colour, fontsize, visible):
        rect = pygame.Rect(x, y, width, height)
        text_colour = pygame.Color(text_colour)
        font = pygame.font.Font("freesansbold.ttf", fontsize)

        if visible:
            pygame.draw.rect(screen, pygame.Color(colour), rect, 0)

            if text:
                text_surface = font.render(text, True, text_colour)
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)
        return rect            
                
    def toggle_visibility(self):
        self.visible = not self.visible
    
    def getP1Score(self, player1Score):
        return self.player1Score
    
    def getP2Score(self, player2Score):
        return self.player2Score
    
        
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
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player1.x -= 10
                    elif event.key == pygame.K_RIGHT:
                        player1.x += 10
                    
                # if you need it, call visibility function using self.toggle_visibility() AFTER any sort of event handler
                
                screen.fill("blue")
                rect = self.createRect(screen, "#808080", 0, (height - 100), 800, 100, "slime soccer!!!!1!1!!!!!!!!!", "gray", 16, self.visible)
                
                player1 = self.createRect(screen, "white", 0, (height - 110), 80, 10, "", "white", 1, self.visible)

                center = (width // 2, height // 2)
                #pygame.draw.arc(surface, color, rect, start_angle, stop_angle, width=1)
                
                pygame.display.update()

if __name__ == "__main__":
    game = soccerSlimeGame(0, 0)
    game.renderGraphics()