import requests
import json

# API key at https://api.the-odds-api.com/
API_KEY = '52576c8ba030b51aa2ba72fa57fecb4c'

SPORT = 'soccer_fifa_world_cup' # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

# [{"key":"soccer_fifa_world_cup","group":"Soccer","title":"FIFA World Cup","description":"FIFA World Cup 2022","active":"True","has_outrights":"False"},{"key":"soccer_fifa_world_cup_winner","group":"Soccer","title":"FIFA World Cup Winner","description":"FIFA World Cup Winner 2022","active":"True","has_outrights":"True"},{"key":"soccer_netherlands_eredivisie","group":"Soccer","title":"Dutch Eredivisie","description":"Dutch Soccer","active":"True","has_outrights":"False"}]

REGIONS = 'us,uk,eu' # uk | us | eu | au. Multiple can be specified if comma delimited

MARKETS = 'h2h' # h2h | spreads | totals. Multiple can be specified if comma delimited

ODDS_FORMAT = 'decimal' # decimal | american

DATE_FORMAT = 'iso' # iso | unix

BOOKMAKERS = 'williamhill' # https://the-odds-api.com/sports-odds-data/bookmaker-apis.html#us-bookmakers


# The usage quota cost = [number of markets specified] x [number of regions specified]
# For examples of usage quota costs, see https://the-odds-api.com/liveapi/guides/v4/#usage-quota-costs

def scrap_odds():

    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
        #    'bookmakers': BOOKMAKERS,
        }
    )

    if odds_response.status_code != 200:
        print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')

    else:
        # Check the usage quota
        print('Remaining requests', odds_response.headers['x-requests-remaining'])
        print('Used requests', odds_response.headers['x-requests-used'])

        # Export to txt
        odds_json = odds_response.json()
        data = json.dumps(odds_json)
        with open('dump.txt', 'w') as f:
            f.write(data)
        print(' Exported to dump.txt')



def import_odds():
    with open('dump.txt') as f:
        lines = f.read()
        odds_json = json.loads(lines)
    return(odds_json)
