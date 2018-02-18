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
    playground = [][]
    if level == 0:              # Niveau débutant
        for k in range(10):
            x = random.randint(0,9)
            y = random.randint(0,9)
            while (x,y) in coord_mines:
                x = random.randint(0,9)
                y = random.randint(0,9)
            coord_mines.append((x, y))
        for coord in coord_mines:
            x = coord[0]
            y = coord[1]
            playground[x][y] = Case(True, 0)
        
        for i in range(9):
            for j in range(9):
                if (i,j) not in coord_mines:
                    playground[i][j] = Case(False, 0)

                
    elif level == 1:            # Niveau intermédiaire
        
    else:                       # Niveau expert


def main():
