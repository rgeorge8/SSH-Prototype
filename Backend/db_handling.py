import sqlite3

def get_fridge_contents(user_id):

    conn = sqlite3.connect("proto5.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM Contents WHERE userID = Alice",(user_id)) # here we have selected Alice as our user
    fridge_contents = [row[0] for row in cursor.fetchall()]

    conn.close()

    return ",".join(fridge_contents) # api include_ingerdient tags takes a lsit of ingredients in a string separated by commas
