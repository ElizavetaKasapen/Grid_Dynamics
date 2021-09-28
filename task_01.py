

def get_permutations(symbols_list, i, length, permutation_list):
        if i == length:
            permutation_list.append(''.join(symbols_list))
        else:
            for j in range(i, length):
            # swapping
             symbols_list[i], symbols_list[j] = symbols_list[j], symbols_list[i]
             #recursion
             get_permutations(symbols_list, i + 1, length, permutation_list)
             symbols_list[i], symbols_list[j] = symbols_list[j], symbols_list[i] 
            return permutation_list


def main(input_string):
    #list of results
    permutation_list =[]
    #check if it is string
    if type(input_string) is not str or len(input_string)==0:
       return "Please, input string!"
    symbols_list= list(input_string)
    result = get_permutations(symbols_list, 0, len(symbols_list), permutation_list)
    return result




