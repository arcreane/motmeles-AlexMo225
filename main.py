import string
import random


width = 25
height = 15


grid = [[random.choice(string.ascii_uppercase) for i in range(0,width)] for j in range(0,height)]

#grid[0][0]='B'
#grid[0][1]='O'
#grid[0][2]='N'
#grid[0][3]='J'
#grid[0][4]='O'
#grid[0][5]='U'
#grid[0][6]='R'
#grid[0][7]='O'
#grid[0][8]='G'
print("\n".join(map(lambda row: "  ".join(row), grid)))