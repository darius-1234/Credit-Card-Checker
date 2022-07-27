from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Credit card verification <h1>CCV<h1>"

@app.route("/<num>")
def user(num):
    l = len(num)
    if not (l== 16):
        return f"<h1 style=color:red;font-size:110%;font-family:Helvetica;>Your card number should be 16 " \
               f"digits long. Yours is {l} digits long </h1> "
    # we iterate through the number from the LSD
    cardSum = 0
    isSecond = False
    for i in range(15, -1, -1):
        digit = ord(num[i]) - ord('0')
        if isSecond:
            digit *= 2
        # these 2 lines deal with both single digit and double-digit cases
        cardSum += digit // 10
        cardSum += digit % 10
        isSecond = not isSecond
    if cardSum % 10 == 0:
        return "<h1 style=color:green;font-size:110%;font-family:Helvetica;>Verified</h1>"
    else:
        return "<h1 style=color:red;font-size:110%;font-family;Helvetica>Card number invalid</h1>"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()