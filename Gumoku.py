############################################
    # Computer Projecct #11
    #
    # Algorithm
    #   main()
    #       display game board  
    #       prompt to input position on the board
    #       check if the position is valid
    #       ensure inputs are valid and display proper code for errors
    #       Check if there is a winner and display proper code when found
    #       keep looping until a winner is found   
    #
    #
    #
#############################################





class GoPiece(object):
    '''
    class that intializes the piece color and also has a function to determine
    if the color is valid. It can also get the string name of the color.
    '''
    def __init__(self,color = "black"):
        '''
        function to initialize the color and to make sure that it is a valid color
        '''
        
        if color != "black" and color != "white":
            raise MyError('Wrong color.') #raisiing error if it is an invalid color
       
        self.__color = color
                
            
        pass  # replace and delete
    
    def __str__(self):
        '''
        function to return the correct symbol for the correct string
        '''
        if self.__color == "black": #black for black dot
            return ' ● '
        if self.__color == "white": #white for white dot
            return ' ○ '

    
    def get_color(self):
        '''
        function to return the string name of the color of the dot
        '''
        return self.__color #returns the color name
        
            
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    '''
    Class to initialize values for the board size, win count, and current player. 
    It also determines the winner horizontally, vertically and diagonally. lastly 
    it assigns a piece to a space and gives the proper errors.
    '''
    def __init__(self,board_size=15,win_count=5,current_player="black"):
        '''
        function to initialize the boardsize, the wincount, and the current player
        It also checks if the board size and win count is an int and the players
        are either black or white
        if all conditions are met, the functino assigns the variables and assigns 
        the board.
        '''
        
        if type(board_size) != int: #checking if board size is int
            raise ValueError
          
        if type(win_count) != int: #checking if win count is an int
            raise ValueError
        
        if current_player != "black" and current_player != "white":
            raise MyError('Wrong color.') #checking if the player is either white or black
        #assigning all variables
        self.__board_size = board_size 
        self.__win_count = win_count
        self.__current_player = current_player
        #Assigning the board wih the board size
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]
            
            
        
            
    def assign_piece(self,piece,row,col):
        '''
        functions that checks for errors regarding the column number and row number
        It also gives an error when the position is occupied. When all the conditions
        are satisfied, the piece is placed.
        '''
        if col < 1 or col > self.__board_size:#checking if the col is less than 1 or bigger than the max board size
            raise MyError('Invalid position.')
        if row < 1 or row > self.__board_size:#checking if the row is less than 1 or bigger than the max board size
            raise MyError('Invalid position.')
        if self.__go_board[row-1][col-1] != ' - ': #checking if the position is occupied
            raise MyError('Position is occupied.')
        
        self.__go_board[row-1][col-1] = piece #place the piece
        
        
            
    def get_current_player(self):
        '''
        function that returns the name of the current player or the color of the dot
        '''
        
        return self.__current_player
        pass  # replace and delete
    
    def switch_current_player(self):
        ''' 
        Function that takes the current player and switches to the 
        opposing player
        '''
        if self.__current_player == 'black':#if the player is black
            self.__current_player = 'white'#switch to white
        else:
            self.__current_player = 'black'#otherwise change it to black
        
        
    def __str__(self):
        '''
        function given within the skeleton code
        '''
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
        
    def current_player_is_winner(self):
        '''
        Function that determines if a winner is found. It checks horizontally, 
        vertically and diagonally for the current player. the disgonal algorithm
        is divided into two parts to check diagonal winning pieces from right to left
        and left to right. 
        '''
        #HORIZONAL LOOP
        #looping through the rows in the board minus the board size
        for row in range(0,self.__board_size): # 
            #looping through the columns for each row getting a position
            for col in range(0,self.__board_size-self.__win_count+1):
                #setting the cell equal to that row and column
                cell = self.__go_board[row][col]
                #checking if the cell is empty
                if cell == ' - ':
                    continue
                #checking if the cell's color is equal to the current player
                if cell.get_color() == self.__current_player:
                    
                    
                    #looping through values it takes to get winner horizontally
                    #HORIZONTAL*********************************
                    for i in range(1,self.__win_count):
                        #initializing cell and adding to the column
                        cell = self.__go_board[row][col+i]
                        #breaks if the cell is ever empty
                        if cell == ' - ':
                            break
                        #breaks if the cell is another player
                        elif cell.get_color() != self.__current_player:
                            break
                        
                    else:
                        return True #WINNER FOUND
          
            
        #VERTICAL LOOP
        for col in range(0,self.__board_size): # 
            #looping through the columns for each row getting a position
            for row in range(0,self.__board_size-self.__win_count+1):
                #setting the cell equal to that row and column
                cell = self.__go_board[row][col]
                #checking if the cell is empty
                if cell == ' - ':
                    continue
                #checking if the cell's color is equal to the current player
                if cell.get_color() == self.__current_player:
                    
                    
                    #looping through values it takes to get winner horizontally
                    #VERTICAL*********************************
                    for i in range(1,self.__win_count):
                        #initializing cell and adding to the column
                        cell = self.__go_board[row+i][col]
                        #breaks if the cell is ever empty
                        if cell == ' - ':
                            break
                        #breaks if the cell is another player
                        elif cell.get_color() != self.__current_player:
                            break
                        
                    else:
                        return True #WINNER FOUND
                    
        #DIAGONAL PART !: diagonal lines going down from left to right            
        for row in range(0,self.__board_size-self.__win_count+1): # 
            #looping through the columns for each row getting a position
            for col in range(0,self.__board_size-self.__win_count+1):
                #setting the cell equal to that row and column
                cell = self.__go_board[row][col]
                #checking if the cell is empty
                if cell == ' - ':
                    continue
                #checking if the cell's color is equal to the current player
                if cell.get_color() == self.__current_player:
                    
                    
                    #looping through values it takes to get winner horizontally
                    
                    for i in range(1,self.__win_count):
                        #initializing cell and adding to the column
                        cell = self.__go_board[row+i][col+i]
                        #breaks if the cell is ever empty
                        if cell == ' - ':
                            break
                        #breaks if the cell is another player
                        elif cell.get_color() != self.__current_player:
                            break
                        
                    else:
                        return True #WINNER FOUND            
        
        #DIAGONAL PART !: diagonal lines going down from right to left
        for row in range(0,self.__board_size-self.__win_count+1): # 
            #looping through the columns for each row getting a position
            for col in range(self.__win_count-1,self.__board_size):
                #setting the cell equal to that row and column
                cell = self.__go_board[row][col]
                #checking if the cell is empty
                if cell == ' - ':
                    continue
                #checking if the cell's color is equal to the current player
                if cell.get_color() == self.__current_player:
                    
                    
                    #looping through values it takes to get winner horizontally
                    
                    for i in range(1,self.__win_count):
                        #initializing cell and adding to the column
                        cell = self.__go_board[row+i][col-i]
                        #breaks if the cell is ever empty
                        if cell == ' - ':
                            break
                        #breaks if the cell is another player
                        elif cell.get_color() != self.__current_player:
                            break
                        
                    else:
                        return True #WINNER FOUND                        
        return False #if no winner is found then return false
        
def main():
    '''
    main function takes the input and splits the row and column from the comma.
    It checks the input to see if they are numbers. then it calls the eppropriate functions
    to assign the piece and display the board. there is also a while loop that 
    continues asking for positions and switching players until a winner is found. 
    '''
    board = Gomoku()
    print(board)# printing the board
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q': #loop unless q is entered for quit
        play_list = play.strip().split(',') #stripping and splitting between row and col
        
        
        
        try:
            try: 
                row = int(play_list[0]) #validating row and column for integers
                col = int(play_list[1])
            
            except: #raise error for incorrect input
                raise MyError("Incorrect input.")
            piece = GoPiece(board.get_current_player())
            board.assign_piece(piece,row,col) #assigning the piece
            if board.current_player_is_winner(): #checking if there is a winner
                print(board) #printing the board when winner is found
                print("{} Wins!".format(board.get_current_player()))
                break
                
            board.switch_current_player()#switching the player        
            
#                

        except MyError as error_message: 
            print("{:s}\nTry again.".format(str(error_message)))
        #printing the board and asking for input afain.
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()
