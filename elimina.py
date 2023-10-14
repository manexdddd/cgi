#!C:\Python311/python.exe

import os
import mysql.connector
import cgi
import cgitb

cgitb.enable()
print("Content-type: text/html\n")
print()

metodo = os.environ["REQUEST_METHOD"]

if(metodo == "POST"):
    datos = cgi.FieldStorage()
    e = datos.getvalue("email")
    
    con = mysql.connector.connect(user='root',password='', host='127.0.0.1', database='foro')
    cursor =  con.cursor()
    sql = f"DELETE from users  WHERE email='{e}'"
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h2>Usuario eliminado</h2>")
else:
    print("<h2>Metodo no permitido</h2>")