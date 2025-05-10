import csv
import os

class Logger:
    def __init__(self, filename="training_log.csv"):
        self.filename = filename
        self.fields = ["Run", "Reward", "Epsilon", "AI Score", "Player Score"]

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fields)
                writer.writeheader()

    def log(self, run, reward, epsilon, ai_score, player_score):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writerow({
                "Run": run,
                "Reward": round(reward, 3),
                "Epsilon": round(epsilon, 4),
                "AI Score": ai_score,
                "Player Score": player_score
            })
