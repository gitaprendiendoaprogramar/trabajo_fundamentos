from flask import Flask, render_template, request, redirect, url_for, session, logging
#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker
#from passlib.hash import sha256_crypt
#from pip install passlib import MySQL,MySQLdb
#import bcrypt

# engine = create_engine("mysql+pymysql://root:1234567@localhost/register")
                       #("mysql+pymysql://username:passoword@localhost/databasename)
# bd = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
def Inicio():
    return render_template("inicio.html")

@app.route("/Acercade")
def Acerca():
    return render_template("Acerca.html")

@app.route("/Trilladoras")
def Trilladoras():
    return render_template("Trilladoras.html")

@app.route("/Foro")
def Foro():
    return render_template("Foro.html")

@app.route("/registro", methods = ["GET", "POST"])
def registro():
    # if  request.methods == "POST":
        # name = request.form.get("nombre")
        # username = request.form.get("usuario")
    #   }  password = request.form.get("contraseña")
        # confirm = request.form.get("confirm")
        # secure_password = sha256_crypt.encrypt(str(password))


        # if password == confirm:
            # db.execute("INSERT INTO users(name, username, password) VALUES(:name, :username, :password)",
                                        #  {"name":name, "username":username, "password":secure_password})
            # bb.comimit()
            # return redirect(url_for("login"))
        # else:
            # return render_template("registro.html")
    return render_template("registro.html")



@app.route("/login")
def loginn():
    return render_template("login.html")

if  __name__ == "__main__":
    app.run(debug = True)