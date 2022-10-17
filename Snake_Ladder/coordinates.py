coordinates ={}
i=1
x=10
y=560
right=True
for j in range (y,-40,-60):
    if right:
        for k in range (x,610,60):
            coordinates[i]=[k,j]
            i+=1
        right=False
    else:
        for k in range (550,-50,-60):
            coordinates[i]=[k,j]
            i+=1
        right=True
# print(coordinates)

Ladders ={
    4:25,
    13:46,
    33:49,
    42:63,
    50:69,
    62:81,
    74:92
}

Snakes ={
    27:5,
    40:3,
    43:18,
    54:31,
    66:45,
    76:58,
    89:53,
    99:41
}
