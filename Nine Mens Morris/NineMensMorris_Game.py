############################################
    # Computer Projecct #10
    #
    # Algorithm
    #   main()
    #       display game data and rules       
    #       prompt to input position until 18 pieces on board
    #       switch players back and forth between X and O
    #       ensure inputs are valid and display proper code when help 
    #       or reset is requested
    #       
    #       prompt to input origin and destination to move piece
    #       call correct functions to execute move and ensure it is within bounds of rules
    #       prompt to remove opponents piece if a mill is formed after the move    
    #       End the game when one of the player's pieces count is less than 3
    #          
    #
    #
    #
#############################################

import NMM #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""


MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
        
def count_mills(board, player):
    """
    This function counts the number of mills on the board for the specified player
    input: board and the player
    output is the count of mills
    """
    count = 0 #intialize count
    for item in board.MILLS: #loop through items in possible mills
        x = 0 
        for point in item: #loop through the tuple from the class
            if board.points[point]==player: #check if the point belongs to the player
                x+=1
        if x==3: #if all three belong to the player increase the main count of mills by 1
            count+=1
            
          
    return count #return the final count
             
            
def place_piece_and_remove_opponents(board, player, destination):
    """
    This function places the piece and checks if a mill is formed. If so, then 
    it calls to another function to remove te piece.
    input is the board, player, and the desired desstination to be placed
    
    """
    
    if board.points[destination] != " ":
        raise RuntimeError("Invalid command: Destination point already taken")
        
    pre_mill = count_mills(board, player) #mill count before the piece change
    
    board.assign_piece(player,destination)#change the piece
    
    post_mill = count_mills(board, player)#mill count after the piece change
    if (post_mill-pre_mill)>0: #checking if there is a mill formed
        print("A mill was formed!")
        print(board)#print the board after declaring a mill was formed
        player2 = get_other_player(player)
        
        remove_piece(board,player2)
        #call to remove piece
    else:
        "*********************************************************************"
        
        
    
    pass  # stub; delete and replace it with your code
     
def move_piece(board, player, origin, destination):
    """
    move piece function checks for adjacency and makes sure the points are valid
    to move the peice from the player onto the board.
    board: input of the current board with all peices at positiions
    origin: specified point to move from
    destination: specified point to move to
    player: specified player that is requesting the move
    returns the board for winner purposes later on in the main function
    """
    adj = board.ADJACENCY #initialize class adjancency dictionary
    p = board.points #points in class
    
    
    
    if destination not in adj[origin]: #checking if the destination is adjacent
        raise RuntimeError("Invalid command: Destination is not adjacent") #raising error
    if p[origin] != player: #checking if the origin belongs to the player
        raise RuntimeError("Invalid command: Origin point does not belong to player")
    
    #calling to clear the origin
    board.clear_place(origin)
    #calling for function to transfer the piece
    place_piece_and_remove_opponents(board,player,destination)        
    #returning the board for winning purposes
    return board
       
   
    
def points_not_in_mills(board, player):
    """
    function to find all positions of points that are not in mills
    takes input of the board and the player
    outputs set of positions not in mills
    """
    
    mill_points = set() #initializing set of mill points
    for item in board.MILLS: #looping through items in possible mills
        x = 0
        points = [] #intiialize points list
        for point in item: #looping through ppoints in item of the list of mills
            if board.points[point]==player: 
                x+=1
                points.append(point)
        if x==3: #if all three points are in a mill append it to list of points in a mill
            for char in points:    
                mill_points.add(char)   
        
    total = placed(board,player)
    not_in_mills =total-mill_points #finding not in mills by subtracting all points by points in mills.

    return(not_in_mills) #return set of points not in mills
def placed(board,player):
    """
    the placed function shows the points where the player's peices have been placed
    for the specified player
    input: board and the player
    output is the set of different positions that the player occupies
    """
    s = set()
    #intiializing set
    P = board.points #initializing P as the points in the board
    
    for item in P.items(): #looping through positions in teh board
        if item[1] == player: #if teh belong to the player
            s.add(item[0]) #add it to the set
    return s
            
        
    pass  
    
def remove_piece(board, player):
    """
    remove piece function takes the board and the player as inputs and prompts 
    for a position to remove the piece. 
    input is the board and the player
    does not return anything
    """
    p = points_not_in_mills(board, player)
    if len(p)==0:
        p = placed(board,player)
    while True: #loop with try and except to weed out all raise error functions
        remove = input("Remove a piece at :> ").strip().lower()
        try: #try except to loop through and find errors in the input of the remove input
            
            if remove not in board.points: #checking if its a valid points
                raise RuntimeError("Invalid command: Not a valid point")
            if board.points[remove] != player:#hecking if it belongs to a player
                raise RuntimeError("Invalid command: Point does not belong to player")
            if remove not in p: #if the point is in a mill
                raise RuntimeError("Invalid command: Point is in a mill")
            #if all the above are not satisfied and no raid errors are brought up, call to remove piece
            board.clear_place(remove)
            
                
            break
        except RuntimeError as error_message: #if error found, prompted again to try again
                print("{:s}\nTry again.".format(str(error_message)))
                #remove = input("Remove the piece from :> ").strip().lower()
 
    
    pass
           
def is_winner(board, player):
    
    """
    This function uses the board and a player as inputs to determine the input
    input: board and a player
    output: true or false if a game is won or not
    """
    p1 = placed(board,player)
    #print(len(p1))
    player2 = get_other_player(player)
    p2 = placed(board,player2)
    #if the pieces of either oppononent falls below 3 and no mills can be formed
    if len(p2)<3 or len(p1)<3:
        return True
    else:
        return False
    
    #player on eless than three player 3
    pass  # stub; delete and replace it with your code
   
def get_other_player(player):
    """
    Get the other player.
    """
    
    return "X" if player == "O" else "O"
    
def main():
    """
    The main function has no inputs but uses two while loops to go through 
    both phases of the game. It also prints when the game is won and calls
    functions that are written above to move and remove pieces. 
    """
    #Loop so that we can start over on reset
    while True:
        #Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0 # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent
        valid_points = []
        B = board.points
        for item in B.items():
            valid_points.append(item[0])
        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            
            try: #try loop in phase one to validate the input and call the proper functions
                if command == "h":#checking if help is requested
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                if command == "r": #checking if reset is requested
                    break
                if command not in valid_points: #checking if a valid point
                    raise RuntimeError("Invalid command: Not a valid point")
                
                else:
                    #call to place the piece and then switch to another player
                    place_piece_and_remove_opponents(board, player, command)
                    player = get_other_player(player)
                    placed_count += 1 #count is increased to make sure only 18 pieces are put on the board
              
                
                pass  
                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                
            #Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
        
        #Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            try:
                if command == "h":#checking again for help
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                    continue
                if command == "r":#cehcking for a reset
                    break
                if len(command)!=2:#chekcing if the length of the input is two since phase 2
                    raise RuntimeError("Invalid number of points")
                origin = command[0]#setting origin to first part of input
                destination = command[1] #setting destination to second part of input
                if origin not in valid_points: #checking is the origin is a valid point
                    raise RuntimeError("Invalid command: Not a valid point")
                if destination not in valid_points:#checking if destination is a valid point
                    raise RuntimeError("Invalid command: Not a valid point")
                board = move_piece(board, player, origin, destination) #calling for moving the piece if all abve is met
                player = get_other_player(player) #cahnging the player
                
                #code to check if a winner is achieved
                if is_winner(board,player) == True:
                    print(BANNER)#print the banner once met
                    command = "q"#quit the program
                    break
                 
                
                pass  # stub; delete and replace it with your code
                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))         
            #Display and reprompt
            print(board)
            #display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return

            
if __name__ == "__main__":
    main()
