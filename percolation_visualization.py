import matplotlib.pyplot as plt
import random
import math
from collections import deque

# PARAMETERS

l = 10
Nc = 1500
AREA = 50

# RANDOM CENTERS

points = [(random.uniform(0, AREA),random.uniform(0, AREA)) for _ in range(Nc)]

# RANDOM SEGMENTS

segments = []

for (x, y) in points:

    theta = random.uniform(0, 2 * math.pi)

    dx = (l / 2) * math.cos(theta)
    dy = (l / 2) * math.sin(theta)

    x1 = x - dx
    y1 = y - dy

    x2 = x + dx
    y2 = y + dy

    segments.append(((x1, y1), (x2, y2)))

# INTERSECTION FUNCTION

def segment_intersection(p1, p2, p3, p4):

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denom = ((x1 - x2) * (y3 - y4)
             - (y1 - y2) * (x3 - x4))

    if abs(denom) < 1e-9:
        return None

    px = (((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4))/ denom)

    py = (((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4))/ denom)

    if (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2) and
        min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4)):
        return (px, py)

    return None

# BUILD GRAPH

graph = {i: [] for i in range(Nc)}

for i in range(Nc):
    for j in range(i + 1, Nc):

        if segment_intersection(segments[i][0], segments[i][1], segments[j][0], segments[j][1]):
            graph[i].append(j)
            graph[j].append(i)


# RANDOM SOURCE/DRAIN POINTS

source_point = (3,3)
drain_point = (47,47)   

# POINT ON SEGMENT CHECK

def point_on_segment(px, py, seg, tol=0.15):

    (x1, y1), (x2, y2) = seg

    dx = x2 - x1
    dy = y2 - y1

    seg_len_sq = dx*dx + dy*dy

    if seg_len_sq == 0:
        return False

    t = ((px - x1)*dx + (py - y1)*dy) / seg_len_sq

    if t < 0 or t > 1:
        return False

    nearest_x = x1 + t*dx
    nearest_y = y1 + t*dy

    dist = math.hypot(px - nearest_x,py - nearest_y)

    return dist < tol


# FIND SOURCE SEGMENT

source = None

for i, seg in enumerate(segments):
    if point_on_segment(source_point[0],source_point[1],seg):
        source = i
        break

# FIND DRAIN SEGMENT

drain = None

for i, seg in enumerate(segments):
    if point_on_segment(drain_point[0],drain_point[1],seg):
        drain = i
        break

# BFS

path = []
path_found = False

if source is not None and drain is not None:

    queue = deque([source])

    visited = {source}
    parent = {}

    while queue:

        current = queue.popleft()

        if current == drain:
            path_found = True
            break

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)
                parent[neighbour] = current
                queue.append(neighbour)

    if path_found:

        node = drain

        while node != source:
            path.append(node)
            node = parent[node]

        path.append(source)
        path.reverse()

        print("Percolating pathway exists!")
        print("Path:", path)

    else:
        print("Source and drain connected to network, but no path exists.")

else:

    if source is None:
        print("Source not connected to any segment.")

    if drain is None:
        print("Drain not connected to any segment.")

plt.figure(figsize=(8, 8))

# Segments
for i, seg in enumerate(segments):

    (x1, y1), (x2, y2) = seg

    if i in path:
        plt.plot([x1, x2],[y1, y2],color='green', linewidth=3)
    else:
        plt.plot([x1, x2],[y1, y2],color='red',linewidth=1, alpha= 0.8)

# Centers
plt.scatter([p[0] for p in points], [p[1] for p in points],color='black',s=8)

# Source
plt.scatter(source_point[0],source_point[1],color='blue',s=40,zorder=5,label='Source')

# Drain
plt.scatter(drain_point[0],drain_point[1],color='yellow',s=40,zorder=5,label='Drain')

plt.xlim(0, AREA)
plt.ylim(0, AREA)
plt.title("Random Nanowire Percolation Network")
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
