import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.message import EmailMessage


#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}

def send_msg(name,subject_name,emailto):
  msg = EmailMessage()
  msg.set_content(f"\nHey @{name} ( ^ ^ )\n\nAttendance has been submitted\n\nDetails:\nSubject:{subject_name} :)\nStatus:present\n\nThank you........&&831!!!")
  msg['subject'] = "Your attendance result :)"
  msg['from'] = "attendence.result.bot@gmail.com"
  msg['to'] = emailto
  server = smtplib.SMTP_SSL("smtp.gmail.com",465)
  server.login("attendence.result.bot@gmail.com","DevarajAgulla")
  server.send_message(msg)
  server.quit()

  
login_list = [
        
         {"username":"B191843","password":"S@sb191843*#","email":"sujeeth.barkam@gmail.com","name":"Sujith"},
         
         {"username":"B191081","password":"Ravi*jyothi1","email":"devaagulla770@gmail.com","name":"Deva"},
         
         {"username":"B191329","password":"Rgukt@2021","email":"krishnakrupalithakur15@gmail.com","name":"Mowaya"},
         
         {"username":"B181598","password":"Chinna_2009","email":"lakshmanachary1225@gmail.com","name":"B181598"},
         
         {"username":"B191398","password":"Bhavana@123","email":"chavaganivamshi123@gmail.com","name":"Bhavana"},
         
         {"username":"B192439","password":"Virat@18*-k","email":"rameshrguktbasar@gmail.com","name":"Virat_ramesh"},
         
         {"username":"B191177","password":"Cse.3195","email":"Vempatimeghana1@gmail.com","name":"Meghana"},
         
         {"username":"B191124","password":"K1vy@2003","email":"Kavyakakkerla24@gmail.com","name":"Kavya"},
  
         {"username":"B191138","password":"Karthik@286","email":"Karthikmethuku286@gmail.com","name":"Karthik"},

         {"username":"B181623","password":"Sudheer*2003","email":"sudheer123kondapuram@gmail.com","name":"B181623"}
         
        ]

while True:
  for login in login_list:
    with requests.Session() as s:
      try:
        login_data = {
              "anchor":"",
              "logintoken":"",
              "username":login["username"],
              "password":login["password"]
              }
        #print("looop")
        #print(login["name"])
        r = s.get("http://lms.rgukt.ac.in/login/index.php")
        soup = BeautifulSoup(r.content,"html.parser")
        login_data["logintoken"] = soup.find("input",attrs={"name":"logintoken"})["value"]
        r = s.post("http://lms.rgukt.ac.in/login/index.php/" , data = login_data)
        soup = BeautifulSoup(r.content,"html.parser")
        #print(r.content)
        x = datetime.datetime.now()
        month = x.strftime("%B")
        day = x.strftime("%A")
        date = x.strftime("%d")
        date = int(date)
        url = soup.find("a",{"aria-label":f"Today {day}, {date} {month}"})["href"]
        r = s.post(url)
        soup = BeautifulSoup(r.content,"html.parser")
        activity = soup.find_all("a",class_ = "card-link")
        links = []
        for ac in activity:
            links.append(ac["href"])
            #print(links)
        for url in links:
            r = s.post(url)
            soup = BeautifulSoup(r.content,"html.parser")
            try:
                attendance = soup.select_one(".statuscol a[href]")["href"]
                #print(attendance)
                r = s.post(attendance)
                soup = BeautifulSoup(r.content,"html.parser")
                sessid = soup.find("input",{"name":"sessid"})["value"]
                sesskey = soup.find("input",{"name":"sesskey"})["value"]
                status = soup.find("input",{"name":"status"})["value"]
                form_data = {
                     "sessid":sessid,
                     "sesskey":[sesskey,sesskey],
                     "_qf__mod_attendance_form_studentattendance":"1",
                     "mform_isexpanded_id_session":"1",
                     "status":status,
                     "submitbutton":"Save+changes"
                    }
                r = s.post("http://lms.rgukt.ac.in/mod/attendance/attendance.php" , data = form_data)
                soup = BeautifulSoup(r.content,"html.parser")
                subject_name = soup.find("h1").get_text() 
                send_msg(login["name"],subject_name,login["email"])
                #print(subject_name)
            except:
                continue
      except:
        continue

  #print("finished")
            
#name = soup.find("h1").get_text()
#print(name)
#print(r.json())
#LM5GZs30N5lDfN20LkbAJLYiMq4s7muv
#QDH6NQRm6kJwM8lLEqFbC8JImEjbcWvF



"""sessid	"30551"
sesskey	[…]
0	"bWnd2ZrArj"
1	"bWnd2ZrArj"
_qf__mod_attendance_form_studentattendance	"1"
mform_isexpanded_id_session	"1"
status	"3422"
submitbutton	"Save+changes" """ 
