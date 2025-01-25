from flask import Flask,render_template,redirect,request,session,send_file,after_this_request
import json
import random
import bba
import b1
import os


UPLOAD_FOLDER = "uploads"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()_-+=:;<,..{[}]|\}?"

# defining the flask app
app = Flask(__name__)
app.secret_key = "PIGmanGOOOhahah"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER






# app routes
@app.route("/",methods=['GET','POST'])
def index():
	if request.method == "GET":
		return render_template("index.html")
	else:
		file = request.files['file']

		filename = file.filename

		file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)

		file.save(file_path)

		session['filename'] = filename


		return redirect("/")

@app.route("/cryptography",methods=['POST'])
def cryp():
	if request.method == "POST":
		msg = request.form.get("string")
		action = request.form.get("action")

		

		try:
			if action == "enc":
				cryp = bba.FileDict(f"/{app.config['UPLOAD_FOLDER']}/{session['filename']}")

				cryp_dict = cryp.returnWholeDict()


				enc_str = b1.b1.encrypt(cryp_dict,msg)
				return render_template("index.html",msg=enc_str,msgType="is-success")
			else:
				cryp = bba.FileDict(f"/{app.config['UPLOAD_FOLDER']}/{session['filename']}")


				cryp_dict = cryp.returnWholeDict()
				dec_dict = b1.b1.gen_dec_dict(cryp_dict)
				try:
					dec_str = b1.b1.decrypt(cryp_dict,dec_dict,msg)
					return render_template("index.html",msg=dec_str,msgType="is-success")
				except Exception as e:
					return render_template("index.html",msg="Failed to decrypt",msgType="is-danger")
		except Exception as e:
			return render_template("index.html",msg="No Key was added",msgType="is-warning")
			
@app.route("/gen-key",methods=['GET','POST'])
def gen_key():
	if request.method == "POST":
		key = int(request.form.get("key"))
		size = int(request.form.get("size"))

		bit_code = b1.b1.gen_bit_code(size=size,gen_file=False)
		number = b1.b1.gen_number(bit_code,key)
		cryp_dict = b1.b1.gen_crypt_dict(number)
		enc_dict = cryp_dict[0]

		with open("./uploads/sample.bba","w") as f:
			json_data = json.dump(enc_dict,f)

		@after_this_request
		def cleanup(response):
			try:
				if os.path.exists("./uploads/sample.bba"):
					os.remove("./uploads/sample.bba")
			except Exception as e:
				print(e)
			return response
		

		return send_file("./uploads/sample.bba",as_attachment=True,download_name="key.bba")

@app.route("/clear-session",methods=['GET'])
def clearSession():

	try:
		if os.path.exists(f"./uploads/{session['filename']}"):
			os.remove(f"./uploads/{session['filename']}")
	except Exception as e:
		print(e)

	session.pop("filename",None)
	return redirect("/")

# running the app
if __name__ == "__main__":
	app.run(debug=True)
