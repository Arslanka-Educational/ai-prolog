%facts

% --games
game(minecraft).
game(csgo).
game(dota2).
game(fortnite).
game(gta).

% --teams
team(navi).
team(virtus_pro).
team(g2).
team(gambit).
team(og).
team(team_liquid).

% --country
country(russia).
country(ukraine).
country(germany).
country(netherlands).

% --continent
continent(asia).
continent(africa).
continent(north_america).
continent(south_america).
continent(antarctica).
continent(europe).
continent(australia).

%predicate
% --developers
% developer(X, Y) <-> X is developer of the game Y
developer(mojang, minecraft).
developer(valve, csgo).
developer(valve, dota2).
developer(epic_games, fortnite).
developer(rockstar, gta).

% --genres
% genre(X, Y) <-> X is genre of the game Y
genre(sandbox, minecraft).
genre(shooter, csgo).
genre(shooter, gta5).
genre(moba, dota2).
genre(survival, fortnite).

% --game_to_play
% game_to_play(X, Y) <-> team X is playing the game Y
game_to_play(navi, csgo).
game_to_play(navi, dota2).
game_to_play(virtus_pro, csgo).
game_to_play(virtus_pro, dota2).
game_to_play(virtus_pro, fortnite).
game_to_play(gambit, csgo).
game_to_play(og, minecraft).

% --country_of
% country_of(X, Y) <-> X is continent where the Y country is located
country_of(europe, russia).
country_of(asia, russia).
country_of(europe, ukraine).
country_of(europe, germany).
country_of(europe, netherlands).

% --team_was_found
% team_was_found(X, Y) <-> X is country where the Y team was found
team_was_found(ukraine, navi).
team_was_found(russia, virtus_pro).
team_was_found(netherlands, og).
team_was_found(russia, gambit).
team_was_found(russia, g2).
team_was_found(germany, team_liquid).


%rules
game_oponents(X, Y) :- X \= Y, game_to_play(X, Z), game_to_play(Y, Z).
same_country_teams(X, Y) :- X \= Y, team_was_found(Z, X), team_was_found(Z, Y).
same_country_game_oponents(X, Y) :- game_oponents(X, Y), same_country_teams(X, Y).
same_continent_teams(X, Y) :- X \=Y, team_was_found(A, X), team_was_found(B, Y), country_of(W, A), country_of(W, B).
same_continent_game_oponents(X, Y) :- game_oponents(X, Y), same_continent_teams(X, Y).


%test
% developer(valve, X).
% country_of(X, russia).
% game_to_play(gta, _).
% team_was_found(X, Y), country_of(europe, X).
% game_oponents(og, og).
% same_country_game_oponents(gambit, virtus_pro).
% same_country_game_oponents(og, g2).