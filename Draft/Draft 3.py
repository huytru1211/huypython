import mysql.connector

connection = mysql.connector.connect(
    host= '127.0.0.1',
    port= 3306,
    database= 'people',
    user= 'dbuser',
    password= 'pass_word',
    autocommit=True)
def getemployeesbylastname(last_name):
    sql = "SELECT id, lastname, firstname, salary FROM employees"
    sql = sql + " WHERE lastname='"+ last_name + " '"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result= cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! Im {row[2]} {row[1]}. My salary is {row[3]} euros per month. ")
    return
getemployeesbylastname("Rolola")









