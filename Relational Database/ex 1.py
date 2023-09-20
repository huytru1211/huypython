import mysql.connector
connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def getemployeesbylastname(user):
    sql = "SELECT ident, name, municipality from airport"
    sql = sql + " WHERE ident='"+ user + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Name airport: {row[1]}, Municipality: {row[2]}, ident: {row[0]}")
    return
user= input("Please enter the ICAO code of an airport: ")
getemployeesbylastname(user)


