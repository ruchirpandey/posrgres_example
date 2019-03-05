import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Book

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
        book=Book(
            month=month,
            date=date,
            event=event
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        holidays=Book.query.all()
        return render_template("list.html",holidays = holidays)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get/<month_>")
def get_by_id(month_):
    try:
        book=Book.query.filter_by(month=month_).first()
        req = request.get_json(silent=True, force=True)
        print("in comin grequest",req)
        action = req['queryResult']['parameters']['Holiday']
        month = req['queryResult']['parameters']['Months']
        response =  """
                Response : {0}
                """.format('Hello Manishaaaaaaaaaa - You inquired Holidays with out Month parameter')
        return jsonify(book.serialize())
        reply = {"fulfillmentText": response,}
        if month != '':

            response =  """
                Response : {0}
                """.format('Hello Kirtiiiiiiiiiiiii You inquired Holidays with Month parameter')
            reply = {
            "fulfillmentText": response,
        }
        
        
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        month=request.form.get('month')
        date=request.form.get('date')
        event=request.form.get('event')
        try:
            book=Book(
                month=month,
                date=date,
                event=event
            )
            db.session.add(book)
            db.session.commit()
            return "Book added. book id={}".format(book.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

if __name__ == '__main__':
    app.run()