# Gaming Leaderboard System
import sys

class Player:
    def __init__(self, username, game_title, level, scores):
        self.username = username
        self.game_title = game_title
        self.level = level
        self.scores = scores
        self.average = self.calculate_average()
        self.rank = self.assign_rank()

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def assign_rank(self):
        avg = self.average
        if 900 <= avg <= 1000:
            return "Legend"
        elif 700 <= avg < 900:
            return "Pro"
        elif 500 <= avg < 700:
            return "Intermediate"
        elif 300 <= avg < 500:
            return "Beginner"
        else:
            return "Noob"

    def display_info(self):
        print("\n--- Player Leaderboard Entry ---")
        print(f"Username: {self.username}")
        print(f"Game Title: {self.game_title}")
        print(f"Level: {self.level}")
        print(f"Scores: {self.scores}")
        print(f"Average Score: {self.average:.2f}")
        print(f"Rank Badge: {self.rank}")


# Example usage
if __name__ == "__main__":
    username = "Shamith"
    game_title = "Valorant"
    level = 99

    # Try to parse scores from command-line arguments
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            # Ignore non-numeric args (like pytest flags)
            pass

    # If no scores passed, fall back to interactive input
    if not scores:
        print("Enter scores for 3 matches:")
        for i in range(3):
            score = int(input(f"Match {i+1} score: "))
            scores.append(score)

    # Create player object
    player = Player(username, game_title, level, scores)

    # Display leaderboard entry
    player.display_info()
