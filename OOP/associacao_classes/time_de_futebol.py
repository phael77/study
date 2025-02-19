class Player:
    def __init__(self, name: str, position: str, number: int) -> None:
        self.name = name
        self.position = position
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} ({self.position} - Shirt No {self.number})"


class Team:
    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city
        self.players = []

    def add_players(self, player: Player):
        self.players.append(player)

    def list_players(self) -> None:
        print(f"\nPlayers of {self.name} ({self.city})\n")
        for player in self.players:
            print(f"{player}\n")


team_1 = Team("Corinthians", "São Paulo")

player_1 = Player("Depay", "Forward", 10)
player_2 = Player("Garro", "Midfield", 8)
player_3 = Player("Yuri Alberto", "Forward", 9)

team_1.add_players(player_1)
team_1.add_players(player_2)
team_1.add_players(player_3)

team_1.list_players()

