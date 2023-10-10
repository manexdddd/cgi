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

    e = cgi.FieldStorage().getvalue("email")
    p = cgi.FieldStorage().getvalue("password")
    n = cgi.FieldStorage().getvalue("name")
    a = cgi.FieldStorage().getvalue("avatar")
    r = cgi.FieldStorage().getvalue("role")
    con = mysql.connector.connect(user='root',password='', host='127.0.0.1', database='foro')
    cursor =  con.cursor()
    sql = "INSERT INTO users VALUES ('{}','{}','{}','{}','{}')".format(e,p,n,a,r)
    cursor.execute(sql)
    con.commit()
    con.close()
    print("<h2>Usuario Agregado</h2>")
else:
    print("<h2>Metodo no permitido</h2>")