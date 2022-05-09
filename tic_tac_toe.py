class TicTacToe:
    def __init__(self):
        self.values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        #dict in wich is specified where each user_input goes
        self.input_to_index = {
            "1A": 0,
            "1B": 1,
            "1C": 2,
            "2A": 3,
            "2B": 4,
            "2C": 5,
            "3A": 6,
            "3B": 7,
            "3C": 8,
        }
        self.round_of_play = 1

    def get_grid(self):
        """Inserts values into a grid for the user to see"""
        grid = [
            "   A   B   C \n",
            "  -------------\n",
            "1 | ", self.values[0], " | ", self.values[1], " | ", self.values[2], " |\n",
            "  -------------\n",
            "2 | ", self.values[3], " | ", self.values[4], " | ", self.values[5], " |\n",
            "  -------------\n",
            "3 | ", self.values[6], " | ", self.values[7], " | ", self.values[8], " |\n",
            "  -------------\n"
        ]
        return "".join(grid)

    def add_user_input(self, user_input: str, value: str):
        """Adds the user input to the values"""
        #if the place is occupied it won't add anything to round of play
        if self.values[self.input_to_index[user_input.title()]] == " ":
            #adds the value to its location
            self.values[self.input_to_index[user_input.title()]] = value
            self.round_of_play += 1
        else:
            print("That place is already occupied")

    def reset(self):
        """resets the game"""
        #Set values and round of play to original values
        self.values = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.round_of_play = 1

    def check_for_winner(self, player):
        """Takes 'X' or 'O' as player and checks if the player has won or not"""

        #Initialises value to check for
        value = [player, player, player]

        # Checks diagonal
        if self.values[::4] == value:
            return True
        elif self.values[2:7:2] == value:
            return True

        # checks horizontal and vertical
        for i in range(len(value) - 1):
            if i <= 2 and self.values[i::3] == value:
                return True
            # print(self.values[i:i + len(values)])

            if self.values[i * 3:i * 3 + 3] == value:
                return True

        return False

