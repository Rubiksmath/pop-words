from dictionary_and_board_greedy import *
import copy

class Board():
    # Maintains letter position dictionary and array representation

    def make_dictionary_replace(self):
        # Todo: Take into account the move that was performed to reduce redundant calculation (if any) (also how???)
        
        letter_indices = {}
        
        for col, data in enumerate(self.array):
            for row, letter in enumerate(data):
                if letter in letter_indices:
                    letter_indices[letter].append((col, row))
                    
                else:
                    letter_indices[letter] = [(col, row)]

        self.letter_list = letter_indices


    def __init__(self, raw: str = '', flag: bool = False, parents: list = [], array: list = []):

        if raw:
            self.array = [[*raw[x::DIMENSION]][::-1] for x in range(DIMENSION)]
            
        elif array:
            self.array = array
            
        else:
            print("Bozo didn't pass an array or a string!")
            return
        
        self.parents = parents
        
        if flag:
            self.make_dictionary_replace()
        
    def make_move(self, move: list[str, list[tuple: (int, int)]], flag: bool = False):

        array_copy = copy.deepcopy(self.array)
        #print(sorted(move[1])[::-1]);print(array_copy)

        for col, row in sorted(move[1])[::-1]:
        
            # Should prevent interference by going backward in sorted list - slow though
            #print(array_copy);print(col,row)
            del array_copy[col][row]

        while [] in array_copy:
            array_copy.remove([])

        # Flag asks whether to create a child with the new board - nobody knows why such variable even exists
        if flag:

            child_parents = copy.deepcopy(self.parents)
            child_parents.append([self, move])
            
            child = Board(parents = child_parents, array = array_copy)
            #self.make_dictionary()

            return child

    def __repr__(self):

        strings = []
        
        for col in self.array:
            
            # Convert to string with padding to prevent index errors
            strings.append("".join(col).rjust(8))
            
        # Transpose string and join newlines
        return "\n".join([" ".join([col[i] for col in strings]) for i in range(8)])
        

            
            

    
        
