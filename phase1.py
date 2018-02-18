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
    
    def set_showed(self, showed):
        self.showed = showed

class Demineur:
    '''
    Cette classe contient 3 attributs :
        - finish    : booleen indiquant si la partie est finie
        - level     : int indiquant le niveau du démineur (debutant, intermediaire, expert)
        - playground: tableau a 2 dimensions de cases ou se passe le jeu
    '''
    def __init__(self, level):
        self.finish = False
        self.level = level
        self.playground = create_playground(level)
        self.play()
    
    def dig(self, coord):
        x = coord[0]
        y = coord[1]
        sizex = len(self.playground[0])
        sizey = len(self.playground)
        if x>=0 and x<sizex and y>=0 and y<sizey:
            self.playground[y][x].set_showed(True)
            if self.playground[y][x].mined:
                print("You lose!")
                self.finish = True

    def play(self):
        while not self.finish:
            map = str()
            for j in range(len(self.playground)):
                line = str()
                for i in range(len(self.playground[0])):
                    if not self.playground[j][i].showed:
                        line = line + ". "
                    else:
                        line = line + str(self.playground[j][i].neighboor) + " "
                map = map + line + "\n"
            print(map)
            print()
            ximp = input("Where to dig? x = ")
            yimp = input("Where to dig? y = ")
            while ximp == "":
                ximp = input("Where to dig? x = ")
            while yimp == "":
                yimp = input("Where to dig? y = ")
            x = int(ximp)
            y = int(yimp)
            self.dig((x,y))
            win = True
            for i in range(len(self.playground)):
                for j in range(len(self.playground[0])):
                    if not self.playground[j][i].mined and not self.playground[j][i].showed:
                        win = False
            if win:
                print("You win!")
            self.finish = win or self.finish
        
        map = str()
        for j in range(len(self.playground)):
            line = str()
            for i in range(len(self.playground[0])):
                if not self.playground[j][i].showed:
                    line = line + "X "
                else:
                    line = line + str(self.playground[j][i].neighboor) + " "
            map = map + line + "\n"
        print(map)
        print("Thanks for playing!")

        


############################### Fonctions ###############################


def create_playground(level):
    # Liste qui contiendra les coordonnées des cases minées
    coord_mines = []

    if level == -1:             # Niveau test           5x5         2 mines
        sizex = 5
        sizey = 5
        mines = 2
    elif level == 0:            # Niveau débutant       10x10       10 mines
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
    Demineur(-1)
    # dd = Demineur(0)
    # di = Demineur(1)
    # de = Demineur(2)
    # print()
    # print("Demineur test : ")
    # print("    finish : " + str(dt.finish))
    # print("    level : " + str(dt.level))
    # case = dt.playground[0][0]
    # print("    1ère case : mined : " + str(case.mined))
    # print("    1ère case : flagged : " + str(case.flagged))
    # print("    1ère case : showed : " + str(case.showed))
    # print("    1ère case : neighboor : " + str(case.neighboor))
    # print()
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
    # print("Demineur test : ")
    # for j in range(len(dt.playground)):
    #     line = str()
    #     for i in range(len(dt.playground[0])):
    #         line = line + " " + str(dt.playground[j][i].mined)
    #     print(line)
    # print()
    # for j in range(len(dt.playground)):
    #     line = str()
    #     for i in range(len(dt.playground[0])):
    #         if not dt.playground[j][i].mined:
    #             line = line + " " + str(dt.playground[j][i].neighboor)
    #         else:
    #             line = line + " *"
    #     print(line)

if __name__ == "__main__":
    main()