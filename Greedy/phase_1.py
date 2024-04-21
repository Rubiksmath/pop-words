from dictionary_and_board_greedy import *
from board_class_greedy import *
import time


global count
count = 0


def greedy_search(board, score, dictionary):
    global count
    print(count := count + 1)

    if not board.array:
        # Board cleared, must double score and return since definitely no moves
        return score * 2, [board]

    if sum(len(col) for col in board.array) < 3:
        # 1 or 2 letters, definitely no moves
        return score, [board]
        

    # Find all moves
    #print(board)
    possible_moves = make_possible_moves(board.array, dictionary)
    
    if not possible_moves:
        #print(possible_moves, 'e')
        # In this case, best score = current score, 
        return score, [board]
    moves_sorted = sorted(possible_moves, key = lambda x: x['score'], reverse = True)
    max_score = moves_sorted[0]['score']
    #print(max_score)

    # Best score from this position >= current score + max_score, but doesnt matter if we set it lower to start
    best_score_forwards = 0
    best_list = []

    for move in moves_sorted:
        
        move_score = move['score']
        
        if move_score < max_score:
            # Not greedy
            break

        move_safe = [move['word'], move['move']]
        #print(move_safe)

        # Top score and the boards with that score with this move ONLY to begin
        #print(board);print(move)
        top_score, highest_scoring_boards = greedy_search(board.make_move(move_safe, flag = True), score + move_score, dictionary)
        
        # Did this move's best end score beat or equal the others we checked so far? If not, we can forget about them
        if top_score > best_score_forwards:

            best_score_forwards = top_score

            # Replacement is valid since we are beating the target outright
            best_list = highest_scoring_boards

        elif top_score == best_score_forwards:

            # Add to list of best scores, no need to update best score since we tied it
            best_list.extend(highest_scoring_boards)

    # By this point, best_list is precisely what we are after, i.e. it is just best_scoring_boards as far as the previous depth is concerned

    return best_score_forwards, best_list

    
def make_possible_moves(board_array, dictionary, visited = [[False for x in range(DIMENSION)] for y in range(DIMENSION)], trace = []):

    # Finds *all* valid moves for this board given current trace and visited

    
    move_list: list[dict] = []

    if not trace:
        
        # Free to pick anything we want
        for i, col in enumerate(board_array):
            for j, letter in enumerate(col):

                # Cant use this again
                visited[i][j] = True

                moves_from_here = make_possible_moves(board_array, dictionary, visited, [letter, [(i, j)]])
                if moves_from_here:
                        move_list.extend(moves_from_here)
                                    
                # Hate having to do this
                visited[i][j] = False

    else:

        # Can only pick adjacent tiles not yet visited
        start_col, start_row = trace[1][-1]

        # Distance to ground since 0 represents top cell, so now 0 means bottom cell
        cell_height = len(board_array[start_col]) - start_row - 1

        # Valid adjacent column indices
        cols_list = range(max(start_col - 1, 0), min(len(board_array), start_col + 2))

        for col in cols_list:
            column = board_array[col]
            # I use this a lot, lets not recalculate it
            length = len(column)
            
            if length < cell_height:

                # Cant make any moves to this column from that cell (off by one makes it look weird ik)
                continue
            
            # Valid adjacent row indices in some valid adjacent column
            rows_list = range(max(length - cell_height - 2, 0), min(length, length - cell_height + 1))

            for row in rows_list:
                
                if visited[col][row]:
                    # Cant use this
                    continue

                visited[col][row] = True
                
                letter = column[row]
                new = trace[0] + letter
                if any(word.startswith(new) for word in dictionary):
                    # Good to go

                    moves_from_here = make_possible_moves(board_array, dictionary, visited, [new, trace[1]+[(col, row)]])
                    if moves_from_here:
                        move_list.extend(moves_from_here)
                        
                    if new in dictionary:
                        # This is a possible move

                        move_dictionary = {'word': new, 'move': trace[1] + [(col, row)], 'score': SCORE_DICTIONARY[len(new)]}
                        move_list.append(move_dictionary)
                        
                else:
                    # No point wasting our time
                    visited[col][row] = False
                    continue

                visited[col][row] = False

    if move_list:
        return move_list

def print_results(high_score, best, total):
    print(f'Highest score found by greedy was {high_score}, obtained by {len(best)} different move sets')
    for x in range(len(best)):
        data = best[x]
        
        print(f'Solution {x} used the following move set:')
        for state in range(len(data.parents)):
            info = data.parents[state]
            print(f'Move {state + 1} used word "{info[1][0]}" ({SCORE_DICTIONARY[len(info[1][0])]} points), and tile list {info[1][1]}')
            print(f'Board state at this point was:\n{info[0]}')
            #print state[1]
        print(f'Final board state was: {data}')
        print("-"*20)
    print(f"This took {total:.3f} seconds to figure out!")
        

def main():
    
    words, initial_board = get_parameters()
    dictionary, letter_counts, board = process_parameters(words, initial_board)

    start_board = Board(initial_board)
    t0 = time.time()
    high_score, best = greedy_search(start_board, 0, dictionary)
    t1 = time.time()
    total = t1 - t0
    print_results(high_score, best, total)
    
    

main()

            

        
        
                
        
        
    
    
    

    
        

    




            
                
                
                

    
    
    
    
