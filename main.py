

def find_sequence_in_list(list_to_check, values):
    if list_to_check[::4] == values:
        return True
    elif list_to_check[2:7:2] == values:
        return True

    for i in range(len(values) - 1):
        if i <= 2 and list_to_check[i::3] == values:
            return True
        # print(list_to_check[i:i + len(values)])

        if list_to_check[i * 3:i * 3 + 3] == values:
            return True

    return False


# values = ["X", "X", "X"]
# data1 = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
# data2 = [1, 1, 4, 3, 1, 2, 1]
#
# print(find_sequence_in_list(data1, values))
# print(find_sequence_in_list(data2, values))

play = True
round_of_play = 1
grid_list = [
        "   A   B   C \n",
        "  -------------\n",
        "1 | ", " ", " | ", " ", " | ", " ", " |\n",
        "  -------------\n",
        "2 | ", " ", " | ", " ", " | ", " ", " |\n",
        "  -------------\n",
        "3 | ", " ", " | ", " ", " | ", " ", " |\n",
        "  -------------\n"
    ]

grid_dict = {
        "1A": 3,
        "1B": 5,
        "1C": 7,
        "2A": 11,
        "2B": 13,
        "2C": 15,
        "3A": 19,
        "3B": 21,
        "3C": 23,
    }

value_x = ["X", "X", "X"]
value_o = ["O", "O", "O"]

while play is True:
    grid = ''.join(grid_list)
    print(grid)

    if round_of_play % 2 or round_of_play == 0:
        player_x_input = input(f"Enter a row and column you want to place your X\n").title()
        if grid_list[grid_dict[player_x_input]] == " ":
            grid_list[grid_dict[player_x_input]] = "X"
            round_of_play += 1
        else:
            print("That place is already occupied")
    else:
        player_o_input = input(f"Enter a row and column you want to place your O\n").title()
        if grid_list[grid_dict[player_o_input]] == " ":
            grid_list[grid_dict[player_o_input]] = "O"
            round_of_play += 1

    if round_of_play >= 5:
        entries = []
        for key in grid_dict:
            entries.append(grid_list[grid_dict[key]])
        if find_sequence_in_list(entries, value_x):
            grid = ''.join(grid_list)
            print(grid)
            print("Player X won.")

            again = input("Would you like to play again?yes or no. ").lower()
            if again == "yes":
                round_of_play = 1
                grid_list = [
                    "   A   B   C \n",
                    "  -------------\n",
                    "1 | ", " ", " | ", " ", " | ", " ", " |\n",
                    "  -------------\n",
                    "2 | ", " ", " | ", " ", " | ", " ", " |\n",
                    "  -------------\n",
                    "3 | ", " ", " | ", " ", " | ", " ", " |\n",
                    "  -------------\n"
                ]
            else:
                play=False

        elif find_sequence_in_list(entries, value_o):
            grid = ''.join(grid_list)
            print(grid)
            print("Player O won")

            again = input("Would you like to play again?yes or no. ").lower()
            if again == "yes":
                round_of_play = 1
                grid_list = [
                    "   A   B   C \n",
                    "  -------------\n",
                    "1 | ", " ", " | ", " ", " | ", " ", " |\n",
                    "  -------------\n",
                    "2 | ", " ", " | ", " ", " | ", " ", " |\n",
                    "  -------------\n",
                    "3 | ", " ", " | ", " ", " | ", " ", " |\n",
                    "  -------------\n"
                ]
            else:
                play = False

    if round_of_play == 10:

        grid = ''.join(grid_list)
        print(grid)
        print("Its a tie.")
        print(" ")
        again = input("Would you like to play again?yes or no. ").lower()
        if again == "yes":
            round_of_play = 1
            grid_list = [
                "   A   B   C \n",
                "  -------------\n",
                "1 | ", " ", " | ", " ", " | ", " ", " |\n",
                "  -------------\n",
                "2 | ", " ", " | ", " ", " | ", " ", " |\n",
                "  -------------\n",
                "3 | ", " ", " | ", " ", " | ", " ", " |\n",
                "  -------------\n"
            ]
        else:
            play = False

