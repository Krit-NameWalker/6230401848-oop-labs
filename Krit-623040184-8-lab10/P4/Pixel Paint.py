from tkinter import *
import pygame

sys.setrecursionlimit(100)
pygame.init()

sw, sh = 760, 600
sc = (sw // 2, sh // 2)
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Pixel Paint")
pygame.display.set_icon(pygame.image.load("data/Pd2.png"))

brushImage = pygame.transform.scale(pygame.image.load("data/brush.png"), (25, 25))
eraserImage = pygame.transform.scale(pygame.image.load("data/eraser.png"), (25, 25))

def Remap(oldlow, oldhigh, newlow, newhigh, value):
    oldRange = (oldhigh - oldlow)
    newRange = (newhigh - newlow)
    newVal = (((value - oldlow) * newRange) / oldRange) + newlow
    return newVal


def draw_walls():

    wall_thickness = 4
    pygame.draw.rect(screen, (105, 105, 105), (
    g1.xCount * g1.cellSize, 0, sw - g1.xCount * g1.cellSize, g1.yCount * g1.cellSize))  # color bourd tools size

    pygame.draw.rect(screen, (0, 250, 250), (g1.xCount * g1.cellSize, 0, wall_thickness, g1.yCount * g1.cellSize))
    pygame.draw.rect(screen, (250, 250, 0), (0, g1.yCount * g1.cellSize - wall_thickness, sw, wall_thickness))

    pygame.draw.rect(screen, (250, 0, 250), (0, 0, sw, wall_thickness))
    pygame.draw.rect(screen, (0, 0, 250), (sw - wall_thickness, 0, wall_thickness, sh))
    pygame.draw.rect(screen, (0, 250, 0), (0, 0, wall_thickness, sh))

class Cell(object):

    def __init__(self, size, color=[0, 0, 0]):
        self.size = size
        self.color = color
        self.subsurface = pygame.Surface((self.size, self.size))
        self.subsurface.fill(self.color)
        self.pos = (0, 0)

    def change_color(self, color):
        self.color = color
        self.subsurface.fill(self.color)

    def Draw(self, win, x, y):
        self.pos = (x, y)
        win.blit(self.subsurface, self.pos)


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
                self.grid[i][j].Draw(win, self.pos[0] + (self.cellSize * i), self.pos[1] + (self.cellSize * j))

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
        self.subsurface = pygame.Surface((self.width, self.height))
        self.subsurface.fill(self.color)
        self.font = pygame.font.SysFont(None, self.fontSize)
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
            self.subsurface.blit(self.mes, (15, self.height / 3))
        elif self.type == 2:
            self.slideVal = Remap(-60, 40, 1, 5, (self.pos[0] - self.drawPos[0]))
            pygame.draw.rect(screen, (128, 128, 128), (self.drawPos[0] - 90, self.drawPos[1] - 30, 120, 60))
            pygame.draw.rect(screen, (220, 220, 220),
                             (self.drawPos[0] - 50, self.drawPos[1] + self.height / 3, 60, self.height / 2))
            pygame.draw.rect(screen, (220, 220, 220), (self.drawPos[0] - 80, self.drawPos[1] + 1, 20, 20))
            self.valMes = self.font.render(str(val), True, (30, 30, 30))
            win.blit(self.valMes, (self.drawPos[0] - 75, self.drawPos[1] + 3))
            win.blit(self.subsurface, (self.pos[0] - self.width / 2, self.pos[1]))
            win.blit(self.mes, (self.drawPos[0] - 90, self.drawPos[1] - 25))

colorTitleFont = pygame.font.SysFont(None, 25)

g1 = Grid(50, 50, 12, 0, 0, [255, 255,255])

S_brushSize = Button(700, 305, 10, 20, (240, 240, 240), " Brush Size", 2)
S_eraserSize = Button(700, 225, 10, 20, (240, 240, 240), " Eraser Size", 2)
S_buttons = [S_brushSize, S_eraserSize]

B_penTool = Button(625, 60, 30, 30, (80, 80, 80), "", 1)
B_eraserTool = Button(675, 60, 30, 30, (80, 80, 80), "", 1)

B_Buttons = [B_penTool, B_eraserTool]

fileFont = pygame.font.SysFont(None, 30)

selectedTool = 0
selectedToolBefore = 0

colorUsing = [128, 30, 30]
selectedColor = [0, 0, 0]
clicking = False
penSize = 3
eraserSize = 3

round = -1
clock = pygame.time.Clock()
holdingCTRL = False
undoed = False
mouseRelPosX = 0
mouseRelPosY = 0

positions1 = []
positions2 = []

def paint(var):
    global mouseRelPosX, mouseRelPosY
    if var == 0:
        sizeToDraw = penSize
    elif var == 1:
        sizeToDraw = eraserSize

    if sizeToDraw == 1:
        mouseRelPosX = max(penSize - 3, min(g1.xCount - 1, int(
            Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pygame.mouse.get_pos()[0]))))
        mouseRelPosY = max(penSize - 3, min(g1.yCount - 1, int(
            Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pygame.mouse.get_pos()[1]))))
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)

    if sizeToDraw == 2:
        mouseRelPosX = max(penSize - 1, min(g1.xCount - 2, int(
            Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pygame.mouse.get_pos()[0]))))
        mouseRelPosY = max(penSize - 1, min(g1.yCount - 2, int(
            Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pygame.mouse.get_pos()[1]))))
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX + 1, colorUsing)
    if sizeToDraw == 3:
        mouseRelPosX = max(penSize - 2, min(g1.xCount - 2, int(
            Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pygame.mouse.get_pos()[0]))))
        mouseRelPosY = max(penSize - 2, min(g1.yCount - 2, int(
            Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pygame.mouse.get_pos()[1]))))
        g1.change_color(mouseRelPosY, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY - 1, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX - 1, colorUsing)
        g1.change_color(mouseRelPosY, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY - 1, mouseRelPosX - 1, colorUsing)
        g1.change_color(mouseRelPosY - 1, mouseRelPosX + 1, colorUsing)
        g1.change_color(mouseRelPosY + 1, mouseRelPosX - 1, colorUsing)

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

def key_event_up(event):
    global penSize, undoed, holdingCTRL, colorScheme, selectedTool

    if event.key == pygame.K_1:
        colorScheme = 1
    elif event.key == pygame.K_2:
        colorScheme = 2

    if event.key == pygame.K_e:
        selectedTool = 1
        B_Buttons[1].clicked = True
        for subbutton in B_Buttons:
            if B_Buttons.index(subbutton) != selectedTool:
                subbutton.clicked = False
    elif event.key == pygame.K_b:
        selectedTool = 0
        B_Buttons[0].clicked = True
        for subbutton in B_Buttons:
            if B_Buttons.index(subbutton) != selectedTool:
                subbutton.clicked = False

    if event.key == pygame.K_LCTRL:
        holdingCTRL = False

    if event.key == pygame.K_SPACE:
        if holdingCTRL:
            g1.clean()
            undoed = True

    if event.key == pygame.K_z:
        if holdingCTRL:

            for i in range(g1.yCount):
                for j in range(g1.xCount):
                    if round == 1:
                        g1.change_color(j, i, g1.undoList[1][i][j])
                    if round == -1:
                        g1.change_color(j, i, g1.undoList[0][i][j])
            undoed = True

A = True
while A:
    clock.tick(240)

    if undoed:
        for i in range(g1.xCount):
            for j in range(g1.yCount):
                g1.undoList[0][i][j] = g1.grid[i][j].color
                g1.undoList[1][i][j] = g1.grid[i][j].color
        undoed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                selectedToolBefore = selectedTool
                selectedTool = 1
            elif event.button == 1:
                if pygame.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pygame.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
                    if selectedTool == 0 or selectedTool == 1:
                        paint(selectedTool)
                        clicking = True

                    elif selectedTool == 3:
                        mouseRelPosX = max(0, min(g1.xCount - 1, int(
                            Remap(0, (g1.cellSize * g1.xCount), 0, g1.xCount, pygame.mouse.get_pos()[0]))))
                        mouseRelPosY = max(0, min(g1.yCount - 1, int(
                            Remap(0, (g1.cellSize * g1.yCount), 0, g1.yCount, pygame.mouse.get_pos()[1]))))

                        selectedColor = g1.grid[mouseRelPosX][mouseRelPosY].color

                else:

                    for but in S_buttons:
                        if but.subsurface.get_rect(topleft=(but.pos[0] - but.width / 2, but.pos[1])).collidepoint(
                                pygame.mouse.get_pos()):
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

        if event.type == pygame.MOUSEBUTTONUP:
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

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pygame.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
                pygame.mouse.set_visible(False)
            else:
                pass
                pygame.mouse.set_visible(True)
            if clicking:
                if pygame.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pygame.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
                    paint(selectedTool)
            else:

                for but in B_Buttons:
                    if but.subsurface.get_rect(topleft=but.pos).collidepoint(pygame.mouse.get_pos()):
                        but.rollOver = True
                    else:
                        but.rollOver = False
                for but in S_buttons:
                    if but.active:
                        but.pos[0] = max(but.drawPos[0] - 50, min(pygame.mouse.get_pos()[0], but.drawPos[0] + 10))
                    else:
                        but.active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                holdingCTRL = True

        if event.type == pygame.KEYUP:
            key_event_up(event)

    tool_activate(selectedTool)

    screen.fill((255, 255, 255))
    g1.Draw(screen)
    draw_walls()

    screen.blit(colorTitleFont.render(" Tools", True, (250, 250, 250)),(610, 30))
    pygame.draw.rect(screen, (128, 128, 128), (610, 50, 140, 50))
    for but in B_Buttons:
        but.Draw(screen)

    S_brushSize.Draw(screen, penSize)
    S_eraserSize.Draw(screen, eraserSize)
    penSize = int(S_brushSize.slideVal)
    eraserSize = int(S_eraserSize.slideVal)

    screen.blit(pygame.transform.scale(eraserImage, (22, 22)), (B_eraserTool.pos[0] + 3, B_eraserTool.pos[1] + 2))
    screen.blit(pygame.transform.scale(brushImage, (22, 22)), (B_penTool.pos[0] + 3, B_penTool.pos[1] + 2))

    if selectedTool == 0:
        if pygame.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pygame.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
            pygame.draw.circle(screen, colorUsing, (pygame.mouse.get_pos()), penSize * 8, 1)
    elif selectedTool == 1:
        if pygame.mouse.get_pos()[0] < g1.xCount * g1.cellSize and pygame.mouse.get_pos()[1] < g1.yCount * g1.cellSize:
            pygame.draw.circle(screen, (50, 50, 50), (pygame.mouse.get_pos()), eraserSize * 8, 1)
    else:
        A = False
    pygame.display.update()
