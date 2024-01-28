import pygame
import map

#Sprite class for Player
class Player(pygame.sprite.Sprite):
    def __init__(self, screen, group, nColumn, nRow):
        #Add it into the sprite group
        super().__init__(group)

        self.screen = screen
        
        #Load image
        self.image = pygame.image.load("assets/pacmanPng.png").convert()
        self.image = pygame.transform.scale(self.image, (self.screen.get_width() / (nColumn * 2), self.screen.get_height() / (nRow * 1.5)))
        self.image.set_colorkey((0, 0, 0))

        self.tileWidth = self.screen.get_width() / nColumn
        self.tileHeight = self.screen.get_height() / nRow

        #Site where player will start
        self.rect = self.image.get_rect(center = pygame.Vector2((self.tileHeight * map.playerPosition[1] + 1) + self.tileHeight / 2, (self.tileWidth * map.playerPosition[0] + 1) + self.tileWidth / 2))

        #Movement times
        self.CANMOVE = pygame.USEREVENT + 0
        pygame.time.set_timer(self.CANMOVE, 0)
        self.canMove = True

    #All the movement stuff
    def playerMovement(self, event):
        playerDelay = 150 #ms
    
        if event.type == self.CANMOVE:
            self.canMove = True

        if event.type == pygame.KEYDOWN and self.canMove:
            if event.key == pygame.K_UP:
                if self.movePlayerUp():
                    self.rect.y -= self.screen.get_height() / map.nRow
                    self.canMove = False
                    pygame.time.set_timer(self.CANMOVE, playerDelay)

            if event.key == pygame.K_DOWN:
                if self.movePlayerDown():
                    self.rect.y += self.screen.get_height() / map.nRow
                    self.canMove = False
                    pygame.time.set_timer(self.CANMOVE, playerDelay)
            
            if event.key == pygame.K_LEFT:
                if self.movePlayerLeft():
                    self.rect.x -= self.screen.get_width() / map.nColumn
                    self.canMove = False
                    pygame.time.set_timer(self.CANMOVE, playerDelay)
            
            if event.key == pygame.K_RIGHT:
                if self.movePlayerRight():
                    self.rect.x += self.screen.get_width() / map.nColumn
                    self.canMove = False
                    pygame.time.set_timer(self.CANMOVE, playerDelay)

    #Check if player can move somewhere and then move it
    def movePlayerUp(self):

        if map.map[map.playerPosition[0] - 1][map.playerPosition[1]] in (0, 2, 4):
            map.map[map.playerPosition[0]][map.playerPosition[1]] = 0
            
            if [map.playerPosition[0], map.playerPosition[1]] in map.puntsPositions:
                map.puntsPositions.remove([map.playerPosition[0], map.playerPosition[1]])

            map.map[map.playerPosition[0] - 1][map.playerPosition[1]] = 3
            
            return True
        
        return False

    def movePlayerDown(self):

        if map.map[map.playerPosition[0] + 1][map.playerPosition[1]] in (0, 2) or map.map[map.playerPosition[0] + 1][map.playerPosition[1]] >= 4:
            map.map[map.playerPosition[0]][map.playerPosition[1]] = 0

            if [map.playerPosition[0], map.playerPosition[1]] in map.puntsPositions:
                map.puntsPositions.remove([map.playerPosition[0], map.playerPosition[1]])

            map.map[map.playerPosition[0] + 1][map.playerPosition[1]] = 3

            return True

        return False

    def movePlayerLeft(self):

        if map.map[map.playerPosition[0]][map.playerPosition[1] - 1] in (0, 2) or map.map[map.playerPosition[0]][map.playerPosition[1] - 1] >= 4:
            map.map[map.playerPosition[0]][map.playerPosition[1]] = 0

            if [map.playerPosition[0], map.playerPosition[1]] in map.puntsPositions:
                map.puntsPositions.remove([map.playerPosition[0], map.playerPosition[1]])

            map.map[map.playerPosition[0]][map.playerPosition[1] - 1] = 3

            return True
        
        return False

    def movePlayerRight(self):

        if map.map[map.playerPosition[0]][map.playerPosition[1] + 1] in (0, 2) or map.map[map.playerPosition[0]][map.playerPosition[1] + 1] >= 4:
            map.map[map.playerPosition[0]][map.playerPosition[1]] = 0
            
            if [map.playerPosition[0], map.playerPosition[1]] in map.puntsPositions:
                map.puntsPositions.remove([map.playerPosition[0], map.playerPosition[1]])

            map.map[map.playerPosition[0]][map.playerPosition[1] + 1] = 3

            return True
        
        return False

    #Final message
    def final(self, message, ghosts):

        messageRectWidth = self.screen.get_width() / 2.75
        messageRectHeight = self.screen.get_height() / 5

        messageRectX = self.screen.get_width() / 2 - map.tileWidth - messageRectWidth / 4.6
        messageRectY = self.screen.get_height() / 2 - map.tileHeight

        messageRect = pygame.Rect((messageRectX, messageRectY), (messageRectWidth, messageRectHeight))
        
        pygame.draw.rect(self.screen, "snow", messageRect, 0, 10)
        pygame.draw.rect(self.screen, "black", messageRect, 10, 10)
        pygame.draw.rect(self.screen, "dimgrey", messageRect, 1, 10)


        messageFontX = messageRectX + messageRectWidth / 7
        messageFontY = messageRectY + messageRectHeight / 2.75

        self.screen.blit(message, (messageFontX, messageFontY))

        self.image = pygame.transform.scale(self.image, (1, 1))
        
        for i in ghosts:
            i.image = pygame.transform.scale(self.image, (1, 1))

        return True