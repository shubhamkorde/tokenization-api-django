from curses.ascii import isdigit
import re
import json

valid_keys = ['temperature', 'effacement', 'fhr', 'pulse', 'dilatation', 'bp', 'discharge', 'drugs']
valid_drugs = ['lignocaine']
valid_discharge = ['red']
valid_words = valid_keys + valid_drugs + valid_discharge
def check_int(str):
    return re.match(r"[-+]?\d+(\.0*)?$", str) is not None

def remove_non_keywords(query):
    while query.split()[0] not in valid_words:
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

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

def parse(query):
    """"This will be the main method"""
    # query = "temperature 88.3 degree bp 120 bata 80 celcius pulse 93 bpm effacement mota dilatation 8 centimeter" 
    query = query.lower()
    response = {
            'temperature': -1,
            'dilatation': -1,
            'pulse': -1,
            'fhr': -1,
            'bp_systolic': -1,
            'bp_diastolic': -1,
            'effacement': -1, 
            'drugs': 'n/a',
            'discharge': 'n/a'
        } 
    while len(query) != 0:
        # Removong unnecessary words
        query = remove_non_keywords(query)
        # print(query)
        if query == "":
            break
        key = query.split()[0]
        key, value, query = get_value(query.split(' ', 1)[1], key) 
        # print("key is ", key)
        # print("value is ", value)
        # print("query is ", query)
        if key == 'bp':
            if value[0].isdigit:
                response['bp_systolic'] = value[0]
            if value[1].isdigit:
                response['bp_diastolic'] = value[1]
        elif key == 'dilatation':
            if value.isdigit:
                response['dilatation'] = value
        elif key == 'drugs':
            if value in valid_drugs:
                response['drugs'] = value
        elif key == 'fhr':
            if value.isdigit:
                response['fhr'] = value
        elif key == 'effacement':
            if value.isdigit:
                response['effacement'] = value
        elif key == 'pulse':
            if value.isdigit:
                response['pulse'] = value
        elif key == 'temperature':
            if is_float(value):
                response['temperature'] = value
        elif key == 'discharge':
            if value in valid_discharge:
                response['discharge'] = value
        else:
            print("incorrect key received")
    print(response)
    return response

def main():
    parse("drugs lignocaine")

if __name__ == "__main__":
    main()