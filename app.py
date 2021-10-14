from flask import Flask, request, jsonify, render_template
from flask_mail import Mail,Message
import pymongo
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import leprosy



app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://paras123:paras123@blog.w2rbt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


app.config['DEBUG']=True
app.config['TESTING']=False
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USE_SSL']=False
app.config['MAIL_USERNAME']='incognitohealer@gmail.com'
app.config['MAIL_PASSWORD']='incognito123'
app.config['MAIL_DEFAULT_SENDER']=('incognitohealer@gmail.com')
app.config['MAIL_MAX_EMAILS']=None
app.config['MAIL_ASCII_ATTACHMENTS']= False

mail=Mail(app)

@app.route('/predict1',methods=['POST'])
def predict1():
    int_features = [x for x in request.form.values()]
    l = []
    #['S ADITYA', 's.aditya04042001@gmail.com', '21/07/2001', '9:00 to 10:00', ' Child psychiatrist', '']
    for i in range(len(int_features)):
        l.append(int_features[i])
    name=l[0]
    email=l[1]
    day=l[2]
    msg= l[3]

    msg = Message('Leprosy_detector', recipients=[email])
    msg.html = 'MESSAGE FROM Leprosy_detector!'+'<br><br</br></br>'+"<br>Name : </br>"+name+'\n'+"<br>Day : </br>"+day+'\n''<br><br</br></br>'+"<br> join in this meet  at suitable slot</br>"+'<br>https://meet.google.com/cjo-raps-jwf</br>'
    mail.send(msg)
    return "Data Submitted"




class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = leprosy(self.filename)

clApp = ClientApp()
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')
    
@app.route("/Pros", methods=['GET'])
def proc():
    return render_template('Pros.html')

@app.route("/predict", methods=['POST'])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.prediction_leprosy()
    print(result)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
    #app().run(debug=True)
