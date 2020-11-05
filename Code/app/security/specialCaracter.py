def is_allowed(char_list) :
    
    v = True
    n = len(char_list)
    i = 0
    while v and i < n :
        char = char_list[i]
        v = (char.isalpha() or char.isalnum() or char.isspace())
        i += 1
    return(v)

