import re

def concat_values_array(ary):
    str_concat = ""
    for v in ary:
        str_concat += v
    return str_concat

def avaliation_func(str_analysis, label_fnc):
    if label_fnc == 'LEN':
        return len(str_analysis)
    elif label_fnc == 'LETTERS':
        letters = concat_values_array(re.findall(r'[a-zA-z]+', str_analysis))
        return len(letters)
    elif label_fnc == 'NUMBERS':
        numbers = concat_values_array(re.findall(r'[0-9]+', str_analysis))
        return len(numbers)
    elif label_fnc == 'SPECIALS':
        specials = concat_values_array(re.findall(r'[^\w\s]', str_analysis))
        return len(specials)

def avaliation_restric(value_aval, operator_restrict, value_restrict):
    if operator_restrict == '>':
        return value_aval > value_restrict
    elif operator_restrict == '<':
        return value_aval < value_restrict
    elif operator_restrict == '=':
        return value_aval == value_restrict


def validate(passwd, requeriments):
    ary_result_validate = []
    for label_fnc, operator, value_restrict in requeriments:
        value_aval = avaliation_func(passwd, label_fnc)
        result_aval = avaliation_restric(value_aval, operator, value_restrict)
        ary_result_validate.append(result_aval)
    return ary_result_validate

