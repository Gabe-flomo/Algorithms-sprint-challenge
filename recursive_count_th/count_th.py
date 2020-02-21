'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

count = 0
i = 0
def count_th(word):
    # start with the first index
    # check if the letter is a 't'
    # if it is a 't' check if the next letter is an 'h'
    # if the next letter is an 'h' increase the counter and call the function again starting at the index after the 'h'
    # if the letter is not an 'h' dont increase the counter but still call the functoin again
    global count
    global i

    if i >= len(word):
        return count
    
    # start with the first index
    elif word[i] == "t":
        
        # if it is a 't' check if the next letter is an 'h'
        check_next = word[i+1] == 'h'

        # if the next letter is an 'h' increase the counter and call the function again starting at the index after the 'h'
        if check_next:
            count += 1
            i += 2
            count_th(word)

    # if the letter is not an 'h' dont increase the counter but still call the functoin again
    else:
        i += 1
        count_th(word)
    
    return count
print(f"***th*** occurs {count_th('th')} times")


