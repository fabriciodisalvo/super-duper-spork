import odds_api
import os


def print_hero():
    os.system('cls' if os.name=='nt' else 'clear')
    print()
    print("==================================================================================================================")
    print("======================================== WORLD CUP ODDS - Version 01 =============================================")
    print("==================================================================================================================")
    print()

option_list_main_menu = [" Download Odds (checks Quota first).", " Process downloaded Odds."]

def print_options(option_list):
    print("     Options : ")
    print()
    quantity_of_options = len(option_list)
    indent = ("        ")
    option_line_1 = (indent + "(1) " + str(option_list[0])).ljust(50)
    option_line_2 = (indent + "(2) " + str(option_list[1])).ljust(50)
    print(option_line_1 + option_line_2)
    print()
    chosen_option = input(' Choose entering the number of the item in the menu:  ')
    print()
    print()
    return(chosen_option)



# MAIN MENU
print_hero()
chosen_option = print_options(option_list_main_menu)

if chosen_option == "1":
    print_hero()
    print(" QUOTA Exceded. Importing existing odds...")
    print()
    odds_json = odds_api.import_odds()
    print(" Odds imported.")

elif chosen_option == "2":
    print_hero()
    print("Importing existing odds...")
    print()
    odds_json = odds_api.import_odds()
    print(" Odds imported.")


# ODDS IMPORTED MENU
print_hero()
chosen_option = print_options(["Print Available Odds.","IMPLEMENT SELECTION OF EVENT."])

if chosen_option == "1":
    print_hero()
    number_of_events = len(odds_json)
    print('Number of events:', number_of_events)

    indent = "    "
        
    chosen_option = print_options(["Print All Available Odds.","Print Average Odds."])
    for i in range(min(5, number_of_events)):
        print("=========================================================")
        print(odds_json[i]['sport_title'] + " match id: " + odds_json[i]['id'])
        print(indent, odds_json[i]['home_team'], " - ", odds_json[i]['away_team'])
        print(indent, odds_json[i]['commence_time'])
        print("=========================================================")
        print()
        odds_dict = {}
        for bookmaker in odds_json[i]['bookmakers']:
            # print(indent, bookmaker['title'])
            for market in bookmaker['markets']:
                for outcome in market['outcomes']:
                    if str(outcome['name']) in odds_dict:
                        odds_dict[str(outcome['name'])].append(outcome['price'])
                    else:
                        odds_dict[str(outcome['name'])] = []
                        odds_dict[str(outcome['name'])].append(outcome['price'])
                    # print(indent * 2, outcome['name'], outcome['price'])

        if chosen_option == "1":
            number_of_bookmakers = len(odds_json[i]['bookmakers'])
            print("Available odds:", number_of_bookmakers, "bookmakers.")
            for bookmaker in odds_json[i]['bookmakers']:
                print(indent, bookmaker['title'])
                for market in bookmaker['markets']:
                    for outcome in market['outcomes']:
                        print(indent * 2, outcome['name'], outcome['price'])

        if chosen_option == "2":
                print("Average odds: ")
                for dict_name in odds_dict:
                    average_name = dict_name
                    average_price = round(sum(odds_dict[dict_name])/len(odds_dict[dict_name]),4)
                    print(indent, average_name, average_price)
                print()

elif chosen_option == "2":
    print(" NOT IMPLEMENTED YET.")