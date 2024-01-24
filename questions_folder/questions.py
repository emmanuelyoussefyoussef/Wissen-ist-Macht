import random

questions_dict = {
    1: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    2: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    3: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    4: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    5: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    6: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    7: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    8: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    9: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    10: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'sports.jpg',
        'category': 'Sport'
    },
    11: {
        'question': 'Wer war der erste deutsche Bundeskanzler?',
        'possible_answers': ['a) Wolfgang Schäuble', 'b) Konrad Adenauer', 'c) Helmut Schmidt', 'd) Joachim Gauck'],
        'right_answer': 'b) Konrad Adenauer',
        'picture': '',
        'cotegory': 'Allgemeinbildung'
    },
    12: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    13: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    14: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    15: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    16: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    17: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    18: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    19: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    20: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Allgemeinbildung'
    },
    21: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    22: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    23: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    24: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    25: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    26: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    27: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    28: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    29: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    30: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': '',
        'category': 'Filme/Comics'
    },
    31: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    32: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    33: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    34: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    35: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    36: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    37: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    38: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    39: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    40: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'history.jpg',
        'category': 'Geschichte'
    },
    41: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    42: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    43: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    44: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    45: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    46: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    47: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    48: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    49: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
    50: {
        'question': '',
        'possible_answers': ['a)', 'b)', 'c)', 'd)'],
        'right_answer': '',
        'picture': 'geography.jpg',
        'category': 'Geographie'
    },
}

# Funktion um zufällig 10 Fragen auszuwählen
def get_random_questions():
    questions_keys = list(questions_dict.keys()) # holt die Fragen durch die Nummerierung (Schlüssel) aus dem Dictionary
    random_questions_keys = random.sample(questions_keys, 10) # zufällige Auswahl von 10 Fragen
    random_questions = {key: questions_dict[key] for key in random_questions_keys} # erstellt neues Dictionary mit den ausgewählten 10 Fragen
    return random_questions # neues Dictionary wird zurückgegeben
