import csv
import time
import smtplib
import json
import os

import urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import requests

# 設置發件人的賬戶信息

def demomail(msg):
# /demomail#jj0922792265@outlook.com#
 
    wjson_file = "demosmtp.json"
    wsftpflr = os.environ.get('linebot_ftpurl')
# 讀取 JSON 檔案  local
#   # with open("cbd.json" , "r") as f:
    #with open(wjson_file , "r") as f:
    #    js_dta = json.load(f)

    url = wsftpflr + "json/" + wjson_file #http://www.abc.com/cust.json"
    response = requests.get(url)
    if response.status_code != 200:
        print (response.status_code) 
        return (" Demo Mail not config " + url )
    
    
    print(url)
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    js_dta = json.loads(data)
    
    username = js_dta["username"]    #"tt6395b@outlook.com" 
    print(username)
    password = js_dta["password"]   #"bqm2151#"
    smtp_server = "smtp.office365.com"
    smtp_port = 587

        # 讀取收件人列表
    wsmsg =  msg.split('#')   # msg = '/demomail#jj0922792265@outlook.com#'
    receiver = wsmsg[1]    #"buddhisty@gmail.com" #"tt6395b@outlook.com" 
    subject = js_dta["subject"] #"臉書優質紛絲團，邀請您 按讚支持" 

    content = js_dta["content"]  # "陌生開發優質粉絲團，人員募集中\n歡迎加入\n分享陌開心法及免費工具\n邀起您加入我們 請開啟網址 https://www.facebook.com/profile.php?id=100065188140659 按讚留言 獲取更多的資訊\n www.mydailychoice.com"
    sendfrom = js_dta["from"]   
    #sendfrom = "FACEBOOK"
                # 設置郵件內容

    print ("=================  demomail info ==================")
    print ("user = " + username)
    print("password= " + password)
    print("sendfrom " + sendfrom )
    print ("to " + receiver)

    message = MIMEMultipart()
    print(sendfrom + " <" +  username + ">")
    message["From"] = username  #sendfrom + "<" +  username + ">"
    message["To"] =  receiver 
    message["Subject"] = subject 

    message.attach(MIMEText(content, "plain"))
                # 添加附件
        #filename = "attachment.pdf"
        #with open(filename, "rb") as attachment:
        #    part = MIMEApplication(attachment.read(), Name=filename)
        #    part["Content-Disposition"] = f'attachment; filename="{filename}"'
        #    message.attach(part)
                # 發送郵件
    try:
        
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        print (username +"-" + password + "-" + smtp_server  + "-" + str(smtp_port))
        smtp.login(username, password)
        print("smtp sendmail")
        smtp.sendmail(username, [receiver], message.as_string())
        smtp.quit()
        print(f"郵件已發送至 {receiver}")
        return ((f"郵件已發送至 {receiver}"))
    except Exception as e:
                print(f"郵件發送失敗：{e}")
                return (f"郵件發送失敗：{e}")