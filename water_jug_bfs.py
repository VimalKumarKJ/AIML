from collections import deque

def bfs(start, target, jug1, jug2):
    queue = deque([(start, set(), [])])
    
    while queue:
        (curr_jug1, curr_jug2), visited, steps = queue.popleft()
        
        if (curr_jug1, curr_jug2) in visited:
            continue
        visited.add((curr_jug1, curr_jug2))
        
        if curr_jug1 == target or curr_jug2 == target:
            steps.append((curr_jug1, curr_jug2))
            return steps
        
        new_steps = steps + [(curr_jug1, curr_jug2)]
        queue.append(((jug1, curr_jug2), visited.copy(), new_steps))
        queue.append(((curr_jug1, jug2), visited.copy(), new_steps))
        queue.append(((0, curr_jug2), visited.copy(), new_steps))
        queue.append(((curr_jug1, 0), visited.copy(), new_steps))
        queue.append(((min(curr_jug1+curr_jug2, jug1), max(0, curr_jug1+curr_jug2-jug1)), visited.copy(), new_steps))
        queue.append(((max(0,curr_jug1+curr_jug2-jug2), min(curr_jug1+curr_jug2, jug2)), visited.copy(), new_steps))
        
    return None

def water_jug(jug1_cap, jug2_cap, target):
    start_point = (0, 0)
    
    steps = bfs(start_point, target, jug1_cap, jug2_cap)
    if steps is not None:
        print(f"Target acheived: ({target}, 0)")
        print("steps involved:")
        for i in steps:
            print(i)
    else:
        print("Target cannot be acheived")
        
water_jug(4, 3, 2)