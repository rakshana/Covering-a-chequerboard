class Chequerboard:

    def __init__(self):
        self.board = []
        self.create_new_board()
        self.visited = 0
        self.block_count = 0

    def create_new_board(self):
        for i in range(10):
            row = []
            for j in range(10):
                row.append(0)
            self.board.append(row)

    def clear_board(self):
        for i in range(10):
            for j in range(10):
                self.board[i][j] = 0
        self.visited = 0
        self.block_count = 0


class Rules():

    def __init__(self):
        self.board = None
        self.directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        pass

    def move(self, tile, direction, board):
        self.board = board
        new_tile = []
        if direction == 'N':
            if tile[0]-3 < 0 or self.board[tile[0]-3][tile[1]] == 1:
                return False
            else:
                new_tile = [tile[0]-3, tile[1]]

        elif direction == 'S':
            if tile[0]+3 > 9 or self.board[tile[0]+3][tile[1]] == 1:
                return False
            else:
                new_tile = [tile[0]+2, tile[1]]

        elif direction == 'E':
            if tile[1]+3 > 9 or self.board[tile[0]][tile[1]+3] == 1:
                return False
            else:
                new_tile = [tile[0], tile[1]+3]

        elif direction == 'W':
            if tile[1]-3 < 0 or self.board[tile[0]][tile[1]-3] == 1:
                return False
            else:
                new_tile = [tile[0], tile[1]-3]

        elif direction == 'NE':
            if (tile[1]+2 > 9 or tile[0]-2 < 0) or self.board[tile[0]-2][tile[1]+2] == 1:
                return False
            else:
                new_tile = [tile[0]-2, tile[1]+2]

        elif direction == 'NW':
            if (tile[1]-2 < 0 or tile[0]-2 < 0) or self.board[tile[0]-2][tile[1]-2] == 1:
                return False
            else:
                new_tile = [tile[0]-2, tile[1]-2]

        elif direction == 'SE':
            if (tile[0]+2 > 9 or tile[1]+2 >9) or self.board[tile[0]+2][tile[1]+2] == 1:
                return False
            else:
                new_tile = [tile[0]+2, tile[1]+2]

        elif direction == 'SW':
            if (tile[1] - 2 < 0 or tile[0] + 2 > 9) or self.board[tile[0]+2][tile[1]-2] == 1:
                return False
            else:
                new_tile = [tile[0] + 2,tile[1] - 2]

        return new_tile


class Game():
    def __init__(self):
        self.chequerboard = Chequerboard()
        self.board = self.chequerboard.board
        self.rules = Rules()
        self.directions = self.rules.directions

    def check_board_coverage(self, base_tile, direction='N', rotation='clockwise'):
        self.board[base_tile[0]][base_tile[1]] = 1
        self.chequerboard.visited += 1
        direction_index = self.directions.index(direction)
        if self.chequerboard.visited != 100 and self.chequerboard.block_count < 7:
            can_move = self.rules.move(base_tile, direction, self.board)
            if can_move:
                self.chequerboard.block_count = 0
                self.check_board_coverage(can_move, direction, rotation)
            else:
                self.chequerboard.block_count += 1
                if rotation == 'clockwise':
                    direction_index += 1
                    if direction_index > 7:
                        direction_index = 0
                    return self.check_board_coverage(base_tile, self.directions[direction_index])
                else:
                    direction_index -= 1
                    if direction_index < 0:
                        direction_index = 7
                    return self.check_board_coverage(base_tile, self.directions[direction_index])

        if self.chequerboard.visited == 100:
            return 'board covered'
        return self.chequerboard.visited


if __name__ == '__main__':
    game = Game()
    total_scenarios = 0
    for i in range(10):
        for j in range(10):
            for direction in game.rules.directions:
                result = game.check_board_coverage([i, j], direction)
                if result == 'board covered':
                    print str(i) + ', ' + str(j) + ' Direction : ' + direction + ' clockwise'
                    total_scenarios += 1
                game.chequerboard.clear_board()

    for i in range(10):
        for j in range(10):
            for direction in game.rules.directions:
                result = game.check_board_coverage([i, j], direction, 'anticlockwise')
                if result == 'board covered':
                    print str(i) + ', ' + str(j) + ' Direction : ' + direction + ' anticlockwise'
                    total_scenarios += 1
                game.chequerboard.clear_board()
    print total_scenarios

