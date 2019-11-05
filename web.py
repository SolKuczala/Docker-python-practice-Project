from flask import Flask
import grsed_core as grsed

app = Flask(__name__)

@app.route("/random/<int:number>")
def x(number):
    return grsed.random_characters(number)
   
@app.route('/encode/<string:randomstring>')
def y(randomstring):
   return grsed.encode_string_64(randomstring)

@app.route('/decode/<string:encodedstring>')
def z(encodedstring):
   return grsed.decode_string_64(encodedstring)

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0')