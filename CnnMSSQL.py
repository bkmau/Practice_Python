import pyodbc

try:
    cnxn = pyodbc.connect(
        "DRIVER={SQL SERVER};SERVER=localhost\SQLEXPRESS;DATABASE=master;UID=******;PWD=*******"
    )

    cursor = cnxn.cursor()
    if cursor:
        print("lala")
except Exception as e:
    print(e)