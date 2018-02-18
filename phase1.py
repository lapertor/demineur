import random

############################### Classes ###############################

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
    
    def set_neighboor(self, neighboor):
        self.neighboor = neighboor

class Demineur:
    '''
    Cette classe contient 3 attributs :
        - finish    : booléen indiquant si la partie est finie
        - level     : int indiquant le niveau du démineur (débutant, intermédiaire, expert)
        - playground: tableau à 2 dimensions de cases où se passe le jeu
    '''
    def __init__(self, level):
        self.finish = False
        self.level = level
        self.playground = create_playground(level) 
        


############################### Fonctions ###############################


def create_playground(level):
# Liste qui contiendra les coordonnées des cases minées
    coord_mines = []
    if level == 0:              # Niveau débutant       10x10       10 mines
        sizex = 10
        sizey = 10
        mines = 10
    
    elif level == 1:            # Niveau intermédiaire  16x16       40 mines
        sizex = 16
        sizey = 16
        mines = 40
    
    else:                       # Niveau expert         16x30       99 mines
        sizex = 30
        sizey = 16
        mines = 99

# Création d'un tableau de cases initialisées à 0 et False : playground[y][x] 
    playground = [[Case(False, 0) for i in range(sizex)] for j in range(sizey)]
# Détermination des cases minées
    for k in range(mines):
        x = random.randint(0,sizex-1)
        y = random.randint(0,sizey-1)
        while (x,y) in coord_mines: # Si on répète deux fois la meme coordonnée
            x = random.randint(0,sizex-1)   # On recrée un autre couple de coordonnées
            y = random.randint(0,sizey-1)
        coord_mines.append((x, y))  # On ajoute les coordonnées à la liste
# Placement des cases minées
    for coord in coord_mines:       # Pour chaque couple de coordonnées
        x = coord[0]                # On insère une case minée dans le playground
        y = coord[1]                # aux coordonnées données
        playground[y][x] = Case(True, 0)
        # for j in range(len(playground)):
        #     line = str()
        #     for i in range(len(playground[0])):
        #         line = line + " " + str(playground[j][i].mined)
        #     print(line)

    for j in range(len(playground)):
        for i in range(len(playground[0])):
            pmines = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x != i or y != j:
                        if x>=0 and x<sizex and y>=0 and y<sizey:
                            if playground[y][x].mined:
                                pmines += 1
            playground[j][i].set_neighboor(pmines)
    
    return playground


def main():
    dd = Demineur(0)
    # di = Demineur(1)
    de = Demineur(2)
    print()
    print("Demineur debutant : ")
    print("    finish : " + str(dd.finish))
    print("    level : " + str(dd.level))
    case = dd.playground[0][0]
    print("    1ère case : mined : " + str(case.mined))
    print("    1ère case : flagged : " + str(case.flagged))
    print("    1ère case : showed : " + str(case.showed))
    print("    1ère case : neighboor : " + str(case.neighboor))
    print()
    # print("Demineur intermediaire : ")
    # print("    finish : " + str(di.finish))
    # print("    level : " + str(di.level))
    # case = di.playground[0][0]
    # print("    1ère case : mined : " + str(case.mined))
    # print("    1ère case : flagged : " + str(case.flagged))
    # print("    1ère case : showed : " + str(case.showed))
    # print("    1ère case : neighboor : " + str(case.neighboor))
    # print()
    # print("Demineur expert : ")
    # print("    finish : " + str(de.finish))
    # print("    level : " + str(de.level))
    # case = de.playground[0][0]
    # print("    1ère case : mined : " + str(case.mined))
    # print("    1ère case : flagged : " + str(case.flagged))
    # print("    1ère case : showed : " + str(case.showed))
    # print("    1ère case : neighboor : " + str(case.neighboor))
    # print()
    print("Demineur expert : ")
    for j in range(len(de.playground)):
        line = str()
        for i in range(len(de.playground[0])):
            line = line + " " + str(de.playground[j][i].mined)
        print(line)
    print()
    for j in range(len(de.playground)):
        line = str()
        for i in range(len(de.playground[0])):
            if not de.playground[j][i].mined:
                line = line + " " + str(de.playground[j][i].neighboor)
            else:
                line = line + " *"
        print(line)

if __name__ == "__main__":
    main()