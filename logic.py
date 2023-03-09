import random

def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
# find a place i and j where a[i][j]==0 for entering random 2 


def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while( mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)        
    mat[r][c]=2

# we are actually reversing each row to reversed 
#fully board

def reverse(mat):
    new_mat=[]
    
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    
    return new_mat

def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat
       
#merging block with same value
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]*=2
                mat[i][j+1]=0
                changed=True

    return mat,changed

# compress function set all number except to one side of board and 
#set all zero to other side
def compress(mat):
    changed=False
    
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    changed=True
                pos+=1
    return new_mat,changed

'''Getting current state'''
# loss,win,Game not over are the three states.

def get_current_state(mat):
    # WIN
    #ANY WHERE 2048 IS PRESENT
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
            
    # ANYWHERE 0 IS PRESENT
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return 'GAME NOT OVER'
    
    #eVERY ROW AND COLOUMN EXCEPT LAST ROW AND COLUMN

    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER'


    '''check for last row ''' 
    for j in range(3):
        if mat[3][j+1]==mat[3][j]:
            return 'GAME NOT OVER'
    
    # CHECK LAST COLOUMN
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'GAME NOT OVER'
        
    # IF ANY OF AVOBE ARE NOT SATISFIED THEN LOSS CASE HAPPEND
    
    return 'LOST'



 
# take left move as generalised 
'''so for right move 1. take reverse and comprises(by left) and then reverse this will give
right move by using left '''



#FOR LEFT MOVEMENT
'''Left 
       - compress
       - merge
       -compress'''

def move_left(grid):
    new_grid,changed1=compress(grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    # here temp dosnt matter only 1 and 2 line of function is enough
    #to know is there changes are not
    new_grid,temp=compress(new_grid)
    return new_grid,changed


# FOR RIGHT MOVEMENT
'''Right
       -reverse
       -compress(same as in left)
       -merge
       -compress(same as in left)
       -reverse'''

def move_right(grid):
    new_grid=reverse(grid)
    new_grid,changed1=compress(new_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    final_grid=reverse(new_grid)
    return final_grid,changed

#UP MOVEMENT MOVEMENT


'''UP 
       -transpose
       -compress(same as in left)
       -merge
       -compress(same as in left)
       -transponse'''

def move_up(grid):
    new_grid=transpose(grid)
    new_grid,changed1=compress(new_grid)
    new_grid,changed2=merge(new_grid)   
    changed=changed1 or changed2 
    new_grid,temp=compress(new_grid)
    final_grid=transpose(new_grid)
    return final_grid,changed
#DOWN MOVEMENT
'''Down
       -transpose
       -reverse
       -compress(same as in left)
       -merge
       -compress(same as in left)
       -reverse
       -transpose'''

def move_down(grid):
    new_grid=transpose(grid) 
    new_grid=reverse(new_grid)
    new_grid,changed1=compress(new_grid)
    new_grid,changed2=merge(new_grid)
    changed=changed1 or changed2
    new_grid,temp=compress(new_grid)
    new_grid=reverse(new_grid)
    final_grid=transpose(new_grid)

    return final_grid,changed

'''movement/compressin of occupied blocks or merging between block happens
then we add 2 randomly'''
#for this we add another return value which decided that compression or merging
#happen or not
#first is final_grid/new_grid and another is compression or merging happend or not