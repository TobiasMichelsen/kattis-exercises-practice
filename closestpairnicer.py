#inspiration: https://www.geeksforgeeks.org/dsa/closest-pair-of-points-using-divide-and-conquer-algorithm/

import sys, io
import math


# change to sys.stdin
lines = sys.stdin.read().splitlines() 

cursor = 0
tracker = int(lines[cursor]); cursor += 1

list_of_coordinates = []

for line in range(tracker): 
    coordinates = lines[cursor]; cursor += 1
    
    list_of_coordinates.append(coordinates)
    #print(f"list_of_coordinates: {list_of_coordinates}")
    
points = []
for coordinate in list_of_coordinates:
    x1, y1 = map(float, coordinate.split())
    points.append((x1, y1))
    #print(points)

    
def brute_force(points):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = math.hypot(x1 - x2, y1 - y2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return min_distance, closest_pair


def strip_closest(strip, d, pair):
    strip = sorted(strip, key=lambda p: p[1])
    n = len(strip)
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1]) < d:
            x1, y1 = strip[i]
            x2, y2 = strip[j]
            dist = math.hypot(x1 - x2, y1 - y2)
            
            if dist < d:
                d = dist
                pair = (strip[i], strip[j])
            j += 1
    return d, pair


def closest_util(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_x = points[mid][0]

    dist_left, pair_left = closest_util(points[:mid])
    dist_right, pair_right = closest_util(points[mid:])


    if dist_left < dist_right:
        d, pair = dist_left, pair_left
    else:
        d, pair = dist_right, pair_right


    strip = [p for p in points if abs(p[0] - mid_x) < d]
    return strip_closest(strip, d, pair)


points_sorted = sorted(points, key=lambda p: p[0])
min_distance, closest_pair = closest_util(points_sorted)

for x, y in closest_pair:
    print(x, y)
