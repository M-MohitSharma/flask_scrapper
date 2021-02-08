from flask import Flask, render_template , request
app = Flask("My Application")
import scrapper

USERS = [
    {
    "id" : 1,
    "name": "Sakshi Malhotra"
},
{
    "id" : 2,
    "name" : "Jatin"
},
{
    "id" : 3,
    "name" : "mohit"
}
]

@app.route('/', methods=["GET","POST"])
def index():
    products = []
    if request.method == "POST":
        query = request.form['query']
        products = scrapper.scrap(query)
    return render_template('index.html', products = products)

@app.route('/something/<name>')
def something(name):
    print(type(name))
    return name



@app.route('/users')
def users():
    return render_template('users.html' , users = USERS)


@app.route('/users/<int:id>')
def user(id):
    try:
        user = next(filter(lambda x: x["id"] == id, USERS))
        # return render_template('user.html')
        # return "{} - {}".format(user['id'], user['name'])
        return render_template('user.html', **user)
    except StopIteration:
        return "404 Not Found"



if __name__ == "__main__":

    app.run(port = 8080, debug = True)
















