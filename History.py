import dbsConnection
from tabulate import tabulate

def history_func():
    conn, cursor = dbsConnection.main_function()
    myresult = cursor.execute("select * from albumhistory")
    print(tabulate(myresult, headers=['id','User_name', 'Email', 'Date'], tablefmt='psql'))
