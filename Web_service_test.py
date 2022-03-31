from flask import Flask, request, jsonify, render_template
import os



app = Flask(__name__) #, template_folder="C:/Users/Администратор/Desktop/Новая папка")

@app.route("/")
def index():
	name = request.args.get("name")
	message = request.args.get("message")
	if name == None or name == " " or name == "":
		name = "Незнакомец"
	text = "Hello, " + name + "!" + "\n"
	if message == None or message == "" or message == " ":
		message = "Сообщение не введено!"
	text = text + message
	return text

	#Shabl = text

	#with open("C:/Users/Администратор/Desktop/Новая папка/github/index.html", "w") as file:
	#	file.write(html)



#os.startfile("C:/Users/Администратор/Desktop/Новая папка/index.html")

app.run(host="0.0.0.0", port =5000, debug=True)