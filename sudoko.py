import tkinter as tk
from tkinter import messagebox

SIZE = 4  

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("4x4 Sudoku Solver")

        self.entries = [[None for _ in range(SIZE)] for _ in range(SIZE)]
        self.create_board()
        self.create_solve_button()

    def create_board(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        for i in range(SIZE):
            for j in range(SIZE):
                e = tk.Entry(frame, width=3, font=('Arial', 18), justify='center')
                e.grid(row=i, column=j, padx=5, pady=5)
                self.entries[i][j] = e

                if j in [1] and j != SIZE - 1:
                    e.grid(padx=(5, 15))
                if i in [1] and i != SIZE - 1:
                    e.grid(pady=(5, 15))

    def create_solve_button(self):
        solve_btn = tk.Button(self.root, text="Solve Sudoku", command=self.solve)
        solve_btn.pack(pady=10)

    def get_board(self):
        board = []
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                val = self.entries[i][j].get()
                if val == '':
                    row.append(0)
                else:
                    try:
                        num = int(val)
                        if 1 <= num <= 4:
                            row.append(num)
                        else:
                            messagebox.showerror("Invalid Input", f"Numbers must be between 1 and 4")
                            return None
                    except ValueError:
                        messagebox.showerror("Invalid Input", "Please enter only numbers")
                        return None
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(SIZE):
            for j in range(SIZE):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(0, str(board[i][j]))

    def is_valid(self, board, row, col, num):
        for j in range(SIZE):
            if board[row][j] == num:
                return False
        for i in range(SIZE):
            if board[i][col] == num:
                return False
        start_row = row - row % 2
        start_col = col - col % 2
        for i in range(2):
            for j in range(2):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self, board):
        for row in range(SIZE):
            for col in range(SIZE):
                if board[row][col] == 0:
                    for num in range(1, SIZE + 1):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve_sudoku(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def solve(self):
        board = self.get_board()
        if board is None:
            return  
        if self.solve_sudoku(board):
            self.set_board(board)
            messagebox.showinfo("Success", "Sudoku solved!")
        else:
            messagebox.showinfo("No Solution", "No valid solution exists for the entered puzzle.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
