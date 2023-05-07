import requests
import json

# Nederlanse Eredivisie
current_league = '4337'

# PSV Eindhoven
team_home = '133768'
team_away = '134304'


last_events_home_api_url = "https://www.thesportsdb.com/api/v1/json/2/eventslast.php?id=" + team_home
response = requests.get(last_events_home_api_url)
last_events_home_data = response.json()


points = 0

for i in range(len(last_events_home_data['results'])):
    last_event_league = last_events_home_data['results'][i]['idLeague']
    last_event_league_name = last_events_home_data['results'][i]['strLeague']
    last_event_name = last_events_home_data['results'][i]['strEvent']
    last_event_result_home = last_events_home_data['results'][i]['intHomeScore']
    last_event_result_away = last_events_home_data['results'][i]['intAwayScore']
    if last_event_result_home > last_event_result_away:
        points += 1
    if last_event_result_home < last_event_result_away:
        points -= 1
    print(last_event_league_name, ' : ', last_event_name, ' : ', last_event_result_home, ' - ', last_event_result_away)

print(points)
print()

points_home = points

points = 0

last_events_home_api_url = "https://www.thesportsdb.com/api/v1/json/2/eventslast.php?id=" + team_away
response = requests.get(last_events_home_api_url)
last_events_home_data = response.json()

for i in range(len(last_events_home_data['results'])):
    last_event_league = last_events_home_data['results'][i]['idLeague']
    last_event_league_name = last_events_home_data['results'][i]['strLeague']
    last_event_name = last_events_home_data['results'][i]['strEvent']
    last_event_result_home = last_events_home_data['results'][i]['intHomeScore']
    last_event_result_away = last_events_home_data['results'][i]['intAwayScore']
    if last_event_result_home > last_event_result_away:
        points += 1
    if last_event_result_home < last_event_result_away:
        points -= 1
    print(last_event_league_name, ' : ', last_event_name, ' : ', last_event_result_home, ' - ', last_event_result_away)

print(points)

points_away = points
