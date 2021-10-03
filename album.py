import dbsConnection


def album_func():
    conn, cursor = dbsConnection.main_function()
    try:

        singer = input("Enter singer name: ")
        song = input("Enter song name: ")
        album_name = input("Enter album name: ")
        producer = input("Enter name of producer: ")
        company = input("Enter the name of company: ")
        sold = input("Enter the number of copies sold: ")
        price = input("Enter the price of album: ")

        cursor.execute("INSERT INTO Album_Details (Song,Artist,Producer,Album_Name,Company,Copies_Sold,"
                       "Price_per_album) VALUES (?,?,?,?,?,?,?)",
                       (song, singer, producer, album_name, company, sold, price))
        conn.commit()
        print("Your data has been inserted successfully.")
    except Exception as e:
        print(e)
        print("You are unsuccessful to insert data into the database.")