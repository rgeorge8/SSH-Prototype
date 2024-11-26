import sqlite3



def get_fridge_contents(): # will pass on user_name

    user_name = "Alice"


    conn = sqlite3.connect("proto5.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT userID FROM Users WHERE name = ?", (user_name,)) # here we have selected Alice as our user
    id_result = cursor.fetchone()

    if not id_result:
        conn.close()
        return f"User {user_name} not found"
        
    user_id = id_result[0]


        # get fridge contents based on the userID retrived above

    cursor.execute("SELECT item FROM Contents WHERE userID = ?", (user_id,))
    fridge_contents =[row[0] for row in cursor.fetchall()]

        
    #print(f"Fridge contents retrieved for userID {user_id}: {fridge_contents}")
    conn.close()

    return ",".join(fridge_contents) if fridge_contents else "No contents in the fridge was found" # api include_ingerdient tags takes a lsit of ingredients in a string separated by commas
