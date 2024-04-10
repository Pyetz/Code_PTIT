class Candidate:
    static_id = 0
    def __init__(self, full_name, team_code):
        Candidate.static_id += 1
        self.id = 'C' + str(Candidate.static_id).zfill(3)
        self.full_name = full_name
        self.team_code = team_code

class Team:
    static_id = 0
    def __init__(self, name, school):
        Team.static_id += 1
        self.id = 'Team' + str(Team.static_id).zfill(2)
        self.name = name
        self.school = school

def input_teams():
    num_teams = int(input())
    teams = []
    for _ in range(num_teams):
        name = input()
        school = input()
        teams.append(Team(name, school))

    return teams

def input_candidates():
    num_candidates = int(input())
    candidates = []
    for _ in range(num_candidates):
        full_name = input()
        team_code = input()
        candidates.append(Candidate(full_name, team_code))

    return candidates

def sort_candidates(candidates):
    return sorted(candidates, key=lambda x: x.full_name)

def main():
    teams = input_teams()
    candidates = input_candidates()
    candidates = sort_candidates(candidates)

    for candidate in candidates:
        team = next((team for team in teams if team.id == candidate.team_code), None)
        print(candidate.id, candidate.full_name, team.name, team.school)


main()