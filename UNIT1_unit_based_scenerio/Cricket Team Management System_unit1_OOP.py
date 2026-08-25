class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs
        self.category = self.categorize_player()

    def categorize_player(self):
        if self.runs >= 1000:
            return "Excellent"
        elif 500 <= self.runs < 1000:
            return "Good"
        else:
            return "Average"

    def display(self):
        print(f"Jersey #{self.jersey_number:<3} | Name: {self.player_name:<15} | Runs: {self.runs:<5} | Category: {self.category}")


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all_players(self):
        print(f"\n--- {self.team_name} Player Details ---")
        for player in self.players:
            player.display()


# Demonstration / Driver Code
if __name__ == "__main__":
    team = Team("Royal Challengers")
    
    # Adding Player Objects
    team.add_player(Player("Virat Kohli", 18, 1250))
    team.add_player(Player("Faf du Plessis", 13, 730))
    team.add_player(Player("Rajat Patidar", 97, 340))

    # Displaying All Player Records
    team.display_all_players()