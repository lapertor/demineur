import random
class Case:
    '''
    Cette classe contient 4 attributs : 
        - mined     : booléen indiquant si la case contient une mine ou non
        - flagged   : booléen indiquant si la case est flaggée ou non
        - showed    : booléen indiquand si la case est dévoilée ou non
        - neighboor : int donnant le nombre de mines voisines à la case courante
    '''
    def __init__(self, mined, neighboor):          
        self.mined = mined
        self.flagged = False
        self.showed = False
        if mined:
            self.neighboor = 0
        else:
            self.neighboor = neighboor
        

        

class Demineur:
    '''
    Cette classe contient 2 attributs :
        - finish    : booléen indiquant si la partie est finie
        - level     : int indiquant le niveau du démineur (débutant, intermédiaire, expert)
        - playground: tableau à 2 dimensions de cases où se passe le jeu
    '''
    def __init__(self, level):
        self.finish = False
        self.level = level
        self.playground = create_playground(level) 
        

def create_playground(level):
    coord_mines = []
    playground = list(list())
    if level == 0:              # Niveau débutant
        sizex = 10
        sizey = 10
        mines = 10
        for k in range(mines):
            x = random.randint(0,sizex-1)
            y = random.randint(0,sizey-1)
            while (x,y) in coord_mines:
                x = random.randint(0,sizex-1)
                y = random.randint(0,sizey-1)
            coord_mines.append((x, y))
        for coord in coord_mines:
            x = coord[0]
            y = coord[1]
            playground[x][y] = Case(True, 0)
        
        for i in range(sizex):
            for j in range(sizey):
                if (i,j) not in coord_mines:
                    playground[i][j] = Case(False, 0)
        
        for i in range(len(playground)):
            for j in range(len(playground[0])):
                mines = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x != i and y != j:
                            if x>=0 and x<sizex and y>=0 and y<sizey:
                                if playground[x][y].mined:
                                    mines += 1
                playground[i][j].neighboor = mines
        
        return playground

                
    elif level == 1:            # Niveau intermédiaire
        sizex = 16
        sizey = 16
        mines = 40
        for k in range(mines):
            x = random.randint(0,sizex-1)
            y = random.randint(0,sizey-1)
            while (x,y) in coord_mines:
                x = random.randint(0,sizex-1)
                y = random.randint(0,sizey-1)
            coord_mines.append((x, y))
        for coord in coord_mines:
            x = coord[0]
            y = coord[1]
            playground[x][y] = Case(True, 0)
        
        for i in range(sizex):
            for j in range(sizey):
                if (i,j) not in coord_mines:
                    playground[i][j] = Case(False, 0)
        
        for i in range(len(playground)):
            for j in range(len(playground[0])):
                mines = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x != i and y != j:
                            if x>=0 and x<sizex and y>=0 and y<sizey:
                                if playground[x][y].mined:
                                    mines += 1
                playground[i][j].neighboor = mines
        
        return playground
    else:                       # Niveau expert
        sizex = 30
        sizey = 16
        mines = 99
        for k in range(mines):
            x = random.randint(0,sizex-1)
            y = random.randint(0,sizey-1)
            while (x,y) in coord_mines:
                x = random.randint(0,sizex-1)
                y = random.randint(0,sizey-1)
            coord_mines.append((x, y))
        for coord in coord_mines:
            x = coord[0]
            y = coord[1]
            playground[x][y] = Case(True, 0)
        
        for i in range(sizex):
            for j in range(sizey):
                if (i,j) not in coord_mines:
                    playground[i][j] = Case(False, 0)
        
        for i in range(len(playground)):
            for j in range(len(playground[0])):
                mines = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x != i and y != j:
                            if x>=0 and x<sizex and y>=0 and y<sizey:
                                if playground[x][y].mined:
                                    mines += 1
                playground[i][j].neighboor = mines
        
        return playground


def main():
    return None