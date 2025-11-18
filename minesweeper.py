import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size, num_mines):
    board = [["." for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        mines.add((x, y))

    for (x, y) in mines:
        board[x][y] = "*"

    return board, mines

def count_adjacent_mines(board, x, y):
    size = len(board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == "*":
            count += 1

    return count

def reveal_board(board, mines):
    size = len(board)
    revealed = [["." for _ in range(size)] for _ in range(size)]

    for x in range(size):
        for y in range(size):
            if (x, y) in mines:
                revealed[x][y] = "*"
            else:
                revealed[x][y] = str(count_adjacent_mines(board, x, y))

    return revealed

def play_game():
    size = int(input("Enter board size: "))
    num_mines = int(input("Enter number of mines: "))

    board, mines = create_board(size, num_mines)
    revealed = [["." for _ in range(size)] for _ in range(size)]

    while True:
        print_board(revealed)
        x, y = map(int, input("Enter coordinates to reveal (row col): ").split())

        if (x, y) in mines:
            print("Game Over! You hit a mine.")
            print_board(reveal_board(board, mines))
            break

        revealed[x][y] = str(count_adjacent_mines(board, x, y))

        if all(revealed[x][y] != "." for x in range(size) for y in range(size) if (x, y) not in mines):
            print("Congratulations! You cleared the board.")
            print_board(reveal_board(board, mines))
            break

if __name__ == "__main__":
    play_game()