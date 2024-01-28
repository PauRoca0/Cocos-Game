import pygame
import map

#Create sprite class
class Ghost(pygame.sprite.Sprite):
    def __init__(self, screen, group, nFantasma, nRow, nColumn):
        #Add this class into the group
        super().__init__(group)

        self.nRow = nRow
        self.nColumn = nColumn

        self.screen = screen

        self.nFantasma = nFantasma

        #Load ghost image
        self.image = pygame.image.load("assets/pacmanGhost.png").convert()
        self.image = pygame.transform.scale(self.image, (self.screen.get_width() / (nColumn * 1.5), self.screen.get_height() / (nRow * 2)))
        self.image.set_colorkey((0, 0, 0))

        self.tileWidth = self.screen.get_width() / nColumn
        self.tileHeight = self.screen.get_height() / nRow

        if nFantasma == 1:
            self.rect = self.image.get_rect(center = pygame.Vector2((self.tileWidth * map.ghostPosition[0] + 1) + self.tileWidth / 2, (self.tileHeight * map.ghostPosition[1] + 1) + self.tileHeight / 2))
        
        elif nFantasma == 2:
            self.rect = self.image.get_rect(center = pygame.Vector2((self.tileWidth * map.ghostPosition2[1] + 1) + self.tileWidth / 2, (self.tileHeight * map.ghostPosition2[0] + 1) + self.tileHeight / 2))

        #Ghost move time
        self.ghostDelay = 700
        self.GHOSTMOVE = pygame.USEREVENT + 1
        pygame.time.set_timer(self.GHOSTMOVE, self.ghostDelay)

    #When ghost moves
    def ghostMovementTiming(self, event):
        if event.type == self.GHOSTMOVE:
            self.ghostMovement()

            pygame.time.set_timer(self.GHOSTMOVE, self.ghostDelay)

    #All the stuff that makes ghost decisions
    def ghostMovement(self):
        
        if self.nFantasma == 1:
            self.ghostPosition = map.ghostPosition
            self.ghostNum = 4
        
        elif self.nFantasma == 2:
            self.ghostPosition = map.ghostPosition2
            self.ghostNum = 5

        if map.playerPosition[1] > self.ghostPosition[1]:

                if map.map[self.ghostPosition[0]][self.ghostPosition[1] + 1] in (0, 2, 3):
                        self.moveRight()
                
                elif map.playerPosition[0] > self.ghostPosition[0]:
                    if map.map[self.ghostPosition[0] + 1][self.ghostPosition[1]] in (0, 2, 3):
                        self.moveDown()
                
                elif map.map[self.ghostPosition[0] - 1][self.ghostPosition[1]] in (0, 2, 3):
                    self.moveUp()
        
        elif map.playerPosition[1] < self.ghostPosition[1]:

                if map.map[self.ghostPosition[0]][self.ghostPosition[1] - 1] in (0, 2, 3):      
                        self.moveLeft()
                
                elif map.playerPosition[0] > self.ghostPosition[0]:
                    if map.map[self.ghostPosition[0] + 1][self.ghostPosition[1]] in (0, 2, 3):
                        self.moveDown()
                
                elif map.map[self.ghostPosition[0] - 1][self.ghostPosition[1]] in (0, 2, 3):
                    self.moveUp()

        elif map.playerPosition[0] < self.ghostPosition[0]:
            if map.map[self.ghostPosition[0] - 1][self.ghostPosition[1]] in (0, 2, 3):
                self.moveUp()
            
            elif map.playerPosition[1] > self.ghostPosition[1]:
                if map.map[self.ghostPosition[0]][self.ghostPosition[1] + 1] in (0, 2, 3):
                    self.moveRight()
            
            elif map.map[self.ghostPosition[0]][self.ghostPosition[1] - 1] in (0, 2, 3): 
                self.moveLeft()
        
        elif map.playerPosition[0] > self.ghostPosition[0]:

            if map.map[self.ghostPosition[0] + 1][self.ghostPosition[1]] in (0, 2, 3):
                self.moveDown()
            
            elif map.playerPosition[1] > self.ghostPosition[1]:
                if map.map[self.ghostPosition[0]][self.ghostPosition[1] + 1] in (0, 2, 3):
                    self.moveRight()
            
            elif map.map[self.ghostPosition[0]][self.ghostPosition[1] - 1] in (0, 2, 3): 
                self.moveLeft()
            

    #All the movement
    def moveUp(self):
        if [self.ghostPosition[0], self.ghostPosition[1]] not in map.puntsPositions:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 0
        
        else:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 2
        
        map.map[self.ghostPosition[0] - 1][self.ghostPosition[1]] = self.ghostNum

        self.rect.y -= self.screen.get_height() / self.nRow

    def moveDown(self):
        if [self.ghostPosition[0], self.ghostPosition[1]] not in map.puntsPositions:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 0
        
        else:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 2
        
        map.map[self.ghostPosition[0] + 1][self.ghostPosition[1]] = self.ghostNum

        self.rect.y += self.screen.get_height() / self.nRow

    def moveRight(self):
        if [self.ghostPosition[0], self.ghostPosition[1]] not in map.puntsPositions:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 0
        
        else:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 2
        
        map.map[self.ghostPosition[0]][self.ghostPosition[1] + 1] = self.ghostNum

        self.rect.x += self.screen.get_width() / self.nColumn
    
    def moveLeft(self):
        if [self.ghostPosition[0], self.ghostPosition[1]] not in map.puntsPositions:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 0
        
        else:
            map.map[self.ghostPosition[0]][self.ghostPosition[1]] = 2
        
        map.map[self.ghostPosition[0]][self.ghostPosition[1] - 1] = self.ghostNum

        self.rect.x -= self.screen.get_width() / self.nColumn


