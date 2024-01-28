#Import librarys
import pygame, time
#Import files
import player, map, ghost, menu, start

#Initialze library and fonts
pygame.init()
pygame.font.init()

#Screen resolution
width = 500
height = 500

#Create screen and clock (later set frames)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Create fonts
font = pygame.font.SysFont("Consola", 40)
titleFont = pygame.font.SysFont("Consola", 60)

#All messages
winMessage = font.render("You Won!", False, "yellow")
loseMessage = font.render("You Lost!", False, "purple")

button1message = font.render("Automatic", False, "black")
button2message = font.render("Manual", False, "black")
menuTitle = titleFont.render("CHOOSE TYPE OF MAP", False, "black")

rowText = titleFont.render("NUMBER OF ROWS", False, "black")
columnText = titleFont.render("NUMBER OF COLUMNS", False, "black")

levelText = titleFont.render("LEVEL", False, "black")

startTitle = titleFont.render("COCOS GAME", False, "goldenrod")
startMessage = font.render("Press enter to start", False, "orangered")

#Create start and menu variables and set its classes into a variable
startScreen = True
Start = start.Start(screen, startTitle, startMessage)

menuScreen = False
Menu = menu.Menu(screen, button1message, button2message, menuTitle)

#Set some booleans
mapType = None
nRow = None
nColumn = None
level = None

finalPause = False
gameActive = True

firstRun = True

while gameActive:
    #Start screen
    if startScreen:
        screen.fill("navy")

        Start.displayScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    startScreen = False
                    menuScreen = True
            
            Start.startMessageTiming(event)
    #Menu screen
    elif menuScreen:
        screen.fill("lightgray")

        if mapType == None:
            Menu.displayOptions()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False

                mapType = Menu.menuSelection(event)
        #Automatic map
        elif mapType == "a":
            rowORcolumn = None

            if nRow == None:
                rowORcolumn = "row"
                text = rowText
            
            elif nColumn == None:
                rowORcolumn = "column"
                text = columnText

            Menu.mapSizeDisplay(rowORcolumn, text, font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                
                if nRow == None:
                    nRow = Menu.mapSizeSelection(event)

                elif nColumn == None:
                    nColumn = Menu.mapSizeSelection(event)

                else:
                    menuScreen = False
        #Manual map
        elif mapType == "m":
            Menu.mapLevelDisplay(levelText, font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False

                if level == None:
                    level = Menu.mapLevelSelection(event)

                else:
                    menuScreen = False

    #Game
    else:
        #First time game is running
        if firstRun:
            #Create map
            if mapType == "a":
                map.automaticMapCreation(nRow, nColumn)
            
            elif mapType == "m":
                map.manualMapCreation(level)

            #Set all classes and add it into sprite group
            allSprites = pygame.sprite.Group()

            pacMan = player.Player(screen, allSprites, map.nRow, map.nColumn)

            ghost1 = ghost.Ghost(screen, allSprites, 1, map.nRow, map.nColumn)
            ghost2 = ghost.Ghost(screen, allSprites, 2, map.nRow, map.nColumn)

            ghosts = [ghost1, ghost2]

            playerSprite = pygame.sprite.Group()
            playerSprite.add(pacMan)

            ghostSprites = pygame.sprite.Group()

            for i in ghosts:
                playerSprite.add(i)
            
            firstRun = False
        
        screen.fill("black")

        #Pause before the end
        if finalPause:
            time.sleep(1)

            gameActive = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False

            #Characters movements
            ghost1.ghostMovementTiming(event)
            ghost2.ghostMovementTiming(event)

            pacMan.playerMovement(event)

        screen.fill("black")

        #Draw map
        map.drawMap(screen)

        #Check if game has ended (lose if you get touched by a ghost, and win if you take all the points)
        if map.playerPosition in (map.ghostPosition, map.ghostPosition2):
            finalPause = pacMan.final(loseMessage, ghosts)

        if len(map.puntsPositions) == 1:
            finalPause = pacMan.final(winMessage, ghosts)
            
        #Draw sprites
        allSprites.draw(screen)

    #Update screen
    pygame.display.flip()

    #Set 60 frames
    clock.tick(60)

#Quit app
pygame.quit()