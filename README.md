This is a mini project for the usage of backtracking algorithm using python.


# 4x4 Sudoku Solver – GUI Application (Tkinter)

A simple and interactive 4x4 Sudoku Solver built with Python and Tkinter. This tool allows users to enter Sudoku puzzles through a graphical interface and solve them using a backtracking algorithm.

---

## Features

* Graphical User Interface (GUI) using Tkinter
* Supports 4x4 Sudoku puzzles
* Uses Backtracking Algorithm for solving
* User inputs through interactive Entry widgets
* Real-time error checking for invalid inputs
* Highlights invalid values (outside range 1–4)
* Displays success/failure messages using messagebox

---

## Screenshot
![Screenshot 2025-06-07 170611](https://github.com/user-attachments/assets/e22d6f96-e960-448f-a5cf-d82421ac5f24)


---

## How It Works

1. The user enters a partially filled 4x4 Sudoku puzzle.
2. Empty cells can be left blank or filled with `0`.
3. Click the “Solve Sudoku” button.
4. The solver will use the backtracking algorithm to compute a valid solution.
5. If a solution is found:

   * The board will auto-fill with the completed puzzle.
   * A success message will be displayed.
6. If no solution is possible:

   * A warning message is shown to the user.

---

## Rules of 4x4 Sudoku

* Each row must contain numbers from 1 to 4 without repetition.
* Each column must contain numbers from 1 to 4 without repetition.
* Each 2x2 subgrid must contain numbers from 1 to 4 without repetition.

---

## Technologies Used

* Python 3.x
* Tkinter (built-in GUI library in Python)

---

## How to Run

### Prerequisites

* Python installed (3.x recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/JoshikaPalametta/sudoko_backtracking_algo.git
   ```

2. Run the program:

   ```bash
   python sudoko.py
   ```

3. The GUI window will open. Enter your Sudoku puzzle and click "Solve Sudoku".

---

## Algorithm Used

This Sudoku solver uses a classic backtracking algorithm to try all possible valid numbers for each empty cell:

* It checks rows, columns, and the 2x2 subgrid to ensure no duplicates.
* If a number is valid, it's placed and the solver proceeds recursively.
* If no number fits, it backtracks to try a different number in the previous cell.

---

