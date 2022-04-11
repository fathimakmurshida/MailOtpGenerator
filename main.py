import string
from  fastapi import FastAPI
import math
import random
import smtplib


app= FastAPI()

@app.post("/email-verification/{emailid}")
def send_otp(emailid):
        
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        subject='r one v one'
        msg= f'Subject: {subject}\n\n{otp}'
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("fathimamurshida95@gmail.com", "escxawwmkp")
        s.sendmail('fathimamurshida95@gmail.com',emailid,msg)
        return("success")
   
