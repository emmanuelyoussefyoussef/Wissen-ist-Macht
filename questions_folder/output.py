import questions

def start_quiz():
    questions_dict = questions.get_random_questions()

    for question_number, question_info in questions_dict.items():
        question = question_info['question']
        answers = question_info['possible_answers']
        correct_answer = question_info['question_answer']
        image = question_info['picture']
        Category = question_info['current_category']

        print(f'\nFrage {question_number} ({Category}): {question}')
        for i, answer in enumerate(answers, start=1):
            print(f'{i}. {answer}')

        user_answer = input('Antwort eingeben (1-4): ')

if __name__ == '__main__':
    start_quiz()