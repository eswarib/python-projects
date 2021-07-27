#Game of life
"""
1. Any live cell with fewer than two live neighbours dies, as if by loneliness.
2. Any live cell with more than three live neighbours dies, as if by overcrowding.
3. Any live cell with two or three live neighbours lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbours comes to life.

"""

import copy
import time

#function to find the number of live neighbour cells for a given cell
# a cell has 8 neighbours, 2 vertical, 2 horizontal, four diagonal neighhours
# input will be co-ordinates of the current cell
# no validation will be done in this function
def get_live_neighbourcell_count(a,i,j):
    count = 0
    i_limit = len(a)-1
    j_limit = len(a[0])-1
    for x in range(-1,2) :
        
        if(i == 0 and x == -1): #edge case
            continue 
        if(i == i_limit and x == 1) :
            continue
        if(j == 0 ) :
            count = count + a[i+x][j] + a[i+x][j+1]
            continue
        if(j == j_limit) : # last column
            count = count + a[i + x][j-1] + a[i+x][j] 
        else :
            count = count + a[i + x][j-1] + a[i+x][j] + a[i+x][j+1]
    
    #the current element should be excluded
    count = count - a[i][j]
    return count
    
def print_cells(life) :
    for row in life :
        print(row)   

        
def life_cell_evalution(still_life,start,end):
    a = still_life
    live_cells = []
    #rows = len(still_life)
    #columns = len(still_life[0])
    row_min = start[0]
    row_max = end[0]
    col_min = start[1]
    col_max = end[1]

    new_life = []
    import copy
    new_life = copy.deepcopy(still_life)
    
    a=still_life
    loop_count = 0
    
    #for every tick life is going to change
    #for i in range(rows) :
        #for j in range(columns) :
    for i in range(row_min,row_max+1) :
        for j in range(col_min,col_max+1) :
            loop_count += 1
            live_cell_cnt = get_live_neighbourcell_count(a,i,j)
            if(a[i][j] == 1) :
                if( (live_cell_cnt < 2) or (live_cell_cnt > 4)) :
                    #this cell will die because of lonliness or overcrowding
                    new_life[i][j] = 0
                else :
                    live_cells.append([i,j])
            else :          
                if(live_cell_cnt == 3) :
                    #this cell will come live
                    new_life[i][j] = 1
                    live_cells.append([i,j])
    print(f"Number of loops required : {loop_count}")
    return new_life,live_cells
                
#we need to calculated the live cell count for all the live cells and accordingly 
# change the cell status to '0' - dead or '1' - live
#Assuming list will be given as input. Need to add a code for validation
def game_of_life (still_life,no_of_generation):

    generation = 0

    while(generation < no_of_generation) :
        generation += 1
        
        # it is enought to apply the game logic to a bubble, a big square
        #engulfing all the live cells, to increase the performance
        # determine the lowest i,j, highest i,j
        start_pos,end_pos = get_game_bubble(still_live_cell_pos,grid_size_x,grid_size_y)

        print(f"We are going to check all the celss within the positions,{start_pos} to {end_pos}")

        next_gen,live_cells = life_cell_evalution(still_life,start_pos,end_pos)
        
        #now let's print the cell after the 1st tick
        print(" ---- new_life cells afer 1st tick ------ ")
        print_cells(next_gen)
        
        #let's print the positions of the live cells
        print(f"Printing positions of live cells")
        for live_cell in live_cells :
            print(f"{live_cell}")

        #let's keep this new life and discard the previous
        still_life = copy.deepcopy(next_gen)

        time.sleep(5)
        

        
#This function builds the game floor from the co-ordinates of live cells
def fabricate_game_floor(still_life,input_pos) :
    
    temp = input_pos.split(';')

    #position_list = list((map(lambda x: x.split(','),temp)))
    #print(position_list)
    still_live_cell_pos = []
    for pos in temp :
        co_ordinates=pos.split(',')
        
        x = int(co_ordinates[0])
        y = int(co_ordinates[1])
        if(x > grid_size_x or y > grid_size_y) :
            print('Value error')
            return still_life
        still_life[x][y] = 1
        still_live_cell_pos.append([x,y])
    
    return still_life, still_live_cell_pos

def min(a,b):
    if(a<b) :
        return a
    else :
        return b

def max(a,b):
    if(a>b) :
        return a
    else :
        return b
        
        
def get_game_bubble(cell_pos,xMax,yMax) :
    min_x = cell_pos[0][0]
    min_y = cell_pos[0][0]
    max_x = cell_pos[0][0]
    max_y = cell_pos[0][0]
    
    for pos in cell_pos :
        mix_x = min(min_x,pos[0])
        min_y = min(min_y,pos[1])
        
        max_x = max(max_x,pos[0])
        max_y = max(max_y,pos[1])

    if(min_x > 0 ):
        min_x -= 1
    if(min_y > 0) :
        min_y -= 1
        
    if(max_x < xMax) :
        max_x += 1
    if(max_y < yMax) :
        max_y += 1

    start_pos = [min_x,min_y]
    end_pos = [max_x,max_y]
    
        
    return start_pos,end_pos



#Start of the game   

        
import sys

if(len(sys.argv) < 3):
    raise Exception("Less number of arguments....")
    

input_pattern = sys.argv[1]

#output will be given for these many no of generation
no_of_generation = int(sys.argv[2])

#let's define the game of life grid to be certain size
grid_size_x = 10
grid_size_y = 10

#let's initialise the grid
#init_row = [0 for _ in range(0,grid_size_y)]
#still_life = [init_row for _ in range(0,grid_size_x)]
still_life=[]
for _ in range(0,grid_size_x):
    still_life.append([0 for _ in range(0,grid_size_y)])

print('Game of life grid initialised to zero')
#print_cells(still_life)

#live cell co-ordinates are given as input.
# let's form the matrix with that
still_life,still_live_cell_pos = fabricate_game_floor(still_life,input_pattern)

print('Initial seed of still life')
print_cells(still_life)



game_of_life(still_life,no_of_generation)


        

