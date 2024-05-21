import pygame
import math

# button1 = drawRectangle(screen, "#0c0182", 15, 100, 130, 40, "1 minute", "white", 18)
# button2 = drawRectangle(screen, "#0c0182", 175, 100, 130, 40, "2 minutes", "white", 18)
# button3 = drawRectangle(screen, "#0c0182", ((width - 130) // 2), 100, 130, 40, "3 minutes", "white", 18)
# button4 = drawRectangle(screen, "#0c0182", 495, 100, 130, 40, "8 minutes", "white", 18)
# button5 = drawRectangle(screen, "#0c0182", 655, 100, 130, 40, "Quit", "white", 18)

class Player:
    def __init__(self, x, y, width, height, colour, score, screen_width, screen_height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = colour
        self.visible = True
        self.score = 0
        self.mass = 5
        self.velo = 5
        self.is_jumping = False
        self.jump_velocity = 15
        self.gravity = 1
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, pygame.Color(self.colour), self.rect)

    def move(self, dx):
        new_x = self.rect.x + dx
        if new_x < 0:
            self.rect.x = 0
            
        if (0 <= new_x <= 720):
            self.rect.x = new_x    
        
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velo = self.jump_velocity
        
    def update_jump(self):
        if self.is_jumping:
            self.rect.y -= self.velo
            self.velo -= self.gravity

            if self.rect.y >= 325:
                self.rect.y = 325
                self.is_jumping = False
                self.velo = self.jump_velocity
                
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y


class soccerSlimeGame:
    def __init__(self):
        self.width = 830
        self.height = 400
        self.player1 = Player(0, 325, 80, 5, "white", 0, self.width, self.height)
        self.player2 = Player(720, 325, 80, 5, "white", 0, self.width, self.height)
        self.visible = True
        self.font = None
        
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
    
    def getP1Score(self):
        return self.player1Score
    
    def getP2Score(self):
        return self.player2Score
    
    def drawScores(self, screen):
        p1ScoreText = self.font.render(f"Player 1: {self.player1.score}", True, pygame.Color("white"))
        p2ScoreText = self.font.render(f"{self.player2.score}: Player 2", True, pygame.Color("white"))

        screen.blit(p1ScoreText, (10, 10))
        screen.blit(p2ScoreText, (self.width - 135, 10))
        
    def renderGraphics(self):
        # Game loop starts here
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800, 430))  
        pygame.display.set_caption("Soccer Slime")
        height = screen.get_height()
        width = screen.get_width()
        self.font = pygame.font.Font("freesansbold.ttf", 18)
        
        running = True
        while running:
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    
                keys = pygame.key.get_pressed()
               
            #player 1 movement        
            if keys[pygame.K_LEFT]:    
                self.player1.move(-5)
                        
            if keys[pygame.K_RIGHT]:
               self.player1.move(5)
               
            if keys[pygame.K_UP]:
                self.player1.jump()
            
            self.player1.update_jump()
                
            #player 2 movement
            if keys[pygame.K_d]:
                self.player2.move(5)
                
            if keys[pygame.K_a]:
                self.player2.move(-5)
                
            if keys[pygame.K_w]:
                self.player2.jump()
            
            self.player2.update_jump()
                    
            # if you need it, call visibility function using self.toggle_visibility() AFTER any sort of event handler
                
            screen.fill("blue")
            self.createRect(screen, "#808080", 0, (height - 100), 800, 100, "slime soccer!!!!1!1!!!!!!!!!", "gray", 16, self.visible)
            self.drawScores(screen)
            
            self.player1.draw(screen)
            self.player2.draw(screen)
            
            pygame.display.update()

if __name__ == "__main__":
    game = soccerSlimeGame()
    game.renderGraphics()