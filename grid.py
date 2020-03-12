
class Grid:
    def __init__(self, grid_width=10, grid_height=10):
        self.running = True

        self.field_width = 20
        self.field_height = 20

        self.width = grid_width
        self.height = grid_height

        self.MARGIN_LEFT = int(self.field_width/2 + 5)
        self.MARGIN_TOP = int(self.field_height/2 + 5)

        self.grid = [[None] * self.height for _ in range(self.width)]

        self.id_counter = 0


    def get(self, coords):
        return self.grid[coords[0]][coords[1]]


    def swap(self, x1, y1, x2, y2):
        temp = self.grid[x2][y2]
        self.grid[x2][y2] = self.grid[x1][y1]
        self.grid[x1][y1] = temp


    def push(self, x1, y1, x2, y2):
        new_stack = self.grid[x2][y2]
        self.grid[x2][y2] = self.grid[x1][y1]
        self.grid[x1][y1] = self.grid[x1][y1].stacked
        self.grid[x2][y2].stacked = new_stack


    def move(self, x, y, d):
        if d == "right":
            if x+1 > self.width:
                return False
            self.push(x, y, x+1, y)
        elif d == "up":
            if y-1 < 0:
                return False
            self.push(x, y, x, y-1)
        elif d == "down":
            if y+1 > self.height:
                return False
            self.push(x, y, x, y+1)
        elif d == "left":
            if x-1 < 0:
                return False
            self.push(x, y, x-1, y)

    def place_object(self, x, y, obj):
        if self.grid[x][y] is None or self.grid[x][y].replacable:
            self.grid[x][y] = obj

    def place_object_f(self, x, y, obj):
        self.grid[x][y] = obj

    def get_player(self):
        for col in self.grid:
            for entity in col:
                if entity.type == 'player':
                    return entity

