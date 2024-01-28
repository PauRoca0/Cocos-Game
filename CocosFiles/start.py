import pygame

#Create start class
class Start:
    def __init__(self, screen, startTitle, startMessage):
        self.screen = screen

        self.image = pygame.image.load("assets/pacmanPng.png").convert()
        self.image = pygame.transform.scale(self.image, (self.screen.get_width() / 2, self.screen.get_height() / 2))
        self.image.set_colorkey((0, 0, 0))

        self.startTitle = startTitle
        self.startMessage = startMessage

        #All the start message timing
        self.showStartMessage = True
        self.startMessageTime = 500

        self.PRESSTIME = pygame.USEREVENT + 3
        pygame.time.set_timer(self.PRESSTIME, self.startMessageTime)

    #Display images and texts
    def displayScreen(self):
    
        self.titleX = self.screen.get_width() / 5
        self.titleY = self.screen.get_height() / 8
        self.screen.blit(self.startTitle, (self.titleX, self.titleY))

        if self.showStartMessage:
            self.messageX = self.screen.get_width() / 4
            self.messageY = self.screen.get_height() / 1.25
            self.screen.blit(self.startMessage, (self.messageX, self.messageY))
        
        self.imageX = self.screen.get_width() / 4
        self.imageY = self.screen.get_height() / 4
        self.screen.blit(self.image, (self.imageX, self.imageY))

    #Start message timing
    def startMessageTiming(self, event):
        if event.type == self.PRESSTIME:
            if self.showStartMessage:
                self.showStartMessage = False
                pygame.time.set_timer(self.PRESSTIME, self.startMessageTime)
            else:
                self.showStartMessage = True
                pygame.time.set_timer(self.PRESSTIME, self.startMessageTime)