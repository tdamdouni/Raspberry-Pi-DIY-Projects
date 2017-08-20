import copy, random
import colorsys
import time
nohat = 0
try:
    import unicornhat as uh
except ImportError:
    print "no Unicornhat found"
    nohat = 1
import time

                #j,x
matrix = [[0,0,0,0,0,0,0,0], 
          [0,0,1,0,0,0,0,0], #i,y
          [0,0,1,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]



"""
Rules: 

each cell next generation: 
- under-pop: <2 neighbors: dies
- 2 or 3 neighbors: live 
- overcrowding: >3 neighbors: dies
- reproduction: every dead cell with exactly 3 neighbors: live


"""
if not nohat:
    uh.brightness(.7)

def show_matrix(mat):
    for row in mat:
        print " ".join(str(x[0]) for x in row)

def show_matrix2(mat):
    for y in range(len(mat)):
        for x in range(len(mat[0])):
            if mat[x][y] != (0,0,0):
                uh.set_pixel(x, y, mat[x][y][0], mat[x][y][1], mat[x][y][2])
            else:
                uh.set_pixel(x, y, 0, 0, 0)
    uh.show()
    time.sleep(.2)
        

def neighborhood(x,y, matrix):
    #print x, y, matrix[x][y]
    nbs = 0
    for i in range(y-1,y+2): #rows
        for j in range(x-1,x+2): #cols
            if i<len(matrix) and j<len(matrix):
                if i != y and j != x:
                    if matrix[i][j]:
                        #print i, j
                        nbs+=1
    return nbs

def neighborhood(x,y,mat, basecolor):
    nbs = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i > 0 and j > 0:
                if i<len(mat)-1 and j<len(mat)-1:
                    #i = i%8
                    #j = j%8
                    if not (i==x and j==y):
                        if mat[i][j] == basecolor:
                            nbs+=1
    return nbs

def makenext(height, width, init):
    nextm = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(init)
        nextm.append(row)
    return nextm

def nextgen(matrix, basecolor, shadowed = 1):
    plusgen = makenext(8,8,basecolor)
    for x in range(len(matrix)): #rows
        for y in range(len(matrix[0])): #cols
            nbs = neighborhood(x,y,matrix,basecolor)
            if matrix[x][y] == basecolor:
                #print x, y
                if (nbs < 2) or (nbs > 3):
                    plusgen[x][y] = ([int(z*.5) for z in matrix[x][y]])
            else:
                if nbs == 3:
                    plusgen[x][y] = basecolor
                else:
                    plusgen[x][y] = (0,0,0)
    return plusgen

def ismatempty(mat):
    c = sum([sum([sum(list(x)) for x in row]) for row in mat])
    if c != 0:
        return 0
    else:
        return 1

def matwriteout(mat, prefix = ""):
    with open(prefix + str(time.time()).split(".")[0]+".txt", "w") as o:
        for line in mat:
            o.write(str(line)+"\n")

def makegens(startgen, gens = 10, basecolor = (255,255,255)):
    genslist = [startgen]
    while 1:
        nextmat = nextgen(genslist[-1], basecolor)
        if len(genslist) == 1:
            sind = -1
        if nextmat == genslist[-1]:
            for i in range(5):
                genslist.append(genslist[-1])
            #matwriteout(genslist[0], prefix="stuck")
            return genslist
        elif len(genslist) > 1 and nextmat == genslist[-2]:
            for i in range(20):
                genslist.append(nextmat)
                genslist.append(genslist[-2])
            matwriteout(genslist[-1], prefix="jitter")
            return genslist
        if not ismatempty(nextmat):
            genslist.append(nextmat)
        else:
            return genslist
        
    return genslist

if __name__ == "__main__":
    while 1: 
        time.sleep(1)
        #startcolor = colorsys.hsv_to_rgb(255,255,255)
        startcolor = (random.randint(55,255), random.randint(55,255), random.randint(55,255))
        start = makenext(8,8, init=(0,0,0))
        for i in range(random.randint(17,65)):
            x = random.randint(0,7)
            y = random.randint(0,7)
            #start[x][y] = (255,255,255)
            start[x][y] = startcolor
    
        generations = makegens(start, gens=100, basecolor = startcolor)
        for mat in generations:
        
            if nohat:
                print "#"
                show_matrix(mat)
            else: 
                show_matrix2(mat)
    
        
