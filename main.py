from flask import Flask,render_template,request,redirect,url_for,session
import pymysql


app=Flask(__name__)
app.secret_key='fghjhkrgfjkj' # required for session
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",          # put your password here if any
        database="hr_erp_db",
        #cursorclass=pymysql.cursors.DictCursor  -- If we include this line, it will return result in dict form else it will return tuple
    )
# for mysql ,flask-mysqldb
#app.secret_key='fghjhkrgfjkj'
#app.config['MYSQL_HOST']="localhost"
#app.config['MYSQL_USER']="root"
#app.config['MYSQL_PASSWORD']=""
#app.config['MYSQL_DB']='hr_erp_db'

#temp=1 for all employee, temp=2 for specific employee

@app.route('/') #main page or home page of company
def mainpage():
    return render_template("index.html")

@app.route('/about') #about page of company
def aboutpage():
    return render_template("about.html")

@app.route('/admin') #admin page of company
def adminpage():
    return render_template("admin.html")

@app.route('/adminhome',methods=['post','get']) #adminhome page of admin
def adminhomepage():
    if request.method=="POST":  #logout=Yes
        admin_name=request.form["nameadmin"]
        admin_pass=request.form["passadmin"]
        if admin_name=="Pallavi Gaikwad" and admin_pass=='admin':
            session["admin_name"]=admin_name # save for future pages
            return render_template("adminhome.html",admin_name=admin_name)
        else:
            message="Invalid Username or Password"
            return render_template("admin.html",message=message)
    else:           #logout=No
        admin_name=session.get("admin_name")
        return render_template("adminhome.html",admin_name=admin_name)

@app.route('/addemp') #add employee page of adimn
def addemppage():
    admin_name=session.get("admin_name")
    return render_template("addemp.html",admin_name=admin_name)

@app.route('/save',methods=['post']) #to save the added employee of company
def savepage():
    print("POST received:", request.form)
    if request.method=='POST':
        print("POST received:", request.form)
        empid=request.form['empid']
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        department=request.form['department']
        joining_date=request.form['joining_date']
        salary=request.form['salary']

        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute('insert into employee(empid,full_name,email,phone,department,joining_date,salary) ' \
        'values (%s,%s,%s,%s,%s,%s,%s)',(empid,name,email,phone,department,joining_date,salary))
        conn.commit()
        cur.close()
        conn.close()
        temp=2 #to show added employee only
        return redirect(url_for("showemppage",temp=temp,empid=empid))
    return render_template("addemp.html")

@app.route('/showemp')
def showemppage(temp=1,empid=0):
    admin_name=session.get("admin_name")
    temp = request.args.get('temp', default=1, type=int)
    empid = request.args.get('empid', default=0, type=int)
    if temp==1: #to show all employee
        print("if",temp,empid)
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute('select * from employee')
        employees=cur.fetchall()
        cur.close()
        conn.close()
        return render_template("showemp.html",employees=employees,temp=temp,admin_name=admin_name)
    else:       #to show specific employee
        print("else",temp,empid)
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute('select * from employee where empid=%s',(empid))
        employee_1=cur.fetchall()
        cur.close()
        conn.close()
        return render_template("showemp.html",employee_1=employee_1,temp=temp,admin_name=admin_name)

@app.route('/profile') #to show specific employee details to update /delete page of admin
def profilepage():
        admin_name=session.get("admin_name")
        id=request.args.get('empid')
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute('select * from employee where empid='+id)
        employee_1=cur.fetchall()
        cur.close()
        conn.close()
        return render_template("profile.html",employee_1=employee_1,admin_name=admin_name)

@app.route('/searchemp') #search employee page of admin
def searchemppage():
    admin_name=session.get("admin_name")
    return render_template("searchemp.html",admin_name=admin_name)

@app.route('/updateemp',methods=['POST']) #update employee page of admin
def updateemppage():
    action=request.form['action']
    if action=="update":
        empid=request.form['empid']
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        department=request.form['department']
        joining_date=request.form['joining_date']
        salary=request.form['salary']
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute('update employee set ' \
        'empid=%s,full_name=%s,email=%s,phone=%s,department=%s,joining_date=%s,salary=%s where empid=%s',
        (empid,name,email,phone,department,joining_date,salary,empid))
        conn.commit()
        cur.close()
        conn.close()
        temp=2
        return redirect(url_for("showemppage",temp=temp,empid=empid))
    else:
        empid=request.form['empid']
        conn=get_db_connection()
        cur=conn.cursor()
        cur.execute('delete from employee where empid=%s',(empid))
        conn.commit()
        cur.close()
        conn.close()
        temp=1
        return redirect(url_for("showemppage",temp=temp,empid=empid))

@app.route('/adminlogout')
def adminlogoutpage():
    return render_template("adminlogout.html")

@app.route('/logout')
def logoutpage():
    session.clear()
    return render_template("admin.html")


if __name__=="__main__":
 app.run(debug=True)