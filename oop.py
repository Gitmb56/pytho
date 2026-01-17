import string

class LetterGuessGame:
    def __init__(self, cols=6):
        self.letters = list(string.ascii_uppercase)
        self.cols = cols
        self.matrix = []
        self.possible_letters = set(self.letters)

        self.build_rows()
        self.build_coloumns()

    def build_rows(self):
        """Alphabet ko rows me divide karta hai"""
        self.matrix = []
        
        for i, ch in enumerate(self.letters):
            if i % self.cols == 0:
                self.matrix.append([])
            self.matrix[i // self.cols].append(ch)
    
    def build_coloumns(self):
        """Alphabet ko columns me divide karta hai"""
        self.matrix = [[] for _ in range(self.cols)]

        for i, ch in enumerate(self.letters):
            col_index = i % self.cols
            self.matrix[col_index].append(ch)



    def show_row(self, index):
        """Ek specific row dikhata hai"""
        print(f"\nRow {index}: {self.matrix[index]}")

    def show_column(self, ind):
        """Ek specific column dikhata hai"""
        print(f"\nColumn {ind}: {self.matrix[ind]}")


    def ask_user(self):
        """User se y/n input safely leta hai"""
        usr_word = 
        while True:
            ans = input("Kya aapke word ka pehla letter is row me hai? (y/n): ")
            if ans.lower() in ('y', 'n'):
                return ans.lower()
            print("Sirf y ya n likhiye.")

    def store_index_row_column(self, position):
        """Row ya column ka index store karta hai"""
        self.selected_index = position


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
