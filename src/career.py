from typing import List

def bfs(current_level: int, current_position: int, current_experience: int, max_experience: List[int]) -> None:
   
    L = len(levels)
    max_experience = 0 
    queue = [(0,0, levels [0][0])]

    while queue:
        current_level, current_position, current_experience = queue.pop(0)
        max_experience = max(max_experience, current_experience)


    for next_position in range(len(levels[current_level])):
      if abs(next_position - current_position) <= 1:
        next_experience = current_experience + levels[current_level][next_position]
        queue.append((current_level + 1, next_position, next_experience))



with open("career.in", "r") as file:
    L = int(file.readline())
    levels: List[List[int]] = []
    for _ in range(L):
        levels.append(list(map(int, file.readline().split())))

max_experience = [0]  
dfs(0, 0, levels[0][0], max_experience)
with open("career.out", "w") as file:
    file.write(f"{max_experience[0]}")
