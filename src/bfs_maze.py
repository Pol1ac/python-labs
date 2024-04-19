def bfs(maze, source, destination):
    wide, lenght = len(maze), len(maze[0])
    distance = [[float('inf')] * lenght for _ in range(wide)]
    distance[source[0]][source[0]] = 0
    queue = [source]

    while queue:
        col, row = queue.pop(0)

        if col == destination[0] and row == destination[1]:
            return distance[col][row]

        for iter_col, iter_row in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_col, new_row = col + iter_col, row + iter_row
            if 0 <= new_col < wide and 0 <= new_row < lenght and maze[new_col][new_row] == 1 and (new_col, new_row) not in queue:
                distance[new_col][new_row] = distance[col][row] + 1
                queue.append((new_col, new_row)) 

    return float('inf')


if __name__ == '__main__':
    with open('lab 5/input.txt', 'r') as f:
        source = tuple(map(int, f.readline().split()))
        destination = tuple(map(int, f.readline().split()))
        wide, lenght = map(int, f.readline().split())
        maze = [list(map(int, line.split())) for line in f]

    distance = bfs(maze, source, destination)

    with open('output.txt', 'w') as f:
        if distance == float('inf'):
            f.write('No path found')
        else:
            f.write(str(distance))
