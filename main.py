import flask


app = flask.Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return flask.render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return flask.render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return flask.render_template("resume_2.html")

@app.route('/resume_3')
def resume_3():
    return flask.render_template("resume_3.html")

@app.route('/resume_template')
def resume_template():
    return flask.render_template("resume_template.html")

if(__name__ == "__main__"):
    app.run()