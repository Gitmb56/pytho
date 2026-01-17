import string

class LetterGuessGame:
    def __init__(self, cols=6):
        self.letters = list(string.ascii_uppercase)
        self.cols = cols
        self.matrix = []
        self.row_indices = []
        self.col_indices = []

        self.build_rows()

    # ---------------- ROW BUILD ----------------
    def build_rows(self):
        self.matrix = []
        for i, ch in enumerate(self.letters):
            if i % self.cols == 0:
                self.matrix.append([])
            self.matrix[i // self.cols].append(ch)

    # ---------------- COLUMN BUILD ----------------
    def build_columns(self):
        columns = []
        for c in range(self.cols):
            col = []
            for r in range(len(self.matrix)):
                if c < len(self.matrix[r]):
                    col.append(self.matrix[r][c])
            columns.append(col)
        return columns

    # ---------------- DISPLAY ----------------
    def show_row(self, index):
        print(f"Row {index}: {self.matrix[index]}")

    def show_column(self, index, columns):
        print(f"Column {index}: {columns[index]}")

    # ---------------- INPUT ----------------
    def ask_user(self, msg):
        while True:
            ans = input(msg)
            if ans.lower() in ('y', 'n'):
                return ans.lower()
            print("Sirf y ya n likhiye")

    # ---------------- MAIN GAME ----------------
    def play(self):
        word_len = int(input("Aapne kitne letters ka word socha hai? "))

        print("\nSirf pehle letter se guess shuru hoga\n")

        for letter_pos in range(word_len):
            print(f"\nLetter position {letter_pos + 1}")

            # -------- ROW GUESS --------
            for i in range(len(self.matrix)):
                self.show_row(i)
                ans = self.ask_user("Is row me letter hai? (y/n): ")

                if ans == 'y':
                    self.row_indices.append(i)
                    break

            # -------- COLUMN GUESS --------
            columns = self.build_columns()
            for j in range(len(columns)):
                self.show_column(j, columns)
                ans = self.ask_user("Is column me letter hai? (y/n): ")

                if ans == 'y':
                    self.col_indices.append(j)
                    break

        # -------- RESULT --------
        print("\nStored Row Indices :", self.row_indices)
        print("Stored Column Indices :", self.col_indices)

        print("\nGuessed Letters:")
        for r, c in zip(self.row_indices, self.col_indices):
            print(self.matrix[r][c], end=" ")
game = LetterGuessGame()
game.play()

