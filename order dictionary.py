# In case the dictionary is not in order (thanks game dev)
with open('pog.txt', 'r') as initial_dictionary:
    initial = initial_dictionary.readlines()
    initial.sort()

with open('wordlist.txt', 'w') as fixed_dictionary:
    fixed_dictionary.writelines(initial)
        

