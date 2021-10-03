import pyodbc


def main_function():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=RAHUL\SQLEXPRESS;'
                          'Database=UserData;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    return conn, cursor
