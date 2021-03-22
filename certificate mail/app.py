# doing necessary imports
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import smtplib
from email.message import EmailMessage

df = pd.read_csv('list.csv')
emaillst=df['email'].values.tolist()
df.set_index("email", inplace=True)
EMAIL_ADDRESS = "gmail"
EMAIL_PASSWORD = "password"

for email in emaillst:
    try:
        a=df["First Name"][email]
        name=df.Title[email]+" "+df["First Name"][email]+" "+df["Last Name"][email]
        font = ImageFont.truetype('LibreBaskerville-Regular.ttf', 100)
        #for index, j in df.iterrows():
        img = Image.open('certificate.jpg')
        draw = ImageDraw.Draw(img)
        image_width = img.width
        image_height = img.height
        text_width, _ = draw.textsize(name, font=font)

        draw.text(xy=((image_width - text_width) / 2, 560), text='{}'.format(name), fill=(0, 0, 0),font=font)
        pdf = img.convert('RGB')

        pdf.save('static/pictures/certificate.pdf')

        msg = EmailMessage()
        msg['Subject'] = "certificate"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg.set_content('''
Hi there,

Thanks for being awesome!.

Magfyindia provide various services such as business email,web hosting, dedicated servers, application development,website designing and other IT solutions for your business.

Thanks & Regards
Arjun Panwar


!! Mail us at info@magfyindia,com or visit our website https://magfyindia.com !!

Powered by Magfyindia.''')

        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                <div></div>
<div data-marker="__QUOTED_TEXT__">
<table border="0" cellpadding="0" cellspacing="0" class="body" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background-color: #ffffff; margin-top: 10%;">
<tbody>
<tr>
<td class="container" style="font-family: sans-serif; font-size: 14px; vertical-align: top; display: block; margin: 0 auto; max-width: 580px; padding: 10px; width: 580px;">
<div class="content" style="box-sizing: border-box; display: block; margin: 0 auto; max-width: 580px; padding: 10px;">
<table class="main" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background-color: #203b2a; color: #fff76f; font-family: 'Open Sans', sans-serif; box-shadow: 10px 10px 5px grey; border-radius: 3px;">
<tbody>
<tr>
<td class="wrapper" style="font-family: sans-serif; font-size: 14px; vertical-align: top; box-sizing: border-box; padding: 20px;">
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;">
<tbody>
<tr>
<td style="font-family: sans-serif; font-size: 14px; vertical-align: top;">
<p style="font-family: sans-serif; font-size: 14px; font-weight: bold; margin: 0; margin-bottom: 15px;"><span style="color: #ffffff;">Hi there,</span></p>
<p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;"><span style="color: #ffffff;">Thanks for being awesome!.</span></p>
<hr style="border-top: 1px solid red; margin-bottom: 10px;" />
<p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;"><span style="color: #ffffff;">Magfyindia provide various services such as business email,web hosting, dedicated servers, application development,website designing and other IT solutions for your business.</span></p>
<p style="font-family: sans-serif; font-size: 14px; font-weight: bold; margin: 0; margin-bottom: 5px; margin-top: 10%;"><span style="color: #ffffff;">Thanks &amp; Regards</span><br /><span style="color: #ffffff;">Arjun Panwar</span><br /><br /></p>
</td>
</tr>
<tr>
<td align="center">
<p style="font-family: sans-serif; font-size: 12px !important; font-weight: normal; font-style: italic; margin: 0; margin-bottom: 0px; margin-top: 10%;"><span style="color: #ffffff;">!! Mail us at info@magfyindia,com or visit our website <a href="https://magfyindia.com" target="_blank" title="magfyindia.com" style="color: #ffffff;">https://magfyindia.com</a> !!</span></p>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<div class="footer" style="clear: both; margin-top: 10px; text-align: center; width: 100%;">
<table border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;">
<tbody>
<tr>
<td class="content-block powered-by" style="font-family: sans-serif; vertical-align: top; padding-top: 10px; font-size: 12px; color: #203b2a; text-align: center;">Powered by <a href="http://magfyindia.com" target="_blank" style="color: #203b2a; font-size: 12px; text-align: center; text-decoration: none; font-weight: bold;">Magfyindia</a>.</td>
</tr>
</tbody>
</table>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
            </body>
        </html>
        """, subtype='html')
        with open("static/pictures/certificate.pdf","rb") as f:
            file_data=f.read()
            file_name=name+".pdf"
        msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name  )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        os.remove("static/pictures/certificate.pdf")
        print("sent = "+email)



    except Exception as e:
        print("unsent = "+email,e)
print("mail sent")
