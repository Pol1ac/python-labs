from typing import List

def dfs(current_level: int, current_position: int, current_experience: int, max_experience: List[int]) -> None:
   
   
    if current_level == L:
        max_experience[0] = max(max_experience[0], current_experience)
        return

   
    for next_position in range(len(levels[current_level])):
        next_experience = levels[current_level][next_position]
        
        if abs(next_position - current_position) <= 1:
            dfs(current_level + 1, next_position, current_experience + next_experience, max_experience)


with open("career.in", "r") as file:
    L = int(file.readline())
    levels: List[List[int]] = []
    for _ in range(L):
        levels.append(list(map(int, file.readline().split())))

max_experience = [0]  
dfs(0, 0, levels[0][0], max_experience)
with open("career.out", "w") as file:
    file.write(f"{max_experience[0]}")