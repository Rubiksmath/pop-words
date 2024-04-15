with open('wordlist.txt', 'r') as file:
    words = file.readlines()

# Stack-based language ftw
words = [word[:-1] for word in words]

with open('puzzlelist.txt', 'r') as file:
    # Note that however long ago I first did this, I got the code to remove all the unix timestamps so theyre gone now.
    boardlist = file.readlines()

# Random board
initial_board = boardlist[371][:64]

    
board = [[*initial_board[x::8]] for x in range(7)]
print(board)

