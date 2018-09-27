# !/bin/python
# Mars Team Client Example written in Python
# Requires the following library to install: sudo pip install websocket-client
# if you encounter errors with a Six import:
# you can try: pip remove six; pip install six
# Windows users: you may need to install the Microsoft Visual C++ Compiler for Python 2.7
# Windows users. please use this link: http://aka.ms/vcpython27
import requests
import websocket
import json
import csv
import random
import pickle

# Global Variables
team_name = 'TheShields'  # The Name of the Team
team_auth = ''  # The Team Authentication Token
server_url = 'http://10.207.80.16:8080/api'  # URL of the SERVER API
server_ws = 'ws://10.207.80.16:8080/ws'  # URL of the Sensors Websocket

team_list = 10
max_radiation = 0
min_radiation = 1000
min_temperature = -142
max_temperature = 35

# with open('train_data.csv', 'w') as csvFile:
#     pass  # create the file

# Server Method Calls ------------------------------------------------

team_list = 10
max_radiation = 0
min_radiation = 1000
min_temperature = -142
max_temperature = 35
def register_team(team_name):
    """
    Registers the Team in the Server
    :param team_name:The team name
    :return:The Team authentication Token
    """

    url = server_url + "/join/" + team_name
    print('Server API URL: ' + url)
    payload = ''

    # POST with form-encoded data
    response = requests.post(url, data=payload)

    team_auth = response.text
    # print ('Team Authentication Code:' + team_auth )

    if response.status_code == 200:
        print('Team \'' + team_name + '\' joined the game!')
        print(team_name + ' authentication Code: ' + team_auth)
    else:
        print('Team \'' + team_name + '\' joining game Failed!')
        print("HTTP Code: " + str(response.status_code) + " | Response: " + response.text)

    return team_auth


# Shield Method Calls ------------------------------------------------
def team_shield_up(team_name, team_auth):
    """
    Sets the team shield up
    curl -i -H 'X-Auth-Token: 1335aa6af5d0289f' -X POST http://localhost:8080/api/shield/enable
    :param team_name:The team name
    :param team_auth:The team authentication token
    :return: nothing
    """
    url = server_url + '/shield/enable'
    auth_header = {'X-Auth-Token': team_auth}
    shield_up = requests.post(url, headers=auth_header)
    if shield_up.status_code == 200:
        print('Server: Team: ' + team_name + ' Shield is UP!')
    else:
        print('Server: Team: ' + team_name + ' Shield UP! request Failed!')
        print("HTTP Code: " + str(shield_up.status_code) + " | Response: " + shield_up.text)


def team_shield_down(team_name, team_auth):
    """
    Sets the team shield Down
    curl -i -H 'X-Auth-Token: 1335aa6af5d0289f' -X POST http://localhost:8080/api/shield/disable
    :param team_name:The team name
    :param team_auth:The team authentication token
    :return: nothing
    """
    url = server_url + '/shield/disable'
    auth_header = {'X-Auth-Token': team_auth}
    shield_down = requests.post(url, headers=auth_header)
    if shield_down.status_code == 200:
        print('Server: Team: ' + team_name + ' Shield is DOWN!')
    else:
        print('Server: Team: ' + team_name + ' Shield DOWN! request Failed!')
        print("HTTP Code: " + str(shield_down.status_code) + " | Response: " + shield_down.text)


# Client Logic ------------------------------------------------

def data_recording(parsed_json):
    """
    Saves the Mars sensor data in data repository
    :param parsed_json:Readings from Mars Sensors
    :return:Nothing
    """
    readings = parsed_json['readings']
    solar_flare = readings['solarFlare']
    temperature = readings['temperature']
    radiation = readings['radiation']
    with open('train_data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([solar_flare, temperature, radiation])
    print("\nData Recording: Saving Data row for persistence. Time: " + str(parsed_json['startedAt']))


def team_strategy(parsed_json):
    """
  Contains the Team's strategy.
  :param parsed_json: Readings from the Mars Sensors
  :return:Nothing
  """
    # The Strategy for this client is to have the shield up constantly until it is depleted.
    # Then wait until is charged again to a 10% and enable it again
    teams_list = parsed_json['teams']
    readings = parsed_json['readings']
    for team in teams_list:
        # Register the Team
        if team['energy'] <= 10 and team['life'] >= 50:
            team_shield_down(team_name, team_auth)
        elif team['energy'] <= 10 and team['life'] <= 10:
            x = random.uniform(0, 1)
            if x == 0:
                team_shield_up(team_name, team_auth)
            else:
                team_shield_down(team_name, team_auth)
        elif team['energy'] >= 50 and team['life'] <= 10:
            team_shield_up(team_name, team_auth)
        else:
            if readings['temperature'] > 0 or readings['radiations'] > 700:
                team_shield_up(team_name, team_auth)
            else:
                team_shield_down(team_name, team_auth)

    # teams_list = parsed_json['teams']
    # readings = parsed_json['readings']
    # # Find this team
    # for team in teams_list:
    #     if team['name'] == team_name:
    #         print("\n current temperature: " + str(readings['temperature']) + " current radiation: " + str(
    #             readings['radiation']))
    #         print("\n team shield is: " + str(team['shield']))
    #         if readings['radiation'] >= 700 and team['shield'] != True:
    #             print("shield up, radiation is too high")
    #             team_shield_up(team_name, team_auth)
    #         else:
    #             if readings['radiation'] < 300 and team['life'] > 50:
    #                 print("shield down, radiation is low")
    #                 team_shield_down(team_name, team_auth)
    #             else:
    #                 if team['energy'] > 50:
    #                     print("shield up energy level high")
    #                     team_shield_up(team_name, team_auth)
    #                 else:
    #                     if team['energy'] <= 10:
    #                         print("shield down energy level is too low")
    #                         team_shield_down(team_name, team_auth)
    #             print("\n default case: temperature is: " + str(readings['temperature']) + " radiation is: " + str(
    #                 readings['radiation']))


# Register the Team

team_auth = register_team(team_name)

# Create the WebSocket for Listening
ws = websocket.create_connection(server_ws)

while True:

    json_string = ws.recv()  # Receives the the json information

    # Received '{"running":false,"startedAt":"2015-08-04T00:44:40.854306651Z","readings":{"solarFlare":false,"temperature":-3.
    # 960996217958863,"radiation":872},"teams":[{"name":"TheBorgs","energy":100,"life":0,"shield":false},{"name":"QuickFandang
    # o","energy":100,"life":0,"shield":false},{"name":"InTheBigMessos","energy":32,"life":53,"shield":false},{"name":"MamaMia
    # ","energy":100,"life":100,"shield":false}]}'

    parsed_json = json.loads(json_string)

    # Check if the game has started
    print("Game Status: " + str(parsed_json['running']))

    if not parsed_json['running']:
        print('Waiting for the Game Start')
    else:
        data_recording(parsed_json)
        team_strategy(parsed_json)

ws.close()

print("Good bye!")


    # # Find this tea,./;m
    # for team in teams_list:
    #     if team['name'] == team_name:
    #         with open("tree.pkl", 'rb') as pkl_input:
    #             radiation_ratio = (radiation - min_radiation) / (max_radiation - min_radiation)
    #             temperature_ratio = (temperature - min_temperature) / (max_temperature - min_temperature)
    #             decision_tree = pickle.load(pkl_input)
    #             prediction = decision_tree.predict([radiation_ratio, temperature_ratio])[0]
    #             if prediction == 1:
    #                 team_sheid_up(team_name,team_auth)
    #             elif prediction == 0:
    #                 pass
    #             else:
    #                 raise ValueError("Prediction Value is not known")
    #     else:
    #         with open("k_means_model.pkl", 'rb') as pkl_input:
    #             readings = parsed_json['readings']
    #             temperature = readings['temperature']
    #             radiation = readings['radiation']
    #             radiation_ratio = (radiation - min_radiation) / (max_radiation - min_radiation)
    #             temperature_ratio = (temperature - min_temperature) / (max_temperature - min_temperature)
    #             k_means_model = pickle.load(pkl_input)
    #             prediction = k_means_model.predict([radiation_ratio, temperature_ratio])[0]
    #             if prediction == 1:
    #                 team_sheid_up(team_name,team_auth)
    #             elif prediction == 0:
    #                 pass
    #             else:
    #                 raise ValueError("Prediction value")
