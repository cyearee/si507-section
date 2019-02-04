from flask import Flask
from sec2_poss_solution import * 

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>COFFEECOFFEECOFFEE</h1>'

joe = Coffee('boring coffee',2.0,3)
@app.route('/cupofjoe/')
def hey_joe():
	return joe.__str__()

@app.route('/cupofjoe/addmilk/<name>/<extra>/<dairy>')
def milk_joe(name,extra,dairy):
	if dairy=="dairy":
		boo_d = True
	elif dairy=="non-dairy":
		boo_d = False
	else:
		return "<h1>Please tell me if this comes from a cow - I'm lactose-intolerant.</h1>"
	milk = Milk(name,boo_d,float(extra))
	joe.add_milk(milk)
	return joe.__str__()


if __name__ == '__main__':
	app.run() 
