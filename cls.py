class VotingSystem:
    def __init__(self):
        self.teams = ['Team A', 'Team B', 'Team C', 'Team D']
        self.votes = {}
    def display_teams(self):
        print("Voting Options:")
        for i, team in enumerate(self.teams, start=1):
            print(f"{i}. {team}")
    def vote(self, person):
        while True:
            try:
                self.display_teams()
                vote_choice = int(input(f"{person}, enter the number of your chosen team: "))
                if 1 <= vote_choice <= len(self.teams):
                    team_name = self.teams[vote_choice - 1]
                    self.votes[person] = team_name
                    print(f"{person} voted for {team_name}.")
                    break
                else:
                    print("Invalid choice. Please select a valid team number.")
            except ValueError:
                print("Invalid input. Please enter a valid team number.")
    def run_election(self):
        print("Welcome to the Election Voting System!")
        print("Please cast your votes:")
        for i in range(1, 10):
            person = f'Person {i}'
            self.vote(person)
        print("n\nVoting Results: ")
        for person, voted_team in self.votes.items():
            print(f'{person} voted for {voted_team}.')
        team_votes = {team: 0 for team in self.teams}
        for voted_team in self.votes.values():
            team_votes[voted_team] += 1
        print("\nOverall Election Results:")
        for team, votes in team_votes.items():
            print(f'{team}: {votes} votes')
        winning_team = max(team_votes, key=team_votes.get)
        print(f"\n{winning_team} wins the election with {team_votes[winning_team]} votes!")
        print("\nVotes:")
        for person, voted_team in self.votes.items():
            print(f'{person} voted for {voted_team}.')
if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.run_election()
