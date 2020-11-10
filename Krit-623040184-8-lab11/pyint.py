try:
   import pygame as pg
   from tkinter import *
   from tkinter import messagebox
   from tkinter import colorchooser
   from tkinter.filedialog import askopenfilename, asksaveasfilename
except:
   import install_requirements
   import pygame as pg
   from tkinter import *
   from tkinter import messagebox
   from tkinter.filedialog import askopenfilename, asksaveasfilename
import sys


sys.setrecursionlimit(100)
pg.init()

sw, sh = 800, 650
sc = (sw//2, sh//2)
screen = pg.display.set_mode((sw, sh))
pg.display.set_caption("Pixel Paint")
pg.display.set_icon(pg.image.load("data/Pd2.png"))

brushImage = pg.transform.scale(pg.image.load("data/brush.png"), (25,25))
eraserImage = pg.transform.scale(pg.image.load("data/eraser.png"), (25,25))


def Remap(oldlow, oldhigh, newlow, newhigh, value):
    oldRange = (oldhigh - oldlow)
    newRange = (newhigh - newlow)
    newVal = (((value - oldlow) * newRange) / oldRange) + newlow
    return newVal


def draw_walls():
    wall_color = (250,0,0)
    wall_thickness = 4

    pg.draw.rect(screen, (105,105,105), (g1.xCount * g1.cellSize, 0, sw - g1.xCount * g1.cellSize, g1.yCount*g1.cellSize))#color bourd tools size
    pg.draw.rect(screen, (110, 110, 110), (0, g1.xCount * g1.cellSize, sw, sh-g1.yCount*g1.cellSize))#color bourd lord save

    pg.draw.rect(screen, (0,250,250), (g1.xCount * g1.cellSize, 0, wall_thickness, g1.yCount*g1.cellSize))
    pg.draw.rect(screen, (250,250,0), (0, 0, sw, wall_thickness))

    pg.draw.rect(screen, (250,0,250), (0, 0, sw, wall_thickness))
    pg.draw.rect(screen, (0,0,250), (sw-wall_thickness, 0, wall_thickness, sh))
    pg.draw.rect(screen, (0,250,0), (0, 0, wall_thickness, sh))



class Cell(object):

    def __init__(self, size, color=[0, 0, 0]):
        self.size = size
        self.color = color
        self.subsurface = pg.Surface((self.size, self.size))
        self.subsurface.fill(self.color)
        self.pos = (0, 0)

    def change_color(self, color):
        self.color = color
        self.subsurface.fill(self.color)

    def Draw(self, win, x, y):
        self.pos = (x, y)
        win.blit(self.subsurface, self.pos)

    def morec(self):
        color = colorchooser.askcolor(parent=Tk())
        color.configure(bg=color[1])
        color.pack()
        return list(color[0])

class Grid(object):
    def __init__(self, xc, yc, csize, x, y, color=[255, 255, 255]):
        self.xCount = xc
        self.yCount = yc
        self.cellSize = csize
        self.pos = (x, y)
        self.color = color
        self.grid = []
        self.undoList = [[], []]

        for i in range(self.xCount):
            self.grid.append([])
            self.undoList[0].append([])
            self.undoList[1].append([])
            for j in range(self.yCount):
                self.grid[i].append(Cell(self.cellSize, self.color))
                self.undoList[0][i].append(self.color)
                self.undoList[1][i].append(self.color)

    def Draw(self, win):
        for i in range(self.xCount):
            for j in range(self.yCount):
                self.grid[i][j].Draw(win, self.pos[0]+(self.cellSize*i), self.pos[1]+(self.cellSize*j))

    def change_color(self, posx, posy, color):
        self.grid[posy][posx].change_color(color)

    def clean(self):
        for i in range(self.xCount):
            for j in range(self.yCount):
                self.grid[i][j].change_color(self.color)



class Button(object):
    active = False
    clicked = False
    rollOver = False

    def __init__(self, posX, posY, width, height, color, text="Button", type=1, fontSize=25, fontColor=(255, 255, 255)):
        self.pos = [posX, posY]
        self.drawPos = self.pos.copy()
        self.width, self.height = width, height
        self.color = color
        self.text, self.fontSize, self.fontColor = text, fontSize, fontColor
        self.type = type
        self.subsurface = pg.Surface((self.width, self.height))
        self.subsurface.fill(self.color)
        self.font = pg.font.SysFont(None, self.fontSize)
        self.mes = self.font.render(self.text, True, self.fontColor)
        self.slideVal = 0

    def Draw(self, win, val=-1):
        if self.type == 1:
            if self.rollOver and not self.clicked:
                self.subsurface.set_alpha(100)
            else:
                self.subsurface.set_alpha(150)

            if self.clicked:
                self.subsurface.set_alpha(255)

            win.blit(self.subsurface, self.pos)
            self.subsurface.blit(self.mes, (15, self.height/3))
        elif self.type == 2:
            self.slideVal = Remap(-60, 40, 1, 5, (self.pos[0] - self.drawPos[0]))
            pg.draw.rect(screen, (128, 128, 128), (self.drawPos[0]-90, self.drawPos[1]-30, 120, 60))
            pg.draw.rect(screen, (220, 220, 220), (self.drawPos[0]-50, self.drawPos[1]+self.height/3, 60, self.height/2))
            pg.draw.rect(screen, (220, 220, 220), (self.drawPos[0]-80, self.drawPos[1]+1, 20, 20))
            self.valMes = self.font.render(str(val), True, (30, 30, 30))
            win.blit(self.valMes, (self.drawPos[0]-75, self.drawPos[1]+3))
            win.blit(self.subsurface, (self.pos[0]-self.width/2, self.pos[1]))
            win.blit(self.mes, (self.drawPos[0]-90, self.drawPos[1]-25))

colors1 = [
    [0, 0, 0], [24,24,24], [48,48,48], [64,64,64], [128,128,128],[155,155,155],[200,200,200],[255,255,255],
    [27,38,49],[40,55,71],[46,64,83],[52,73,94],[93,109,126],[133,146,158],[174,182,191],[214,219,223],
    [77,86,86],[95,106,106],[113,125,126],[149,165,166],[170,183,184],[191,201,202],[213,219,219],[229,232,232],
    [98,101,103],[121,125,127],[144,148,151],[189,195,199],[202,207,210],[229,231,233],[248,249,249],[255,255,255],
    [100,30,22],[123,36,28],[146,43,33],[192,57,43],[205,97,85],[217,136,128],[230,176,170],[242,215,213],
    [120,40,31],[148,49,38],[176,58,46],[220,76,60],[236,112,99],[241,148,138],[245,183,177],[250,219,216],
    [74,35,90],[91,44,111],[108,52,131],[142,68,173],[165,105,189],[187,143,206],[210,180,222],[232,218,239],
    [21,67,96],[26,82,118],[31,97,141],[41,128,185],[84,153,199],[127,179,213],[169,204,227],[212,230,241],
    [20,90,50],[25,111,61],[34,141,84],[34,174,96],[82,190,128],[125,206,160],[169,223,191],[212,239,223],
    ]

colors2 = [
    [125,102,8],[154,125,10],[183,149,11],[230,196,15],[244,208,63],[247,220,111],[249,231,159],[252,243,207],
    [126,81,9],[156,100,12],[185,119,14],[242,156,18],[245,176,65],[248,196,113],[250,215,160],[253,235,208],
    [110,44,0],[135,54,0],[160,64,0],[211,84,0],[220,118,51],[229,152,102],[237,187,153],[246,221,204],
    [241,157,154],[241,179,164],[246,209,190],[252,225,213],[242,193,173],[241,175,153],
    [128,232,221],[124,194,246],[175,129,228],[231,132,186],[249,193,160],[183,246,175],
    [100,93,62],[130,123,92],[156,151,115],[86,113,80],[46,71,43],[16,42,10],
    [252,120,150],[193,107,188],[152,89,197],[108,66,196],[85,56,193],[30,171,215],
    [92,58,42],[121,84,63],[172,138,104],[200,173,139],[223,213,191],[206,159,85]
    ]


colorCells1 = []
colorCells2 = []

for color in colors1:
    colorCells1.append(Cell(20, color))

for color in colors2:
    colorCells2.append(Cell(20, color))



colorTitleFont = pg.font.SysFont(None, 25)
colorTitle = colorTitleFont.render("Color Palette", True, (50, 50, 50))#--------------------------------------------------------------------------------------------------------------------

colorScheme = 1
"""
colorFont = pg.font.SysFont(None, 22)
colorTexts = [colorFont.render("Skin", True, (50, 50, 50)), colorFont.render("Soft Hues", True, (50, 50, 50)),#------------------------------------------------------------------------------------------------------
              colorFont.render("Forest", True, (50, 50, 50)), colorFont.render("Sunset", True, (50, 50, 50)),
              colorFont.render("Coffee", True, (50, 50, 50))]
"""

g1 = Grid(50, 50, 12, 0, 0, [255, 255, 255])
"""#------------------------------------------------------------------------------------------------------
save_b = Button(20, 590, 80, 40, (100, 100, 100), "Save", 1, 24, (255, 255, 255))
load_b = Button(110, 590, 80, 40, (100, 100, 100), "Load", 1, 24, (255, 255, 255))
export_b = Button(200, 590, 80, 40, (100, 100, 100), "Export", 1, 24, (255, 255, 255))
SL_Buttons = [save_b, load_b, export_b]
"""
S_brushSize = Button(700, 305, 10, 20, (240, 240, 240), " Brush Size", 2)
S_eraserSize = Button(700, 225, 10, 20, (240, 240, 240), " Eraser Size", 2)
S_buttons = [S_brushSize, S_eraserSize]

B_penTool = Button(625, 60, 30, 30, (80, 80, 80), "", 1)
B_eraserTool = Button(675, 60, 30, 30, (80, 80, 80), "", 1)

B_Buttons = [B_penTool, B_eraserTool]

P_number1 = Button(720, 380, 15, 15, (80, 80, 80), "")
P_number1.clicked = True
P_number2 = Button(740, 380, 15, 15, (80, 80, 80), "")
P_Buttons = [P_number1, P_number2]

selectedTool = 0
selectedToolBefore = 0

colorUsing = [128, 30, 30]
selectedColor = [0, 0, 0]
clicking = False
penSize = 3
eraserSize = 3

round = -1
clock = pg.time.Clock()
holdingCTRL = False
undoed = False
mouseRelPosX = 0
mouseRelPosY = 0

positions1 = []
positions2 = []

visitedFillPositions = []
i = 0
j = 0
for color in colorCells1:
    positions1.append((615 + i * 20, 405 + j * 25))
    i += 1
    if i >= 8:
        i = 0
        j += 1

i = 0
j = 0
for color in colorCells2:
    positions2.append((615 + i * 20, 405 + j * 25))
    i += 1
    if i >= 8:
        i = 0
        j += 1



def draw_palette(scheme):
    screen.blit(colorTitle, (610, 380))
    pg.draw.rect(screen, (200, 200, 200), (610, 400, 170, 230))

    if scheme == 1:
        for i, color in enumerate(colorCells1):
            screen.blit(color.subsurface, positions1[i])
    elif scheme == 2:
        for i, color in enumerate(colorCells2):
            screen.blit(color.subsurface, positions2[i])

    pg.draw.rect(screen, (235, 235, 235), (positions1[-1][0] - 75, positions1[-1][1] - 265, 35, 35))
    pg.draw.rect(screen, colorUsing, (positions1[-1][0] - 69, positions1[-1][1] - 259, 23, 23))

def paint(var):
    global mouseRelPosX, mouseRelPosY
    if var == 0:
        sizeToDraw = penSize
    elif var == 1:
        sizeToDraw = eraserSize


    if sizeToDraw == 1:
        mouseRelPosX = max(penSize - 3, min(g1.xCount - 1, int(Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pg.mouse.get_pos()[0]))))
        mouseRelPosY = max(penSize - 3, min(g1.yCount - 1, int(Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pg.mouse.get_pos()[1]))))
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)

    if sizeToDraw == 2:
        mouseRelPosX = max(penSize - 1, min(g1.xCount - 2, int(Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pg.mouse.get_pos()[0]))))
        mouseRelPosY = max(penSize - 1, min(g1.yCount - 2, int(Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pg.mouse.get_pos()[1]))))
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX + 1, colorUsing)
    if sizeToDraw == 3:
        mouseRelPosX = max(penSize - 2, min(g1.xCount - 2, int(Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pg.mouse.get_pos()[0]))))
        mouseRelPosY = max(penSize - 2, min(g1.yCount - 2, int(Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pg.mouse.get_pos()[1]))))
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY - 1, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX - 1, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY - 1, mouseRelPosX - 1, colorUsing)
        g1.change_color(mouseRelPosY - 1, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX - 1, colorUsing)


def neighbours(x, y):
    return [[x+1, y],[x-1, y],[x, y+1],[x, y-1]]


def fill(gridObject, posX, posY, colorNow, fillColor):

    if posX < 0 or posY < 0:
        return
    if posX >= gridObject.xCount or posY >= gridObject.yCount:
        return
    if gridObject.grid[posX][posY].color != colorNow:
        return
    if [posX, posY] in visitedFillPositions:
        return

    visitedFillPositions.append([posX, posY])
    gridObject.change_color(posY, posX, fillColor)
    moves = neighbours(posX, posY)
    for move in moves:
        fill(gridObject, move[0], move[1], colorNow, fillColor)


def tool_activate(toolIndex):
    global colorUsing
    if toolIndex == 0:
        colorUsing = selectedColor.copy()
    if toolIndex == 1:
        colorUsing = g1.color.copy()
    if toolIndex == 2:
        colorUsing = selectedColor.copy()
    if toolIndex == 3:
        colorUsing = selectedColor.copy()


def Capture(display, name,pos,size):
    image = pg.Surface(size)
    image.blit(display,(0,0),(pos,size))
    pg.image.save(image,name)


def key_event_up(event):
    global penSize, undoed, holdingCTRL, colorScheme, selectedTool


    if event.key == pg.K_1:
        colorScheme = 1
    elif event.key == pg.K_2:
        colorScheme = 2

    if event.key == pg.K_e:
        selectedTool = 1
        B_Buttons[1].clicked = True
        for subbutton in B_Buttons:
            if B_Buttons.index(subbutton) != selectedTool:
                subbutton.clicked = False
    elif event.key == pg.K_b:
        selectedTool = 0
        B_Buttons[0].clicked = True
        for subbutton in B_Buttons:
            if B_Buttons.index(subbutton) != selectedTool:
                subbutton.clicked = False
    elif event.key == pg.K_g:
        selectedTool = 2
        B_Buttons[2].clicked = True
        for subbutton in B_Buttons:
            if B_Buttons.index(subbutton) != selectedTool:
                subbutton.clicked = False
    elif event.key == pg.K_i:
        selectedTool = 3
        B_Buttons[3].clicked = True
        for subbutton in B_Buttons:
            if B_Buttons.index(subbutton) != selectedTool:
                subbutton.clicked = False

    if event.key == pg.K_LCTRL:
        holdingCTRL = False

    if event.key == pg.K_SPACE:
        if holdingCTRL:
            g1.clean()
            undoed = True


    if event.key == pg.K_z:
        if holdingCTRL:

            for i in range(g1.yCount):
                for j in range(g1.xCount):
                    if round == 1:
                        g1.change_color(j, i, g1.undoList[1][i][j])
                    if round == -1:
                        g1.change_color(j, i, g1.undoList[0][i][j])
            undoed = True


while True:
    clock.tick(240)

    if undoed:
        for i in range(g1.xCount):
            for j in range(g1.yCount):
                    g1.undoList[0][i][j] = g1.grid[i][j].color
                    g1.undoList[1][i][j] = g1.grid[i][j].color
        undoed = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                selectedToolBefore = selectedTool
                selectedTool = 1
            elif event.button == 1:
                if pg.mouse.get_pos()[0] < g1.xCount*g1.cellSize and pg.mouse.get_pos()[1] < g1.yCount*g1.cellSize:
                    if selectedTool == 0 or selectedTool == 1:
                        paint(selectedTool)
                        clicking = True


                    elif selectedTool == 2:
                        mouseRelPosX = max(0, min(g1.xCount - 1, int(Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pg.mouse.get_pos()[0]))))
                        mouseRelPosY = max(0, min(g1.yCount - 1, int(Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pg.mouse.get_pos()[1]))))

                        visitedFillPositions.clear()

                        fill(g1, mouseRelPosX, mouseRelPosY, g1.grid[mouseRelPosX][mouseRelPosY].color, selectedColor)

                    elif selectedTool == 3:
                        mouseRelPosX = max(0, min(g1.xCount - 1, int(Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pg.mouse.get_pos()[0]))))
                        mouseRelPosY = max(0, min(g1.yCount - 1, int(Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pg.mouse.get_pos()[1]))))

                        selectedColor = g1.grid[mouseRelPosX][mouseRelPosY].color

                else:

                    if colorScheme == 1:
                        for i, Scolor in enumerate(colorCells1):
                            if Scolor.subsurface.get_rect(topleft=positions1[i]).collidepoint(pg.mouse.get_pos()):
                                selectedColor = Scolor.color
                    elif colorScheme == 2:
                        for i, Scolor in enumerate(colorCells2):
                            if Scolor.subsurface.get_rect(topleft=positions2[i]).collidepoint(pg.mouse.get_pos()):
                                selectedColor = Scolor.color

                    for but in S_buttons:
                        if but.subsurface.get_rect(topleft=(but.pos[0]-but.width/2, but.pos[1])).collidepoint(pg.mouse.get_pos()):
                            but.active = True
                        else:
                            but.active = False

                    for but in B_Buttons:
                        if but.rollOver:
                            but.clicked = True
                            selectedTool = B_Buttons.index(but)
                            for subbutton in B_Buttons:
                                if B_Buttons.index(subbutton) != selectedTool:
                                    subbutton.clicked = False

                    for but in P_Buttons:
                        if but.rollOver:
                            but.clicked = True
                            colorScheme = P_Buttons.index(but)+1
                            for subbutton in P_Buttons:
                                if P_Buttons.index(subbutton) != selectedTool:
                                    subbutton.clicked = False

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                selectedTool = selectedToolBefore
            elif event.button == 1:
                for i in range(g1.xCount):
                    for j in range(g1.yCount):
                        if round == -1:
                            g1.undoList[0][i][j] = g1.grid[i][j].color
                        if round == 1:
                            g1.undoList[1][i][j] = g1.grid[i][j].color
                round *= -1
                clicking = False

                for but in S_buttons:
                    but.active = False

        if event.type == pg.MOUSEMOTION:
            if pg.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pg.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
                pg.mouse.set_visible(False)
            else:
                pass
                pg.mouse.set_visible(True)
            if clicking:
                if pg.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pg.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
                    paint(selectedTool)
            else:
                for but in B_Buttons:
                    if but.subsurface.get_rect(topleft=but.pos).collidepoint(pg.mouse.get_pos()):
                        but.rollOver = True
                    else:
                        but.rollOver = False
                for but in S_buttons:
                    if but.active:
                        but.pos[0] = max(but.drawPos[0]-50, min(pg.mouse.get_pos()[0], but.drawPos[0]+10))
                    else:
                        but.active = False

                for but in P_Buttons:
                    if but.subsurface.get_rect(topleft=but.pos).collidepoint(pg.mouse.get_pos()):
                        but.rollOver = True
                    else:
                        but.rollOver = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LCTRL:
                holdingCTRL = True

        if event.type == pg.KEYUP:
            key_event_up(event)

    tool_activate(selectedTool)

    screen.fill((255, 255, 255))
    g1.Draw(screen)
    draw_walls()

    screen.blit(colorTitleFont.render(" Tools", True, (250, 250, 250)), (610, 30))
    pg.draw.rect(screen, (128, 128, 128), (610, 50, 140, 50))
    for but in B_Buttons:
        but.Draw(screen)

    for but in P_Buttons:
        but.Draw(screen)

    screen.blit(colorTitleFont.render("Size Settings", True, (50, 50, 50)), (610, 170))
    S_brushSize.Draw(screen, penSize)
    S_eraserSize.Draw(screen, eraserSize)
    penSize = int(S_brushSize.slideVal)
    eraserSize = int(S_eraserSize.slideVal)

    screen.blit(pg.transform.scale(eraserImage, (22, 22)), (B_eraserTool.pos[0]+3, B_eraserTool.pos[1]+2))
    screen.blit(pg.transform.scale(brushImage, (22, 22)), (B_penTool.pos[0]+3, B_penTool.pos[1]+2))

    draw_palette(colorScheme)
    if selectedTool == 0:
        if pg.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pg.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
            pg.draw.circle(screen, colorUsing, (pg.mouse.get_pos()), penSize * 8, 1)
    elif selectedTool == 1:
        if pg.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pg.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
            pg.draw.circle(screen, (50,50,50), (pg.mouse.get_pos()), eraserSize * 8, 1)

    pg.display.update()
