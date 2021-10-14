# Leprosy Detector
A web app which is used to detect a chronic skin disease of leprosy. We attempt to diagnose leprosy as well as help them to fight the disease.With the help of our Machine Learning model we attempt to diagnose leprosy and make an appointment with the medical professionals.With our chat room we try to provide patinets with free consultation.While our chatbot helps you to get to know more about the disease and solve the stigma about it.We also provide you the donate option which enables you to help the less priveleged.  
### LINK
Website link: https://leprosy.herokuapp.com/ <br>
Ppt link: https://drive.google.com/file/d/1GPVdbFysLKXv6A6B5PuAEqVVgu5wvQul/view?usp=sharing&authuser=2<br>
Demo video link - https://drive.google.com/file/d/1HT7i8a-SVtWVsrkpNhq5axX5dHDB6BMw/view<br>
You tube Link of the video explaining the project :https://youtu.be/FBXLglj5cR8 (We added a payment gateway too enabling you to pay through card too)<br>
### Technologies Used
For the front-end we mainly used 

1.HTML/CSS<br>
2.REACT(JS)<br>
For the backend we used :<br>
1.Flask<br>
2.Node.js<br>
3.DialogFlow<br>
4.Tensoflow<br>
We used Mongo DB as the data base in order to store the required data(Blogs).
### Components of the Project
1.Leprosy detection:With our Ml model and image detection we accurately diagnose whether someone is suffering with leprosy or not (Kindly upload dermatology related relevant images only).The model was created using CNN architecture and deployed on flask(model.h5).<br>
2.Dermat:This is the realtime chat application which enables to replicate a support group system.(Dermat)<br>
3.WEvolve:This is the blogging website which enables user to see the blogs written by proffesionals as well as people.Blog's Front End is developed using React and for Backend we used Node, while Blogs are stored in MongoDB.(WEvolve)(In WEvolve folder the front end react part is in client folder while the backend part is in our WEvolve folder only)<br>
4.Charlie:The chatbot was developed using Dialogflow.(In Templates/index.html a short snippet code is added in the body tag to integrate the chatbot)<br>
5.Payment Gateway:We also enable you to donte through card as well as through Paytm.For this we used Stripe library.
### INSTALLING
Step 0: ```Git clone this project```<br>
Step 1: ```cd <local-repository-folder>``` <br>
Step 2: ```pip3 install -r requirements.txt```<br>
Step3: ```python app.py```<br>
### Credits
Team Name:Rookies<br>
Members:<br>
Asis Kaur<br>
Anmol Mittal<br>
S Aditya<br>
Paras Jain<br>
