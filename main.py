from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def hello():
    """
    Navigate to the main page.
    """
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()