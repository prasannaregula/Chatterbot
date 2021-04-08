from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index(name=None):
    return render_template('index.html',name=name)

def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    import Chatbot1
    import Chatbot2
    flag= True
    print("Hi Welcome to VOVO Electric! I'm VOVOBot. Any queries?, COOL! let's chat!")
    while (flag==True):
        userText = request.args.get('msg')
        userText=userText.lower()
        if(userText!= "Goodbye"):
            return (response(str(userText)))
        else:
            return (response(str(userText)))


if __name__ == "__main__":
    app.run()