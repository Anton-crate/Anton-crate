from flask import Flask, request, jsonify




app = Flask(__name__)

@app.route("/anton-crate.github.io/Anton-crate/", methods=["GET"])
def re_kruto():
	name = request.args.get("name")
	message = request.args.get("message")
	if name == None or name == " " or name == "":
		name = "Незнакомец"
	text = "Hello, " + name + "!" + "\n"
	if message == None or message == "" or message == " ":
		message = "Сообщение не введено!"
	text = text + message
	print(text)
	return text


if __name__ == "__main__":
	app.run(debug=True)
