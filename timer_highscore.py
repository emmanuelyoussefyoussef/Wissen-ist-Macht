import time
import threading
from questions_folder.questions import *

# Klasse für Timer und Score
class ScoreTimer:
    def __init__(self):
        # Initialisierung der Variablen
        self.seconds = 0
        self.score = 10
        self.total_score = 0 #Gesamtscore
        self.total_time = 0  # Gesamtzeit 
        self.running = False # Stoppt Timer
        self.timer_thread = None

    # Starten des Timers
    def start_timer(self):
        self.running = True
        self.timer_thread = threading.Thread(target=self._timer_thread)
        self.timer_thread.start()

    # Thread-Funktion für den Timer
    def _timer_thread(self):
        while self.running:
            self.update_score()
            time.sleep(1)
            self.seconds += 1
            self.total_time += 1

    # Stoppen des Timers
    def stop_timer(self):
        self.running = False
        self.timer_thread.join()

    # Aktualisieren des Scores
    def update_score(self):
        if self.seconds >= 10 and self.seconds % 2 == 0 and self.score > 1:
            self.score -= 1

    # Anzeigen des Timers und des Scores
    def display_timer(self):
        hours, remainder = divmod(self.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f'Time: {hours:02}:{minutes:02}:{seconds:02} | Score: {self.score:02}', end='\r')

    # Berechnung des Gesamtscores
    def calculate_total_score(self):
        self.total_score += self.score

    # Abrufen der Gesamtzeit
    def get_total_time(self):
        return self.total_time

    # Abrufen formatierter Gesamtzeit
    def get_total_time_formatted(self):
        hours, remainder = divmod(self.total_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{hours:02}:{minutes:02}:{seconds:02}'

# Funktion zum Starten des Quiz
def start_quiz(timer):
    questions_dict = questions.get_random_questions()

    for question_number, question_info in questions_dict.items():
        # Setzt den Timer und Score für jede Frage zurück
        timer.seconds = 0
        timer.score = 10

        question = question_info['question']
        answers = question_info['possible_answers']
        category = question_info['current_category']

        # Zeigt die Frage und mögliche Antworten an
        print(f'\nFrage {question_number} ({category}): {question}')
        for i, answer in enumerate(answers, start=1):
            print(f'{i}. {answer}')

        # Eingabe für die Antwort
        user_answer = input('Antwort eingeben (1-4): ')

        # Timer und Score anzeigen, während die Antwort eingegeben wird
        timer.display_timer()

        # Berechnet den Gesamtscore nach jeder Frage
        timer.calculate_total_score()

    # Zeigt den Timer am Ende des gesamten Quiz an
    timer.display_timer()
    print(f'\nGesamtpunktzahl: {timer.total_score}')
    print(f'Gesamtzeit: {timer.get_total_time_formatted()}')

# Hauptprogramm
if __name__ == '__main__':
    # Erstellt Instanz des ScoreTimers
    score_timer = ScoreTimer()

    # Startet den Timer
    score_timer.start_timer()

    # Startet das Quiz
    start_quiz(score_timer)

    # Stoppt den Timer
    score_timer.stop_timer()
