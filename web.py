from flask import Flask
import grsed_core as grsed

app = Flask(__name__)

@app.route("/random/<int:number>")
def lapucha(number):
    return grsed.random_characters(number)
   
@app.route('/encode/<string:randomstring>')
def lapucheta(randomstring):
   return grsed.encode_string_64(randomstring)

@app.route('/decode/<string:encodedstring>')
def cortastetodalaloz(encodedstring):
   return grsed.decode_string_64(encodedstring)

if __name__ == "__main__":
    app.run(debug=True)