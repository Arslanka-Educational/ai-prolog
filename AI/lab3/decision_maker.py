from pyswip import Prolog

prolog = Prolog()
prolog.consult("./lab1.pl")


def query(msg: str) -> bool:
    return list(prolog.query(msg))


def validate_game(game: str):
    if not query(f"game({game})"):
        print("There is no game named", game)
        exit()

def validate_team_playing_game(team: str, game: str):
    if not query(f"team({team})"):
        print("There is no team named", team)
        exit()

    validate_game(game)

    if not prolog.query(f"game_to_play({team}, {game}"):
        print("There is no team named:", team, ", playing game:", game)
        exit()


def get_available_developers_of_game(game: str):
    developers = []
    for el in prolog.query(f"is_developer_of_game(Developer, {game})"):
        developers.append(el['Developer'])
    return developers

def get_available_genres_of_game(game: str):
    genres = []
    for el in prolog.query(f"is_genre_of_game(Genre, {game})"):
        genres.append(el['Genre'])
    return genres

def get_available_teams_playing_game(game: str):
    teams = []
    for el in prolog.query(f"game_to_play(Team, {game})"):
        teams.append(el['Team'])
    return teams

def get_available_countries_team_from(team: str):
    countries = []
    for el in prolog.query(f"team_was_found(Country, {team})"):
        countries.append(el['Country'])
    return countries

def get_available_continents_team_from(countries: list):
    continents = []
    for country in countries:
        for el in prolog.query(f"country_of(Continent, {country})"):
            continents.append(el['Continent'])
    return continents

def get_team_game_opponents(team: str):
    opponents = []
    for opponent in query(f"team(Opponent)"):
        if list(prolog.query(f"game_oponents({opponent['Opponent']}, {team})")):
            opponents.append(opponent['Opponent'])
    return opponents

def get_team_same_continent_game_opponents(team: str):
    opponents = []
    for opponent in query(f"team(Opponent)"):
        if list(prolog.query(f"same_continent_game_oponents({opponent['Opponent']}, {team})")):
            opponents.append(opponent['Opponent'])
    return opponents

print("Input game you have: ", end="")
game = input().strip()
validate_game(game)

developers = get_available_developers_of_game(game)
print("Your game was developer by companies:", ', '.join(developers))

genres = get_available_genres_of_game(game)
print("Your game has following genres:", ', '.join(genres))

teams = get_available_teams_playing_game(game)
print("Your game is played with following teams:", ', '.join(teams))

print("Input team playing game:", game)
team = input().strip()
validate_team_playing_game(team, game)
print("Great! You've chosen game:", game, "and team:", team)

countries = get_available_countries_team_from(team)
print("Your team was found in following countries:", ', '.join(countries))

continents = get_available_continents_team_from(countries)
print("Your countries are located in following continents:", ', '.join(continents))

game_oponents = get_team_game_opponents(team)
print("Your team has following game opponents:", ', '.join(game_oponents))

same_continent_game_oponents = get_team_same_continent_game_opponents(team)
print("Your team has following same continent game opponents:", ', '.join(same_continent_game_oponents))

