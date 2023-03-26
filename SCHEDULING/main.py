from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
from datetime import datetime
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='jayant'
app.config['MYSQL_DB']='rotf'

mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        userdetails=request.form
        table_no=(userdetails["table_no"])
        order_no=(userdetails["order_no"])
        order_id=(userdetails["order_id"])
        cur=mysql.connection.cursor()
        List=["","COFFEE","TEA","RAMEN","WUFFLE","DOSA","PANCAKE","MOMO","CHOLE BHATURE"]
        order_name=List[int(order_id)]
        cur.execute("INSERT INTO ordered(order_no,Table_no,OrderID,OrderName, OrderTime) VALUES (%s,%s,%s,%s,%s)",(order_no,table_no,order_id,order_name,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        cur.execute("INSERT INTO kitchen(order_no,Table_no,OrderID,OrderName, OrderTime) VALUES (%s,%s,%s,%s,%s)",(order_no,table_no,order_id,order_name,datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        mysql.connection.commit()
        cur.close()
        return redirect('/')

    return render_template('form.html')




######## for ordered database
@app.route('/delete',methods=['GET','POST'])
def delete ():
    cur=mysql.connection.cursor()
    r=cur.execute("SELECT * FROM kitchen")
    userdetails=cur.fetchall()              #get all data from kitchen database
    if request.method=='POST':
        userdetails=request.form
        order_no=str(userdetails["order_no"])
        # return order_no
        cur=mysql.connection.cursor()

        r= cur.execute("SELECT * from kitchen WHERE order_no=(%s)",[order_no])
        mysql.connection.commit()
        if r>0:
            r=cur.execute("INSERT INTO scheduled(order_no,Table_no,OrderID,OrderName, OrderTime) SELECT order_no,Table_no,OrderID,OrderName, OrderTime FROM ordered WHERE order_no=(%s) ",([order_no]))
            mysql.connection.commit()
            #################
            r=cur.execute("UPDATE scheduled SET PreparedTime =(%s) WHERE order_no=(%s) ",(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),[order_no]))
            mysql.connection.commit()


            cur.execute("SELECT PreparedTime FROM scheduled")
            OrderedTime=cur.fetchall()
            cur.execute("SELECT order_no FROM scheduled")
            Ordered_no=cur.fetchall()
            for x in range(len(OrderedTime)):
                cur.execute("UPDATE scheduled SET WaitingTime =(%s) WHERE order_no=(%s)",((datetime.now()-OrderedTime[x][0]),Ordered_no[x][0]))

            cur.execute("DELETE FROM kitchen WHERE order_no=(%s)",([order_no]))
            mysql.connection.commit()
            cur.close()
        return redirect('/delete')
        
    return render_template('form2.html',userdetails=userdetails)    # the kitchen data is dispalyed

@app.route('/ordered')
def ordered():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM ordered")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)

@app.route('/kitchen')
def kitchen():
        cur=mysql.connection.cursor()
        r=cur.execute("SELECT * FROM kitchen")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try.html',userdetails=userdetails)

@app.route('/scheduled')
def scheduled():
        cur=mysql.connection.cursor()
        cur.execute("SELECT PreparedTime FROM scheduled")
        OrderedTime=cur.fetchall()
        cur.execute("SELECT order_no FROM scheduled")
        Ordered_no=cur.fetchall()
        for x in range(len(OrderedTime)):
            cur.execute("UPDATE scheduled SET WaitingTime =(%s) WHERE order_no=(%s)",((datetime.now()-OrderedTime[x][0]),Ordered_no[x][0]))
        r=cur.execute("SELECT ROW_NUMBER() OVER(ORDER BY WaitingTime)row_num,Order_no,Table_no,OrderID,OrderName,OrderTime,PreparedTime,WaitingTime  FROM scheduled")
        if r>0:
            userdetails=cur.fetchall()
            return render_template('try1.html',userdetails=userdetails)
        else:
            return render_template('empty.html')



if __name__ == "__main__":
    app.run(debug=True)