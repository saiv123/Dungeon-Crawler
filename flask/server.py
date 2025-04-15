from flask import Flask, request, jsonify
import pydoc

#!###################################################################################
#!###################### Move this to where the SQL server is #######################
#!###################################################################################

#this Flask server is going to used as a layer between the sql server and any requests to it
app = Flask(__name__)
#here the Connection to the sql server is going to be established
#Then the connecter will be passed down to otehr files that require it

#!NEED TO CHANGE TO GRAB INFO FROM ENV VARIABLES
server = "192.168.0.0.0" #this might need to be changed dude to the it being a local connection
database = "temp dbname"
username = "temp username"
password = "temp password"


#creating the connection
connString =f"driver={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
conn = pydoc.connect(connString)

#TODO create checks to see if the tables and columns exist in the database

######API GET METHODS######
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    #TODO - need to change schema to add a table for tracking infor like number of monsters killed and number of dungeons completed
    #implement
    return None

@app.route('/GetPlayer', methods=['GET'])
def get_player():
    DiscordID = request.args.get('DiscordID')
    #implement - this will return the players stats and equipped items ONLY
    return None

@app.route('/GetPlayerInventory', methods=['GET'])
def get_player_inventory():
    DiscordID = request.args.get('DiscordID')
    #implement - this will return the players inventory ONLY
    return None

@app.route('/GetequipedItems', methods=['GET'])
def get_equipped_items():
    DiscordID = request.args.get('DiscordID')
    #implement - this will return the players equipped items ONLY
    return None

######API POST METHODS######
@app.route('/updateInventory', methods=['POST'])
def update_inventory():
    DiscordID = request.args.get('DiscordID')
    itemID = request.args.get('itemID')
    action = request.args.get('action')
    #implement - this will update the players inventory with the new items
    return None

@app.route('/equip', methods=['POST'])
def equip_item():
    DiscordID = request.args.get('DiscordID')
    itemID = request.args.get('itemID')
    slot = request.args.get('slot')
    #implement - this will equip the item to the player
    return None

