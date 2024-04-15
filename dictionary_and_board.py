def get_parameters():
    with open('wordlist.txt', 'r') as file:
        words = [x[:-1] for word in file.readlines()]



    with open('puzzlelist.txt', 'r') as file:
        # Note that however long ago I first did this, I got the code to remove all the unix timestamps so theyre gone now.
        boardlist = file.readlines()

    # Random board
    initial_board = boardlist[371][:64]
    return words, initial_board

def process_parameters(words, initial_board):
    dictionary = []
    letter_counts = []
    for letter_index in range(97,123):
        letter_counts.append(initial_board.count(chr(letter_index)))
                             
    for word in words:
        # Assume valid
        add = 1
        for letter in {*word}:
            if letter_counts[ord(letter) - 97] < word.count(letter):
                # Not valid
                add = 0
                break
        if add:
            dictionary.append(word)
                
    board = [[*initial_board[x::8]] for x in range(7)]
    return dictionary, letter_counts, board
