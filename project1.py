
from calendar import c
import random

#################FUNCTIONS DEFINED HERE###################

def createboard(a,b,c):
    '''
    Prints the board.
    '''
    print(f'   1     2     3\n      |     |     \na  {a[0]}  |  {a[1]}  |  {a[2]}  \n _____|_____|_____')
    print(f'      |     |     \nb  {b[0]}  |  {b[1]}  |  {b[2]}  \n _____|_____|_____')
    print(f'      |     |     \nc  {c[0]}  |  {c[1]}  |  {c[2]}  \n      |     |     ')

def turn_taking(counter,first,second):
    '''
    Counter starts with 1 on the first move. Func will return 'first' for the first move. Next loop, the counter increments to 2, resuting in returning 'second'.
    This result is stored in the variable 'turn'. Basically, for odd counter values, we return first, and for even counter values, we return second.
    '''
    if counter % 2 == 1:
        return first
    else:
        return second

def randomizer():
    '''
    randomizer shuffles the list X and O. the variables 'first' and 'second' can be assigned by indexing from the shuffled list.
    '''
    x = ['X','O']
    random.shuffle(x)
    return x

def userinput(userinp,a,b,c,turn):
    '''
    -check_list contains all possible values. 
    -Tells whose turn it is.
    -Enters while loop to return valid user output. It first checks if it is a possible coordinate. If not, return to start of loop.
    -If true, it goes through a second check to see if the spot is occupied; this checking happens through func 'check_if_already_XO'. If true, it exits loop and
     returns userinput. This userinput is stored in 'user'.
    '''
    check_list = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']
    print(f"It is {turn}'s turn.")
    while True:
        userinp = input("Please tell us your grid choice: ")
        if userinp not in check_list:
            print("PLEASE CHOOSE A VALID CHOICE.")
            continue
        if check_if_already_XO(a,b,c,userinp) == True:
            print("THIS SPOT IS ALREADY USED!!")
            continue
        else:
            break
    return userinp

def check_if_already_XO(a,b,c,user):
    '''
    checks if the spot chosen by user already has X or O placed. Returns True when the spot is used up. Uses same logic as 'place_input' func.
    '''
    if user[0] == 'a':
        return a[int(user[1])-1] != ' '
    elif user[0] == 'b':
        return b[int(user[1])-1] != ' '
    elif user[0] == 'c':
        return c[int(user[1])-1] != ' '

def place_input(a,b,c, user, turn):
    '''
    It checks the first part of the input (i.e. the letter). It then converts the second part of the input to an integer, subtracts it by one (since indexing starts
    with zero and not with one) and uses this as an index to place 'X' or 'O' at that position.
    '''
    if user[0] == 'a':
        a[int(user[1])-1] = turn
    elif user[0] == 'b':
        b[int(user[1])-1] = turn
    elif user[0] == 'c':
        c[int(user[1])-1] = turn

def checker(val):
    '''
    It first checks for any horizontal or vertical successes, followed by diagonal successes. It does this for X and O. If X success, it changes first part of the 
    bool_list to True and if O success, it changes second part of the bool_list. In the main_game function, mainbool and mainboolo can be set by indexing.
    '''
    bool_list = [False,False]
    if (['X','X','X'] in val) or (('X','X','X') in zip(val[0],val[1],val[2])):
        bool_list[0] = True
        return bool_list
    elif ('X' == val[0][0] and 'X' == val[1][1] and 'X' == val[2][2]) or ('X' == val[0][2] and 'X' == val[1][1] and 'X' == val[2][0]):
        bool_list[0] = True
        return bool_list
    if ['O','O','O'] in val or (('O','O','O') in zip(val[0],val[1],val[2])):
        bool_list[1] = True
        return bool_list
    elif ('O' == val[0][0] and 'O' == val[1][1] and 'O' == val[2][2]) or ('O' == val[0][2] and 'O' == val[1][1] and 'O' == val[2][0]):
        bool_list[1] = True
        return bool_list
    else:
        return bool_list

def checkblank(val,space=' '):
    '''
    Checks for blanks in tic tac toe board. Used in while statement.
    '''
    for value in val:
        if space in value:
            return True
    return False

def maingame():
    '''
    All functions connected here. This function used to play game.
    '''
    #sets the board.
    a = [' ',' ',' ']
    b = [' ',' ',' ']
    c = [' ',' ',' ']
    #defines the variable userinp. Will be later used to store grid coordinates.
    userinp = ' '
    #counter set to 0. It uses counter to switch between X and O.
    counter = 0

    #randomlist stores the randomized list. Value at index 0 is stored in first; value at index 1 is stored in second. Value can be X or O. 
    randomlist = randomizer()
    first = randomlist[0]
    second = randomlist[1]

    #booleans to keep track of X or O successes. To be later used by checker function.
    mainbool = False
    mainboolo = False

    #game starts.
    createboard(a,b,c)

    #intermediate section of the game. It stays in the while loop as long as mainbools are False and there are blanks.
    while mainbool == False and mainboolo == False and checkblank([a,b,c])==True:
        #every loop, counter is incremented.
        counter+=1
        #turn is set either to 'X' or 'O'.
        turn = turn_taking(counter, first, second)
        #userinput is stored. This will be grid coordinates.
        user = userinput(userinp,a,b,c,turn)
        #input is placed on the board.
        place_input(a,b,c,user, turn)
        #board is output.
        createboard(a,b,c)
        #checks for successes and stores the resulting boolean in these variables.
        mainbool = checker([a,b,c])[0]
        mainboolo = checker([a,b,c])[1]
    #now that it has exited the loop, it outputs the appropriate response and returns the index position for the scoreboard list for appropriate incrementing.
    if mainbool == True:
        print("X has won!")
        return 0
    elif mainboolo == True:
        print('O has won!')
        return 1
    elif checkblank([a,b,c]) == False:
        print("ITS A TIE!")
        return 2
################FUNCTIONS END HERE#####################

###############FUNCTIONS IF REPEATED PLAY##############
def ask_if_again():
    '''
    Asks if user wants to play again.
    '''
    checklist = ['y','n','Y','N']
    while True:
        user = input('Would you like to play again? Answer with Y or N. ')
        if user in checklist:
            return user

def playgame():
    '''
    This is the function to be executed. It sets a scoreboard and prints instructions for the game.
    '''
    #start variable defined for first while loop which asks if the user is ready.
    start = ''
    #playing variable defined for the second while loop which asks if the user wants to play again.
    playing = True
    #scoreboard stores number of X wins, number of O wins, number of ties, respectively.
    scoreboard = [0,0,0]
    #INSTRUCTIONS PRINTED AND USER ASKED###
    print("\n>>>>HELLO! YOU ARE PLAYING TIC TAC TOE.\n\n>>>HOW DO WE PLAY THIS GAME?\n--Get someone to play with you (ofcourse). Decide who takes X and O. Place your token by choosing a position on the grid, with the help of the coordinates.")
    print("--Your coordinates should follow this format: <lowercase letter><number>. For example, a3.\n>>>>TO BEGIN GAME, SEND '1'\n\n\n")
    while start!='1':
        start = input("Are you ready? ")
    #GAME BEGINS###########################
    while playing == True:
        #scoreboard is incremented depending on the situation.
        scoreboard[maingame()] += 1
        #asks if players want to play again, along with printing out scoreboard.
        print(f'Number of points for X: {scoreboard[0]}\nNumber of points for O: {scoreboard[1]}\nNumber of ties: {scoreboard[2]}')

        if ask_if_again().lower() == 'n':
            playing = False
            print("THANKS FOR PLAYING!!")
        else:
            print('\n'*100)

#####################FUNCTIONS FOR REPEATED PLAY END HERE#########################    
playgame()