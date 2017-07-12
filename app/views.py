from app import app
from flask import render_template


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/resource/<resource_name>')
def resource(resource_name):
    return render_template("resource.html", resource_name=resource_name)


if __name__ == '__main__':
    app.run()
