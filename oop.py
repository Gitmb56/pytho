import string

class LetterGuessGame:
    def __init__(self, cols=6):
        self.letters = list(string.ascii_uppercase)
        self.cols = cols
        self.matrix = []
        self.possible_letters = set(self.letters)

        self.build_rows()

    def build_rows(self):
        """Alphabet ko rows me divide karta hai"""
        self.matrix = []

        for i, ch in enumerate(self.letters):
            if i % self.cols == 0:
                self.matrix.append([])
            self.matrix[i // self.cols].append(ch)

    def show_row(self, index):
        """Ek specific row dikhata hai"""
        print(f"\nRow {index}: {self.matrix[index]}")

    def ask_user(self):
        """User se y/n input safely leta hai"""
        while True:
            ans = input("Kya aapke word ka pehla letter is row me hai? (y/n): ")
            if ans.lower() in ('y', 'n'):
                return ans.lower()
            print("Sirf y ya n likhiye.")

    def play(self):
        """Main game loop"""
        print("Koi bhi naam sochiye (sirf pehla letter).")
        input("Ready ho to Enter dabaiye...")

        for idx, row in enumerate(self.matrix):
            self.show_row(idx)
            ans = self.ask_user()

            if ans == 'y':
                self.possible_letters = set(row)
                break
            else:
                self.possible_letters -= set(row)

        print("\nGame Result:")
        if len(self.possible_letters) == 1:
            print("Aapka pehla letter hai:", list(self.possible_letters)[0])
        else:
            print("Possible letters:", self.possible_letters)

game = LetterGuessGame()
game.play()
