from tic_tac_toe import TicTacToe

game = TicTacToe()

play = True

while play is True:
    print(game.get_grid())

    #X always starts, so it checks if the number is even or odd
    if game.round_of_play % 2:
        player_x_input = input(f"Enter a row and column you want to place your X\n")
        game.add_user_input(player_x_input, "X")

    else:
        player_o_input = input(f"Enter a row and column you want to place your O\n")
        game.add_user_input(player_o_input, "O")

    #Checks if any player has won
    if game.round_of_play >= 5:
        if game.check_for_winner("X"):
            print(game.get_grid())
            print("Player X won.")

            again = input("Would you like to play again?yes or no. ").lower()
            if again == "yes":
                game.reset()
            else:
                play = False

        elif game.check_for_winner("O"):
            print(game.get_grid())
            print("Player O won")

            again = input("Would you like to play again?yes or no. ").lower()
            if again == "yes":
                game.reset()
            else:
                play = False

    #If its 10th round the grid is full, and it's a tie
    if game.round_of_play == 10:
        print(game.get_grid())
        print("Its a tie.")
        print(" ")
        again = input("Would you like to play again?yes or no. ").lower()
        if again == "yes":
            game.reset()
        else:
            play = False
