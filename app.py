import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Holiday

#from models import Holiday

@app.route("/")
def hello():
    return "Hello !"

@app.route("/add")
def add_holiday():
    month=request.args.get('month')
    date=request.args.get('date')
    event=request.args.get('event')
    try:
        holiday=Holiday(
            month=month,
            date=date,
            event=event
        )
        db.session.add(holiday)
        db.session.commit()
        return "Holiday added. holiday id={}".format(holiday.id)
    except Exception as e:
	    return(str(e))
        
@app.route("/getall")
def get_all():
    try:
        
        holidays=Holiday.query.all()
        return render_template("list.html",holidays = holidays)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get",methods=['GET', 'POST'] )
def get_by_id():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['parameters']['function']
    month = req['queryResult']['parameters']['Months']
    print("action is", action)
    print("month is", month)
    try: 
        if action=='Holiday':
            holiday=Holiday.query.filter_by(month=month).first()
            

            print("print rows", holiday)
            
            

            print("Month is",holiday.month)
            print("Date is",holiday.date)
            print("Event is",holiday.event)


    
            response =  """
                    id : {0}
                    month: {1}
                    date: {2}
                    event: {3}
                    
                    """.format(holiday.id+ holiday.month+holiday.date +holiday.event)
            reply = {"fulfillmentText": response,}
            return jsonify(reply)
        else:

    
            response =  """
                    Response : {0}
                    """.format("action is not valid")
            reply = {"fulfillmentText": response,}
        #return jsonify(holiday.serialize())
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        month=request.form.get('month')
        date=request.form.get('date')
        event=request.form.get('event')
        try:
            holiday=Holiday(
                month=month,
                date=date,
                event=event
            )
            db.session.add(holiday)
            db.session.commit()
            return "Holiday added. holiday id={}".format(holiday.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

@app.route("/add/studentinfo",methods=['GET', 'POST'])
def add_student_info():
    if request.method == 'POST':
        name=request.form.get('name')
        address=request.form.get('address')
        city=request.form.get('city')
        try:
            table=Student_Info(
                name=name,
                address=address,
                city=city
            )
            db.session.add(table)
            db.session.commit()
            return "Info added. info id={}".format(table.id)
        except Exception as e:
            return(str(e))
    return render_template("studentdata.html")


@app.route("/getdata")

def get_data():

    try:

        All_Holidays=Holiday.query.all()

        All_Students=Student_Info.query.all()

        for row in All_Students:

            print("All Students name -",row.name)

            print("All Students city -",row.city)

        return render_template("list.html",All_Holidays = All_Holidays,All_Students = All_Students)



        #return  jsonify([e.serialize() for e in books])

    except Exception as e:

        return(str(e))





@app.route("/get/<name_>" )

def get_by_name(name_):

    #req = request.get_json(silent=True, force=True)

    #print("in comin grequest",req)

    #action = req['queryResult']['parameters']['Holiday']

    #month = req['queryResult']['parameters']['Months']

    try:

        table=Holiday.query.filter_by(name=name_).first()

        print("print rows", table)

        return (table)

        #return jsonify(table.serialize())

    except Exception as e:

        return(str(e))



if __name__ == '__main__':
    app.run()