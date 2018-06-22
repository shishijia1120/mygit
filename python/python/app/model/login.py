import pymysql

from flask import Flask, Response, json, request

app=Flask(__name__)

def connDB():
    conn=pymysql.connect(host="localhost", user="root",
                     password="root", db="blog", port=3306)
    cur=conn.cursor()
    return (conn,cur)

def exeUpdate(conn,cur,sql):
    sta=cur.execute(sql)
    conn.commit()
    return (sta)

def exeQuery(cur,sql):
    cur.execute(sql)
    return (cur)

def Response_header(content):
    resp=Response(content)
    resp.headers['Access-Control-Allow-Origin']="*"
    return resp

@app.route("/",methods=["POST"])
def index():

    conn, cur = connDB()
    r=request.json.get("username")
    p=request.json.get("password")
    print(r,p)
    sql = "SELECT password FROM login WHERE username='%s'" % r
    print(sql)
    try:
        cur.execute(sql)
        result = cur.fetchall()
        if result[0][0] == p:
            msg = "登陆成功！"
        else:
            msg = "登陆失败！"

    except Exception:
        msg = "登陆失败！"
    t = {}
    t['data'] = msg
    return json.dumps(t,ensure_ascii=False)


@app.route("/register", methods=["POST"])
def chose():
    conn, cur = connDB()
    r = request.json.get("username")
    p = request.json.get("password")
    sql = "SELECT username FROM login "
    cur.execute(sql)
    result = cur.fetchall()


    if(r not in result):
         i = int(p)
         sql2 = "INSERT INTO login(username, password) VALUES ('%s','%s')" % (r, i)
         print(r)
         try:
             cur.execute(sql2)
             conn.commit()
             msg = "注册成功！"
         except Exception:
                print("注册执行出现错误")
    else:
        msg="用户名已存在"
    print(msg)
    print(result)
    t = {}
    t['data'] = msg
    return json.dumps(t, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True)