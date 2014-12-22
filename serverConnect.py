"""
serverConnect.py

This python script contains all of the necessary parameters in order to successfully pull information from an SQL database.

Overview of functions:
    executeSQL(uhost,uuser,upassword,udb,sqlstatement)
        Takes the input information and returns the results of the sqlstatement as a list of lists, where each row
        is its own element in a list.
    SQLrun()
        Takes user input and creates a query. The query result is printed.
"""

def executeSQL(uhost,uuser,upassword,udb,sqlstatement):
    import MySQLdb

    db = MySQLdb.connect(host=uhost,
                          user=uuser,
                          passwd=upassword,
                          db=udb)

    cur = db.cursor()

    cur.execute(sqlstatement)
    sqlReturn = []
    for row in cur.fetchall():
        sqlReturn.append(row)

    return sqlReturn

def main():
    print("This program runs an SQL statement and prints the output")
    userName = input("Enter your username: ")
    userPassword = input("Enter your password: ")
    userHost = input("Enter the host for your db: ")
    userDb = input("Enter the Db you want to query: ")
    userStatement = input("Enter your SQL Statement: ")
    print()

    sqlReturn = executeSQL(userName,userPassword,userHost,userDb,userStatement)

    for row in sqlReturn:
        print(row)

if __name__ == "__main__":
    main()

