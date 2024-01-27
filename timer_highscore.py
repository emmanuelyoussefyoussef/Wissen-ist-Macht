import time
import threading
import questions

class ScoreTimer:
    def __init__(self):
        self.seconds = 0
        self.score = 10
        self.total_score = 0
        self.total_time = 0  # Neue Variable für die Gesamtzeit
        self.running = False
        self.timer_thread = None

    def start_timer(self):
        self.running = True
        self.timer_thread = threading.Thread(target=self._timer_thread)
        self.timer_thread.start()

    def _timer_thread(self):
        while self.running:
            self.update_score()
            time.sleep(1)
            self.seconds += 1
            self.total_time += 1

    def stop_timer(self):
        self.running = False
        self.timer_thread.join()

    def update_score(self):
        if self.seconds >= 10 and self.seconds % 2 == 0 and self.score > 1:
            self.score -= 1

    def display_timer(self):
        hours, remainder = divmod(self.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f'Time: {hours:02}:{minutes:02}:{seconds:02} | Score: {self.score:02}', end='\r')

    def calculate_total_score(self):
        self.total_score += self.score

    def get_total_time(self):
        return self.total_time

    def get_total_time_formatted(self):
        hours, remainder = divmod(self.total_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{hours:02}:{minutes:02}:{seconds:02}'

def start_quiz(timer):
    questions_dict = questions.get_random_questions()

    for question_number, question_info in questions_dict.items():
        # Setze den Timer und Score für jede Frage zurück
        timer.seconds = 0
        timer.score = 10

        question = question_info['question']
        answers = question_info['possible_answers']
        category = question_info['category']

        print(f'\nFrage {question_number} ({category}): {question}')
        for i, answer in enumerate(answers, start=1):
            print(f'{i}. {answer}')

        user_answer = input('Antwort eingeben (1-4): ')

        # Timer und Score anzeigen, während die Antwort eingegeben wird
        timer.display_timer()

        # Berechne die Gesamtpunktzahl nach jeder Frage
        timer.calculate_total_score()

    # Timer am Ende des gesamten Quiz anzeigen
    timer.display_timer()
    print(f'\nGesamtpunktzahl: {timer.total_score}')
    print(f'Gesamtzeit: {timer.get_total_time_formatted()}')

if __name__ == '__main__':
    score_timer = ScoreTimer()
    score_timer.start_timer()

    try:
        start_quiz(score_timer)
    finally:
        score_timer.stop_timer()
