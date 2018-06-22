import pymysql
from flask import Flask,  render_template, Response, json

app=Flask(__name__)


def connDB():
    conn=pymysql.connect(host="localhost",
                         user="root",
                         passwd="root",
                         db="text",
                         charset="utf8");
    cur=conn.cursor();
    return (conn,cur);

def exeUpdate(conn,cur,sql):
    sta=cur.execute(sql);
    conn.commit();
    return (sta);

def exeQuery(cur,sql):
    cur.execute(sql);
    return (cur);

def Response_header(content):
    resp=Response(content)
    resp.headers['Access-Control-Allow-Origin']="*"
    return resp

@app.route("/",methods=["GET"])
def index():
    conn, cur = connDB();
    print("输出当前表！");

    try:
        sql1 = "SELECT class FROM note";
        cur.execute(sql1);
        result1 = cur.fetchall();
        print(result1)
    except Exception:
        print("Sorry,失败了呢！");
        print('\n' * 2)
    try:
        n="SELECT COUNT(DISTINCT class) FROM note"
        cur.execute(n);
        a=cur.fetchall();
        c = a[0]
        d=c[0]
        print("班级总数：")
        print(d)
        sql2 = "SELECT score FROM note";
        cur.execute(sql2);
        result2 = cur.fetchall()
        i=0
        list=[]
        for result3 in range(0,d):
          a=result2[i];
          result=a[0]
          i=i+1
          list.append(result)
          print('班级：'+repr(i)+'成绩：'+repr(result))
          print(list)
    except Exception:
        print("Sorry,失败了呢！");
        print('\n' * 2)

    return render_template("index.html",result1=result1,result2=list)

@app.route("/text.class")
def text1():
         conn, cur = connDB();
         print("输出当前表！");
         try:
             sql1 = "SELECT class FROM note";
             cur.execute(sql1);
             result1 = cur.fetchall();
             print(result1)
         except Exception:
             print("Sorry,失败了呢！");
             print('\n' * 2)
         content=json.dumps(result1);
         result1=Response_header(content)
         return result1

@app.route("/text.score")
def text2():
         conn, cur = connDB();
         print("输出当前表！");
         try:
             sql2 = "SELECT score FROM note";
             cur.execute(sql2);
             result2= cur.fetchall();
             print(result2)
         except Exception:
             print("Sorry,失败了呢！");
             print('\n' * 2)
         content = json.dumps(result2);
         result2 = Response_header(content)
         return result2

if __name__ == '__main__':
    app.run(debug=True)