import time

class ScoreTimer:
    def __init__(self):
        self.seconds = 0
        self.score = 10

    def start_timer(self):

            while True:
                self.update_score()
                self.display_timer()
                time.sleep(1)
                self.seconds += 1


    def update_score(self):
        if self.seconds >= 10 and self.seconds % 2 == 0:
            if self.score > 1:
                self.score -= 1

    def display_timer(self):
        hours, remainder = divmod(self.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f'Time: {hours:02}:{minutes:02}:{seconds:02} | Score: {self.score:02}', end='\r')

if __name__ == "__main__":
    score_timer = ScoreTimer()
    score_timer.start_timer()
