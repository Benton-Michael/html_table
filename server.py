from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [

        {'first_name' : 'Michael', 'last_name' : 'Benton'},
        {'first_name' : 'Benny', 'last_name' : 'Benjamin'},
        {'first_name' : 'Tony', 'last_name' : 'Williams'},
        {'first_name' : 'Elvin', 'last_name' : 'Jones'},
        {'first_name' : 'Earl', 'last_name' : 'Palmer'},
    ]
    return render_template("index.html", users=users)

if __name__ =="__main__":
    app.run(debug=True)
