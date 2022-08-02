from curses.ascii import isdigit
import re
import json

valid_keys = ['temperature', 'effacement', 'fhr', 'pulse', 'dilatation', 'bp']

def check_int(str):
    return re.match(r"[-+]?\d+(\.0*)?$", str) is not None

def remove_non_keywords(query):
    while query.split()[0] not in valid_keys:
        if len(query.split(' ')) > 1:
            query = query.split(' ', 1)[1]
        else:
            query = ""
            break
    return query

def remove_first_word(query_string):
    if query_string == "":
        rem = ""
    if len(query_string.split()) == 1:
        rem = ""
    else:
        rem = query_string.split(' ', 1)[1]
    return rem

def get_first_word(query_string):
    if len(query_string)>0:
        return query_string.split()[0]
    else:
        return ""

def get_value(query_string, key):
    if query_string == "":
        return "", "",""
    if key == 'bp':
        value1 = get_first_word(query_string)
        rem = remove_first_word(query_string)
        query_string = rem
        
        # Check if the next word is numeric or not
        next_word = get_first_word(query_string)
        
        if not check_int(next_word):
            query_string = remove_first_word(query_string)    

        value2 = get_first_word(query_string)
        return key, [value1, value2], rem
    
    elif key in valid_keys:
        value = query_string.split()[0]
        if len(query_string.split()) == 1:
            rem = ""
        else:
            rem = query_string.split(' ', 1)[1]
        return key, value, rem

def parse(query):
    """"This will be the main method"""
    # query = "temperature 88.3 degree bp 120 bata 80 celcius pulse 93 bpm effacement mota dilatation 8 centimeter" 
    query = query.lower()
    key_value_pairs = dict()
    while len(query) != 0:
        
        # Removong unnecessary words
        query = remove_non_keywords(query)
        if query == "":
            break
        key = query.split()[0]
        key, value, query = get_value(query.split(' ', 1)[1], key) 
        key_value_pairs[key] = value
    
    json_data = json.dumps(key_value_pairs)
    return json_data