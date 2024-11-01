from preloaded import print_table

def build_matches_table(num_teams: int) -> list[list[tuple[int, int]]]:
    if num_teams % 2 == 0:
        teams = list(range(1, num_teams + 1))
        schedule = []

        
        for round_index in range(num_teams - 1):
            matchups = []

            
            for i in range(num_teams // 2):
                match = (teams[i], teams[num_teams - 1 - i])
                matchups.append(match)

            schedule.append(matchups)

          
            teams = [teams[0]] + teams[-1:] + teams[1:-1]
        
        print_table(schedule)
        return schedule
