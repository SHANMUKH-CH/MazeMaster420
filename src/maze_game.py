import random

class MazeGame:
    def __init__(self, size=10):
        self.size = size
        self.maze = None
        self.player_pos = [0, 0]
        self.end_pos = [size-1, size-1]
        self.generate_maze()

    def generate_maze(self):
        # Step 1: Create a guaranteed path from start to end
        self.maze = [['#' for _ in range(self.size)] for _ in range(self.size)]
        self.create_guaranteed_path()

        # Step 2: Add random walls
        self.add_random_paths()

        # Step 3: Set start and end
        self.maze[0][0] = 'S'
        self.maze[self.size-1][self.size-1] = 'E'
        self.player_pos = [0, 0]

    def create_guaranteed_path(self):
        x, y = 0, 0
        self.maze[y][x] = ' '
        path = [(x, y)]

        while (x, y) != (self.size - 1, self.size - 1):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)
            found = False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.size and
                    0 <= ny < self.size and
                    self.maze[ny][nx] == '#'):  # Only move to a wall
                    self.maze[ny][nx] = ' '  # Create a path
                    path.append((nx, ny))
                    x, y = nx, ny
                    found = True
                    break

            if not found:
                # If no moves are found, we might have to backtrack (optional)
                if path:
                    x, y = path.pop()



    def add_random_paths(self):
        for _ in range(self.size * self.size // 4):  # Add about 25% more paths
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            if (x, y) not in [(0, 0), (self.size-1, self.size-1)]:
                self.maze[y][x] = ' '

    def move(self, direction):
        dx, dy = {
            'up': (0, -1),    # Up should decrease y
            'down': (0, 1),   # Down should increase y
            'left': (-1, 0),  # Left should decrease x
            'right': (1, 0)   # Right should increase x
        }[direction]

        new_pos = [self.player_pos[0] + dy, self.player_pos[1] + dx]

        if (0 <= new_pos[0] < self.size and
            0 <= new_pos[1] < self.size and
            self.maze[new_pos[0]][new_pos[1]] != '#'):
            self.player_pos = new_pos


    def is_game_over(self):
        return self.player_pos == self.end_pos