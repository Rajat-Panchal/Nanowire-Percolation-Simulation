import numpy as np
import matplotlib.pyplot as plt

occupation_probabilty=0.6
grid_size=25

grid=(np.random.rand(grid_size,grid_size)<occupation_probabilty).astype(int)

visited=np.zeros((grid_size,grid_size),dtype=int)
stack=[]

for col in range(grid_size):
    
    if grid[0,col]==1:

        visited[0,col]=1
        stack.append((0,col))


while stack:
    row,col=stack.pop()
    l= [(-1,0),(1,0),(0,-1),(0,1)]
    
    for dr,dc in l:
        r, c= row+dr, col+dc
        if 0<=r<grid_size and 0<=c<grid_size:
            if grid[r,c]==1 and visited[r,c]==0:
                visited[r,c]=1
                stack.append((r,c))
                
percolates=np.any(visited[grid_size-1])

fig, ax= plt.subplots()

for i in range(grid_size):
    for j in range(grid_size):
        if grid[i,j]==0:
            color='white'
        elif visited[i,j]==1:
            color='red'
        else:
            color='blue'

        rect=plt.Rectangle((j,grid_size-i-1),1,1,facecolor=color,edgecolor='gray')
        ax.add_patch(rect)

ax.set_xlim(0,grid_size)
ax.set_ylim(0,grid_size)
ax.set_aspect('equal')
ax.axis('off')

title="Percolates" if percolates else "Does not Percolate"
plt.title(title)
plt.show()