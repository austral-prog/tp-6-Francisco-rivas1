def remove_elements(lista):
    result = lista.copy()
    indices_to_remove = [0, 4, 5]
    for index in sorted(indices_to_remove, reverse=True):
        if index < len(result):
            del result[index]
    return result


def add_elements(lista_add):
    result = lista_add.copy()
    result.insert(0, 'Pink')    
    result.append('Yellow')     
    return result


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    return sorted(list_to_compare1) == sorted(list_to_compare2)


def list_of_lists(list_of_lists_to_modify):
    if len(list_of_lists_to_modify) != 3:
        return list_of_lists_to_modify
    else:
        return [
        list_of_lists_to_modify[0][:2],  
        list_of_lists_to_modify[1][1:4] 
        if len(list_of_lists_to_modify[1]) >= 4 
        else list_of_lists_to_modify[1][1:],  
        list_of_lists_to_modify[2][-2:]]
