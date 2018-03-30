# Jacob Negri
#S:N 13165429

from positional_list import PositionalList

def list_to_positional_list(list_):

    new_pos_list = PositionalList()

    for element in list_:
        new_pos_list.add_last(element)
    return new_pos_list

