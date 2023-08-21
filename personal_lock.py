import mysql.connector

def sqlinsert(code,text):
    mydb = mysql.connector.connect(
        host="localhost",
        user="#",
        password="#",
        database="#"
)
    mycursor = mydb.cursor()

    sql = "INSERT INTO #table (code, text) VALUES (%s, %s)"
    val = (code, text)
    mycursor.execute(sql, val)

    mydb.commit()
    print("-Your code and file has been successfully stored")

def sqlfindsame(code):
    mydb = mysql.connector.connect(
        host="localhost",
        user="#",
        password="#",
        database="#"
)
    mycursor = mydb.cursor()

    sql = "SELECT * FROM #table WHERE code = %s"
    val = (code,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) != 0:
        pass
        global samecode
        samecode = 0
    else:
        pass
        samecode = 1

def sqlfind(code):
    mydb = mysql.connector.connect(
        host="localhost",
        user="#",
        password="#",
        database="#"
)
    mycursor = mydb.cursor()

    sql = "SELECT * FROM #table WHERE code = %s"
    val = (code,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) != 0:
        for x in myresult:
            y = x[1]
            print("-The message is: " + y)
    else:
        print("***No code found or invalid code number***")
    

while True:
    print("Welcome to the personal lock")
    print("1. Create your lock and text")
    print("2. Retrieve your text")
    print("3. Exit")
    user_input = input("Please select your options: ")
    if (user_input == "1"):
        while True:
            input_code = input("Input your 4 digit code: ")
            try:
                new_input_code = int(input_code)
                sqlfindsame(input_code)
                if samecode == 1:
                    if len(input_code) == 4:
                        print("-You have successfully create a secret code")
                        pass
                    else:
                        print("***Code is not 4 digits***")
                        break
                else:
                    print("***Code is currently in use***")
                    break
            except:
                print("***Code is not in integer.***")
                break
            secret_text = input("Enter your secret text: ")
            sqlinsert(input_code, secret_text)
            break
    elif (user_input == "2"):
        user_code = input("Enter the code for your sercret file: ")
        sqlfind(user_code)
        continue
    elif (user_input == "3"):
        print("Exiting console")
        break
    else:
        print("***Invalid input***")