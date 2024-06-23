from dataclasses import dataclass


@dataclass
class Giocatore:
    playerID: str
    name: str
    surname: str
    salary: float

    def __hash__(self):
        return hash(self.playerID)

    def __eq__(self, other):
        return self.playerID == other.playerID

    def __str__(self):
        return f"{self.playerID} - {self.name} {self.surname}"

    def setTeams(self, teams):
        self.teams = teams
