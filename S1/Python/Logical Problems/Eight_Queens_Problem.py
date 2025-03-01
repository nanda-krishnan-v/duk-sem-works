class NQueens:
    def __init__(self, n=8):
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def solve_n_queens_util(self, row):
        if row == self.n:
            return True
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                if self.solve_n_queens_util(row + 1):
                    return True
                self.board[row] = -1
        return False

    def solve(self):
        if self.solve_n_queens_util(0):
            self.print_board()
        else:
            print("No solution found.")

    def print_board(self):
        for row in range(self.n):
            line = ['Q' if self.board[row] == col else '.' for col in range(self.n)]
            print(' '.join(line))

n_queens = NQueens()
n_queens.solve()