class Solution(object):
    def robotSim(self, commands, obstacles):
        obstacle_set = set(map(tuple, obstacles))
        x = y = 0
        max_distance = 0
        direction_index = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for command in commands:
            if command == -2:
                direction_index = (direction_index - 1) % 4
            elif command == -1:
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x * x + y * y)
        return max_distance
