import time
import random
from libs.B00370287_functions_misc import slow_print, clear


# Completely pointless 'Dubious Eighties Movie Mode'
# Based on the film War Games as working in the console / terminal reminded me of it


def eighties_mode(first_name):
    # eighties mode function - the first name of the logged in user is passed to the function only to display their name
    clear()
    time.sleep(0.6)
    # function slow print used to emulate typing on the screen as seen in the film. The speed can be adjusted as it
    #   can take a while for a lot of text...
    slow_print(['\n\n\tGREETINGS PROFESSOR FALKEN'])
    time.sleep(1)
    slow_print([f'\n\tSORRY, I MEANT, GREETINGS {first_name}...'.upper()])
    slow_print(['\n\tSHALL WE PLAY A GAME?'])
    # list of games to display if the user 'wants to play a game' - game list from the film
    games = ["\n\t\tFALKEN'S MAZE *", '\n\t\tBLACK JACK *', '\n\t\tGIN RUMMY *', '\n\t\tHEARTS *', '\n\t\tBRIDGE*',
             '\n\t\tCHECKERS *', '\n\t\tCHESS *', '\n\t\tPOKER *', '\n\t\tFIGHTER COMBAT *',
             '\n\t\tGUERRILLA ENGAGEMENT *', '\n\t\tDESERT WARFARE *', '\n\t\tAIR-TO-GROUND ACTIONS *',
             '\n\t\tTHEATREWIDE TACTICAL WARFARE *', '\n\t\tTHEATREWIDE BIOTOXIC AND CHEMICAL WARFARE *',
             '\n\n\t\tGLOBAL THERMONUCLEAR WAR', '\n\n\n\t\t* CURRENTLY UNAVAILABLE']
    # y / Y / yes etc will ultimately load a really bad version of noughts and crosses
    user_input = input('\n\t').capitalize()
    if user_input == 'Y' or user_input == 'Yes':
        slow_print(games, 0.005)
        user_input = input('\n\t\t').upper()
        if user_input != 'TIC-TAC-TOE' and user_input != 'TIC TAC TOE' and user_input != 'GLOBAL THERMONUCLEAR WAR':
            slow_print(["\n\t\tSORRY, THAT ONE IS CURRENTLY UNAVAILABLE", "\n\t\tLET'S PLAY TIC-TAC-TOE INSTEAD"])
        # menu indicates only GTW is playable but will load tic-tac-toe
        elif user_input == 'GLOBAL THERMONUCLEAR WAR':
            slow_print(["\n\t\tSERIOUSLY, WHAT IS WRONG WITH YOU?  THAT SOUNDS FAR TOO DANGEROUS...",
                        "\n\n\t\tLET'S PLAY TIC-TAC-TOE INSTEAD"])
        else:
            slow_print(['\n\t\tGOOD CHOICE', '\n\t\tNOW LOADING TIC-TAC-TOE'])
        time.sleep(2)
        tic_tac_toe()
    else:
        slow_print(['\n\n\tOH, OK.', '\n\tRETURNING TO THE MAIN MENU...'])
        time.sleep(0.5)


def tic_tac_toe():
    # function to print the tic-tac-toe grid - the grid is a list of 9 items with a string of what to display (starts
    # with each item being a space and then replaced with a O or X as appropriate)
    def print_grid():
        clear()
        print('\n\t      1     2     3  \n')
        print('  \t         |     |     ')
        print(f'  \tA     {grid[0]}  |  {grid[1]}  |  {grid[2]}   ')
        print('  \t         |     |     ')
        print('  \t    -----+-----+-----')
        print('  \t         |     |     ')
        print(f'  \tB     {grid[3]}  |  {grid[4]}  |  {grid[5]}   ')
        print('  \t         |     |     ')
        print('  \t    -----+-----+-----')
        print('  \t         |     |     ')
        print(f'  \tC     {grid[6]}  |  {grid[7]}  |  {grid[8]}  ')
        print('  \t         |     |     ')

    def win_check(grid_check):
        # arg is a grid list to check for a win - used from the check to win and the computer_move functions
        # function to check if either player has won - gets item 1 & 2 in a row and compares to item 2 and 3,
        # then if they are the same, then a row of 3 has been made of a O or X - returns true or false
        if ((grid_check[0] != ' ') and (grid_check[0] == grid_check[1] and grid_check[1] == grid_check[2])) or \
                ((grid_check[3] != ' ') and (grid_check[3] == grid_check[4] and grid_check[4] == grid_check[5])) or \
                ((grid_check[6] != ' ') and (grid_check[6] == grid_check[7] and grid_check[7] == grid_check[8])) or \
                ((grid_check[0] != ' ') and (grid_check[0] == grid_check[3] and grid_check[3] == grid_check[6])) or \
                ((grid_check[1] != ' ') and (grid_check[1] == grid_check[4] and grid_check[4] == grid_check[7])) or \
                ((grid_check[2] != ' ') and (grid_check[2] == grid_check[5] and grid_check[5] == grid_check[8])) or \
                ((grid_check[0] != ' ') and (grid_check[0] == grid_check[4] and grid_check[4] == grid_check[8])) or \
                ((grid_check[2] != ' ') and (grid_check[2] == grid_check[4] and grid_check[4] == grid_check[6])):
            return True
        else:
            return False

    def check_for_win(grid_check):
        # check if a winner - and if so, display then ask to play again - if not a winner checks for a draw
        if win_check(grid_check):
            print('\n\tAnd we have a winner...  ')
            if input('\tWould you like to play again? (Y/N)').capitalize() == 'N':
                # return 3 to indicate not playing again
                return 3
            else:
                # return 2 to indicate that the user wants to play again
                return 2
        # if there isn't a winner - call the function to check if it is a draw
        else:
            return check_for_draw(grid_check)

    def check_for_draw(grid_to_check):
        # check for draw
        full_grid = True  # set the variable to true - if any spaces will become false
        # iterate through the grid list and if there are any clear squares, the game hasn't been drawn yet
        for grid_check in grid_to_check:
            if grid_check == ' ':
                full_grid = False
        # if there are no spaces and the check for a win has also been completed, this is displayed with a play again
        # prompt
        if full_grid:
            print("\n\tIt's a draw...")
            if input('\tWould you like to play again? (Y/N)').capitalize() == 'N':
                # not play again
                return 3
            else:
                # play again
                return 2
        else:
            # not a win and not a draw - game to continue
            return 1

    def computer_move():
        # function to get a computer move - will try to play a winning move or block as appropriate
        # function gets the best move by checking every move it can (only one move ahead) and will decide if it will
        # result in a win or blocking an immediate win.  Currently only looking one move ahead

        # get the available moves - new list of indexes from the main grid where there is a space - so only shows the
        # grid indexes that haven't been used
        available_moves = [grid_index for grid_index, grid_space in enumerate(grid) if grid_space == " "]
        # define blank lists move_to_win variable
        best_move = []  # will store any moves to win or immediately block a win
        preferred_available = []  # will store any corner or centre moves available
        move_to_win = None  # will store a move that will win if available

        # iterate through the moves the computer has available
        for move_check in available_moves:
            # create 2 copies of the grid - one to test X's and one to test O's
            test_grid_x = grid.copy()
            test_grid_o = grid.copy()
            # add an X or O to the index being examined
            test_grid_x[move_check] = "X"
            test_grid_o[move_check] = "O"
            # check if a move in the space being checked in the loop will result in a win
            if win_check(test_grid_x):
                best_move.append(move_check)
                # if the computer is X then marks it as a move to win which is preferred to a blocking move
                if comp_sign == "X":
                    move_to_win = move_check
            # same action but for O's
            if win_check(test_grid_o):
                best_move.append(move_check)
                if comp_sign == "O":
                    move_to_win = move_check
            # if the index is even, adds to the preferred list which would mean a corner space or the centre
            # preferred list is used if there is no winning move or blocking move available
            if move_check % 2 == 0:
                preferred_available.append(move_check)
        # if best_move has any items, it will randomly select one in the move_to_play variable
        if best_move:
            move_to_play = best_move[random.randint(0, len(best_move) - 1)]
        # if no best move, will randomly select a preferred move if there are any
        elif preferred_available:
            move_to_play = preferred_available[random.randint(0, len(preferred_available) - 1)]
        # if all else fails, move_to_play will become a random move from the spaces available
        else:
            move_to_play = available_moves[random.randint(0, len(available_moves) - 1)]
        # return a move to win if there is one, if not, return the move_to_play variable
        return move_to_win if move_to_win else move_to_play

    grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # list of grid position
    print_grid()
    comp_sign = None
    # loop until user successfully chooses whether to be a O or X
    while not comp_sign:
        # var sign will be used to replace a space within the grid list when a valid move is made
        sign = input('\n\n\tWould you like to be O or X :').capitalize()
        if sign == 'O':
            comp_sign = 'X'
        if sign == 'X':
            comp_sign = 'O'

    # var set to true for the loop below
    play_again = True

    # start of game
    while play_again:
        grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # set the initial game state
        print_grid()
        random.seed()  # randomise the random function
        coin_toss = random.randint(0, 1)  # decide who goes first...
        if coin_toss == 1:
            print('\n\n\tYou go first...')
            turn = 'user'  # user to play
        else:
            print('\n\n\tI will go first...')
            turn = 'computer'  # computer to play
        input('\n\n\tPress enter to continue...')
        game_ended = False  # var for loop below
        while not game_ended:
            print_grid()

            if turn == 'user' and not game_ended:
                valid_move = False  # var for while loop below - will loop until a valid move is input
                while not valid_move:
                    move = input('\n\tWhere would you like to go (eg: A1):  ').lower()
                    # checks user input and it the move is valid, replaces the relevant index in the grid list to
                    # display the move.  valid_move is set to true to end the while loop
                    if move == 'a1' and grid[0] == ' ':
                        grid[0] = sign
                        valid_move = True
                        print_grid()
                    if move == 'a2' and grid[1] == ' ':
                        grid[1] = sign
                        valid_move = True
                        print_grid()
                    if move == 'a3' and grid[2] == ' ':
                        grid[2] = sign
                        valid_move = True
                        print_grid()
                    if move == 'b1' and grid[3] == ' ':
                        grid[3] = sign
                        valid_move = True
                        print_grid()
                    if move == 'b2' and grid[4] == ' ':
                        grid[4] = sign
                        valid_move = True
                        print_grid()
                    if move == 'b3' and grid[5] == ' ':
                        grid[5] = sign
                        valid_move = True
                        print_grid()
                    if move == 'c1' and grid[6] == ' ':
                        grid[6] = sign
                        valid_move = True
                        print_grid()
                    if move == 'c2' and grid[7] == ' ':
                        grid[7] = sign
                        valid_move = True
                        print_grid()
                    if move == 'c3' and grid[8] == ' ':
                        grid[8] = sign
                        valid_move = True
                        print_grid()
                #  Check if the move results in a win (or draw)
                win = check_for_win(grid)
                if win == 2:  # return from win / draw functions to indicate whether to play again
                    game_ended = True
                    play_again = True
                elif win == 3:
                    game_ended = True
                    play_again = False
                turn = 'computer'  # switch the turn to the computer
            if turn == 'computer' and not game_ended:  # computers turn and game not ended
                time.sleep(1)
                comp_turn = computer_move()  # gets a move for the computer from the computer_move function
                turn = "user"  # switch the turn to the user
                grid[comp_turn] = comp_sign  # update the master grid
                print_grid()
                win = check_for_win(grid)  # check for a win or a draw - then changes values for running loops
                if win == 2:
                    game_ended = True
                    play_again = True

                elif win == 3:
                    game_ended = True
                    play_again = False
                print_grid()
    time.sleep(1)
    # display from the film
    slow = ['\n\n\tA STRANGE GAME.', '\n\tTHE ONLY WINNING MOVE IS', '\n\tNOT TO PLAY.',
            '\n\n\tHOW ABOUT A NICE GAME OF CHESS?']
    slow_print(slow)
    answer = input('\t').capitalize()
    # either choice to return to the main menu
    if answer == 'Y' or answer == 'Yes':
        slow_print(['\n\n\tOH, THIS IS EMBARRASSING...', '\n\tI FORGOT TO BRING MY BOARD.',
                    '\n\n\tTAKING YOU BACK TO THE MENU'])
    else:
        slow_print(['\n\n\tPROBABLY A WISE CHOICE', '\n\tTAKING YOU TO THE MAIN MENU INSTEAD'])
