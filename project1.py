def get_file_content(data_file):
    """
    extract some interested columns data into list of dictionary
    """
    # a list to hold all lines' important content
    data_list = []
    # read data_file line by line and get their data into 'data_list'
    with open(data_file, 'r') as file:
        # track line number
        cnt = 0 
        # iterate line by line
        for line in file:
            cnt += 1
            # the first line is header, not real data. skip it.
            if cnt == 1: continue
            cur_line_content = {}
            # each line's items are separated by ",". as the example, the 2nd line 'line_conent' looks like as below.
            # ['1', 'Bulbasaur', 'Grass', 'Poison', '318', '45', '49', '49', '65', '65', '45', '1', 'False\n']
            line_conent = line.split(',')
            # here, we only care 'Name', 'Attack', and 'Defense' columns data.
            cur_line_content['name'] = line_conent[1]
            cur_line_content['attack'] = line_conent[6]
            cur_line_content['defense'] = line_conent[7]
            cur_line_content['speed'] = line_conent[10]
            # append the current line content to the data_list
            data_list.append(cur_line_content)

    return data_list

# Project 1: we use pokemen.csv to practice.
# download this file from https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv

# TBD, update for your local path for this file.
data_file = '/Users/your_name/Downloads/pokemon.csv'
list_data = get_file_content(data_file)
print(list_data)

# project part - your code starts here.

def find_most_attack_pokemon(list_data):
    """
    parameters: list_data
    return the pokemon name whose attack score is highest
    """

def find_most_defense_pokemon(list_data):
    """
    parameters: list_data
    return the pokemon name whose defense score is highest
    """


def find_fastest_pokemon(list_data):
    """
    parameters: list_data
    return the pokemon name whose speed is fastest
    """
