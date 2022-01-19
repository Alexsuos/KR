class Status():
    def __init__(self):
        "Инициализирует статистику"
        self.reset_status()
        self.run_game=True
        with open('record.txt','r')as f:
            self.high_score = int(f.readline())

    def reset_status(self):
        """статистика изменяющая во время игры"""
        self.ship_life=2
        self.score=0