DIMENSION = 5
def get_parameters():
    with open('wordlist.txt', 'r') as file:
        words = [word[:-1] for word in file.readlines()]



    with open('puzzlelist.txt', 'r') as file:
        # Note that however long ago I first did this, I got the code to remove all the unix timestamps so theyre gone now.
        boardlist = file.readlines()

    # Random board
    initial_board = boardlist[371][:DIMENSION**2]
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
        if add and len(word) > 2:
            dictionary.append(word)
                
    board = [[*initial_board[x::DIMENSION]] for x in range(DIMENSION)]
    return dictionary, letter_counts, board

# Maps letter lengths to score
SCORE_DICTIONARY = {3: 1, 4: 2, 5: 4, 6: 7, 7: 11, 8: 17, 9: 25, 10: 35,
                    11: 50, 12: 70, 13: 100, 14: 150, 15: 200, 16: 270,
                    17: 360, 18: 500, 19: 700, 20: 1000, 21: 1500, 22: 2000,
                    23: 2500, 24: 3000, 25: 3500, 26: 4000, 27: 4500, 28: 5000}
