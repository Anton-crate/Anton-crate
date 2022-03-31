from flask import Flask, request, render_template
import os


app = Flask(__name__, template_folder="C:/Users/Администратор/Desktop/Web-site/template")


@app.route("/")
def index():
	name = request.args.get("name")
	message = request.args.get("message")
	if name == None or name == " " or name == "":
		name = "Незнакомец"
	text = "Hello, " + name + "!" + "\n"
	if message == None or message == "" or message == " ":
		message = "Сообщение не введено!"
	return render_template("index.html", name = name, message = message)


if __name__ == "__main__":
	app.run(debug=True)
