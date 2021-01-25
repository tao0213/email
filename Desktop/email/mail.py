import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#文件附檔
# with open("test.txt", "rb") as file:
#     filecontent = file.read()
# mime = MIMEText(filecontent, "base64", "utf-8")   
# mime["Content-Type"] = "application/octet-stream"   
# mime["Content-Disposition"] = 'attachment; filename = "test.txt"'

#圖片附檔
with open("IMG_0067.PNG", "rb") as file:
    filecontent = file.read()

mime = MIMEImage(filecontent)
mime["Content-Type"] = "application/octet-stream"
mime["Content-Disposition"] = 'attachment; filename="IMG_0067.PNG"'

#郵件主旨、標題
#mime = MIMEText("您好! 我是 Tao.", "plain", "utf-8")
mime["Subject"] = "Gmail sent by Python scripts(MIME)"
mime["From"] =" tao gmail"
mime["To"] = "tao yahoo"
#mime["Cc"] = ""
msg = mime.as_string()

#寄件者、收件者
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("znhooo0213@gmail.com", "sfpmuiovnwcjjxrf")
from_addr = "znhooo0213@gmail.com"
to_addr = ["znhooo0213@yahoo.com.tw"]
status = smtp.sendmail(from_addr, to_addr, msg)

if status == {}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()