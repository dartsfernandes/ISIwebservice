from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return render_template("api-doc.html")	

if __name__ == "__main__":
	app.run()