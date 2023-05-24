def dfs(start, target, jug1, jug2):
    stack = [(start, set(), [])]  # Add an empty list to track the steps

    while stack:
        (curr_jug1, curr_jug2), visited, steps = stack.pop()

        if (curr_jug1, curr_jug2) in visited:
            continue
        visited.add((curr_jug1, curr_jug2))

        if curr_jug1 == target or curr_jug2 == target:
            steps.append((curr_jug1, curr_jug2))  # Add the final step
            return steps

        # Add current step to the list
        new_steps = steps + [(curr_jug1, curr_jug2)]

        stack.append(((jug1, curr_jug2), visited.copy(), new_steps))
        stack.append(((curr_jug1, jug2), visited.copy(), new_steps))
        stack.append(((0, curr_jug2), visited.copy(), new_steps))
        stack.append(((curr_jug1, 0), visited.copy(), new_steps))
        stack.append(((min(curr_jug1 + curr_jug2, jug1), max(0, curr_jug1 + curr_jug2 - jug1)), visited.copy(), new_steps))
        stack.append(((max(0, curr_jug1 + curr_jug2 - jug2), min(curr_jug1 + curr_jug2, jug2)), visited.copy(), new_steps))

    return None


def water_jug(jug1_cap, jug2_cap, target):
    start_point = (0, 0)
    target_point = (0, target)

    steps = dfs(start_point, target, jug1_cap, jug2_cap)

    if steps is not None:
        print(f"Target achieved {target_point}")
        print("Steps involved:")
        for step in steps:
            print(step)
    else:
        print("Target not achieved")


water_jug(4, 3, 2)

