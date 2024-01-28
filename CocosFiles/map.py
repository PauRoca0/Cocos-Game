import pygame
import levels

#Creates a empty map taking as parameters the number of rows and columns
def mapCreation(nRow, nColumn):
    global map

    map = []

    for row in range(nRow):
        map.append([])

        for column in range(nColumn):
            if row == 0 or row == nRow - 1 or column == 0 or column == nColumn - 1:
                map[row].append(1)

            else:
                map[row].append(2)
    
    return map

#All the automatic creation stuff (function above creates the map)
def automaticMapCreation(numberRows, numberColumns):
    global map, nRow, nColumn, playerPosition, ghostPosition, ghostPosition2

    nRow = numberRows
    nColumn = numberColumns

    map = mapCreation(nRow, nColumn)

    playerPosition = [nRow // 2, nColumn // 2]
    map[playerPosition[0]][playerPosition[1]] = 3

    ghostPosition = [1, 1]
    map[ghostPosition[0]][ghostPosition[1]] = 4

    ghostPosition2 = [nRow - 2, nColumn - 2]
    map[ghostPosition2[0]][ghostPosition2[1]] = 5

#Create the map using a precreated map
def manualMapCreation(level):
    global map, nRow, nColumn, playerPosition, ghostPosition, ghostPosition2

    if level == 1:
        map = levels.level1
    
    elif level == 2:
        map = levels.level2
    
    elif level == 3:
        map = levels.level3
    
    nRow = len(map)
    nColumn = len(map[0])

    for row in range(nRow):
        for column in range(nColumn):

            if map[row][column] == 3:
                playerPosition = [row, column]
            
            elif map[row][column] == 4:
                ghostPosition = [row, column]
            
            elif map[row][column] == 5:
                ghostPosition2 = [row, column]

map = []

playerPosition = [0, 0]
ghostPosition = [0, 0]
ghostPosition2 = [0, 0]

nRow = 0
nColumn = 0

puntsPositions = []

#Map drawing
def drawMap(screen):
    global map, tileHeight, tileWidth, playerPosition, ghostPosition, ghostPosition2, puntsPositions, nRow, nColumn

    tileWidth = screen.get_width() / nColumn
    tileHeight = screen.get_height() / nRow

    for row in range(len(map)):
        for column in range(len(map[row])):

            if map[row][column] == 1:
                pygame.draw.rect(screen, "blue", (tileWidth * column, tileHeight * row, tileWidth, tileHeight), 5)

            elif map[row][column] == 3:
                playerPosition = [row, column]
            
            elif map[row][column] == 4:
                ghostPosition = [row, column]
            
            elif map[row][column] == 5:
                ghostPosition2 = [row, column]
            
            if map[row][column] == 2:
                pygame.draw.circle(screen, "yellow", (tileWidth * column + tileWidth / 2, tileHeight * row + tileHeight / 2), 5)

                if [row, column] not in puntsPositions:
                    puntsPositions.append([row, column])
