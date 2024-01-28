import pygame

#Create menu class
class Menu:
    def __init__(self, screen, button1message, button2message, menuTitle):
        self.screen = screen

        self.button1message = button1message
        self.button2message = button2message
        self.menuTitle = menuTitle

        self.buttonWidth = 200
        self.buttonHeight = 100

        self.button1x = self.screen.get_width() / 2 - self.buttonWidth / 2
        self.button1y = 200

        self.button2x = self.screen.get_width() / 2 - self.buttonWidth / 2
        self.button2y = 350

        self.button1 = pygame.Rect((self.button1x, self.button1y), (self.buttonWidth, self.buttonHeight))
        self.button2 = pygame.Rect((self.button2x, self.button2y), (self.buttonWidth, self.buttonHeight))

        self.buttonSelected = 1

        self.n = 10

        self.level = 1

    #Display all the buttons and texts (and selector)
    def displayOptions(self):
        titleX = self.screen.get_width() / 25
        titleY = self.screen.get_height() / 6

        self.screen.blit(self.menuTitle, (titleX, titleY))

        pygame.draw.rect(self.screen, "gray", self.button1, 0, 15)
        pygame.draw.rect(self.screen, "dimgray", self.button1, 10, 15)
        self.screen.blit(self.button1message, (self.button1x + self.buttonWidth / 7.5, self.button1y + self.buttonHeight / 2.75))

        pygame.draw.rect(self.screen, "gray", self.button2, 0, 15)
        pygame.draw.rect(self.screen, "dimgray", self.button2, 10, 15)
        self.screen.blit(self.button2message, (self.button2x + self.buttonWidth / 4.5, self.button2y + self.buttonHeight / 2.75))

        if self.buttonSelected == 1:
            pygame.draw.rect(self.screen, "black", self.button1, 5, 15)

        elif self.buttonSelected == 2:
            pygame.draw.rect(self.screen, "black", self.button2, 5, 15)

    #Selection controls
    def menuSelection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.buttonSelected = 1
            
            if event.key == pygame.K_DOWN:
                self.buttonSelected = 2

            if event.key == pygame.K_RETURN:
                if self.buttonSelected == 1:
                    return "a"

                elif self.buttonSelected == 2:
                    return "m"     
    
    #Display all the map size menu things
    def mapSizeDisplay(self, rowORcolumn, text, font):
        if rowORcolumn == "row":
            rowTitleX = self.screen.get_width() / 17
            rowTitleY = self.screen.get_height() / 6

            self.screen.blit(text, (rowTitleX, rowTitleY))
        
        elif rowORcolumn == "column":
            columnTitleX = self.screen.get_width() / 17
            columnTitleY = self.screen.get_height() / 6

            self.screen.blit(text, (columnTitleX, columnTitleY))
        

        number = font.render(str(self.n), False, "black")
        
        numberX = self.screen.get_width() / 2
        numberY = self.screen.get_height() / 2

        self.screen.blit(number, (numberX, numberY))

    #Controls in the map selection menu
    def mapSizeSelection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.n >= 20:
                    self.n = 20

                else:
                    self.n += 1
            
            if event.key == pygame.K_DOWN:
                if self.n <= 7:
                    self.n = 7
                
                else:
                    self.n -= 1
            
            if event.key == pygame.K_RETURN:
                return self.n
            
    #Displays map level menu
    def mapLevelDisplay(self, text, font):
        titleX = self.screen.get_width() / 3
        titleY = self.screen.get_height() / 5

        number = font.render(str(self.level), False, "black")
        
        numberX = self.screen.get_width() / 2
        numberY = self.screen.get_height() / 2

        self.screen.blit(number, (numberX, numberY))

        self.screen.blit(text, (titleX, titleY)) 

    #Controls in the map selector
    def mapLevelSelection(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if self.level == 3:
                    self.level = 3
                
                else:
                    self.level += 1
            
            if event.key == pygame.K_LEFT:
                if self.level == 1:
                    self.levet = 1
                
                else:
                    self.level -= 1
            
            if event.key == pygame.K_RETURN:
                return self.level
