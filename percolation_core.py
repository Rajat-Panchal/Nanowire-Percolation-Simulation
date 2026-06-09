import random
import math
from collections import deque

AREA = 50

l = 10

source_point = (3,3)

drain_point = (47,47)

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


def generate_network(Nc):    

    points = [(random.uniform(0, AREA),random.uniform(0, AREA)) for _ in range(Nc)]

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

    graph = {i: [] for i in range(Nc)}
    
    for i in range(Nc):
        for j in range(i + 1, Nc):

            if segment_intersection(segments[i][0], segments[i][1], segments[j][0], segments[j][1]):
                graph[i].append(j)
                graph[j].append(i)
    
    return segments, graph


def find_source_drain(segments):

    source = None

    for i, seg in enumerate(segments):    
        if point_on_segment(source_point[0],source_point[1],seg):
            source = i
            break

    drain = None

    for i, seg in enumerate(segments):
        if point_on_segment(drain_point[0],drain_point[1],seg):
            drain = i
            break
    
    return source, drain


def bfs_path_exists(graph, source, drain):

    queue = deque([source])

    visited = {source}

    while queue:

        current = queue.popleft()

        if current == drain:
            return True

        for neighbour in graph[current]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(neighbour)

    return False


def percolates(Nc):

    segments, graph = generate_network(Nc)

    source, drain = find_source_drain(segments)

    if source is None or drain is None:
        return False

    return bfs_path_exists(graph, source, drain)