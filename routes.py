from flask import Flask, render_template

from hangman_client import Manager

app = Flask(__name__, template_folder="website/templates")

def createDictionary(file_name):
    file = file_name
        
    dict = {}
        
    with open(file, "r") as file:
        words = file.readlines()
        # seize serve sharp andrew beezy jazzy aahed Abamp poops wendy john phone mouse mice lamp superfaiclious
        for word in words:
            dict.update({word.strip(): 1})
    
    return dict

@app.route("/")
def test():
    return render_template('hangman.html')

# @app.route("/dict1")
# def dict1():
#     return createDictionary("words.txt")

# @app.route("/dict2")
# def dict2():
#     return createDictionary("dict2.txt")


if __name__ == "__main__":
    app.run(debug=True)