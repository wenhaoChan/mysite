from django.shortcuts import render_to_response
import pymysql

# Create your views here.

def coon_hello(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='python_db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    res = 'hello world'
    for r in cur.fetchall():
        print(r)
    conn.close()
    return render_to_response('index/index.html', {'res': res})