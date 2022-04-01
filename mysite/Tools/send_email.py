
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from email.message import EmailMessage
from email.mime.image import MIMEImage
import os

class SendMessage:
    def __init__(self):
        self.msg =  MIMEMultipart("alternative")
        self.msg[ "From" ] = "chrisjulemontwebsite@gmail.com"
        # self.recipients = ['cjulemont@es.imshealth.com'] #'productiongovernance@es.imshealth.com'
        self.recipients = ['chrisjulemontwebsite@gmail.com', 'chrisjulemontwebsite@gmail.com' ] #'UPMSupport@es.imshealth.com', 'productiongovernance@es.imshealth.com' , 'JRocha@es.imshealth.com' ,'DGarcia@es.imshealth.com', 'amjimenez@es.imshealth.com' ,'MPrieto@es.imshealth.com'
        self.msg[ "To" ] = " , ".join(self.recipients)
        with open('/home/cwayacita/Documents/Folder/email_send') as f:
            self.password  = f.read().strip()
    def email(self, content, title):

        self.msg[ "Subject" ] = str(title)
        Title = str(title)
        date = datetime.today()
        date = str(datetime.strptime(str(date)[0:10], '%Y-%m-%d'))

        text = content
        # Create the plain-text and HTML version of your message

        html = """\
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns:m="http://schemas.microsoft.com/office/2004/12/omml" xmlns="http://www.w3.org/TR/REC-html40"><head><meta http-equiv=Content-Type content="text/html; charset=utf-8"><meta name=Generator content="Microsoft Word 15 (filtered medium)"><!--[if !mso]><style>v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style><![endif]--><style><!--
/* Font Definitions */
@font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
@font-face
	{font-family:Calibri;
	panose-1:2 15 5 2 2 2 4 3 2 4;}
@font-face
	{font-family:"Segoe UI";
	panose-1:2 11 5 2 4 2 4 2 2 3;}
@font-face
	{font-family:Corbel;
	panose-1:2 11 5 3 2 2 4 2 2 4;}
/* Style Definitions */
p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0cm;
	margin-bottom:.0001pt;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
a:link, span.MsoHyperlink
	{mso-style-priority:99;
	color:#0563C1;
	text-decoration:underline;}
a:visited, span.MsoHyperlinkFollowed
	{mso-style-priority:99;
	color:#954F72;
	text-decoration:underline;}
p.MsoListParagraph, li.MsoListParagraph, div.MsoListParagraph
	{mso-style-priority:34;
	margin-top:0cm;
	margin-right:0cm;
	margin-bottom:0cm;
	margin-left:36.0pt;
	margin-bottom:.0001pt;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
p.msonormal0, li.msonormal0, div.msonormal0
	{mso-style-name:msonormal;
	mso-margin-top-alt:auto;
	margin-right:0cm;
	mso-margin-bottom-alt:auto;
	margin-left:0cm;
	font-size:11.0pt;
	font-family:"Calibri",sans-serif;}
span.EmailStyle19
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle20
	{mso-style-type:personal;}
span.EmailStyle21
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle22
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle23
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle24
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle25
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle26
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle27
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle28
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle29
	{mso-style-type:personal;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
span.EmailStyle30
	{mso-style-type:personal-reply;
	font-family:"Calibri",sans-serif;
	color:windowtext;}
.MsoChpDefault
	{mso-style-type:export-only;
	font-size:10.0pt;}
@page WordSection1
	{size:612.0pt 792.0pt;
	margin:70.85pt 70.85pt 70.85pt 70.85pt;}
div.WordSection1
	{page:WordSection1;}
--></style><!--[if gte mso 9]><xml>
<o:shapedefaults v:ext="edit" spidmax="1026" />
</xml><![endif]--><!--[if gte mso 9]><xml>
<o:shapelayout v:ext="edit">
<o:idmap v:ext="edit" data="1" />
</o:shapelayout></xml><![endif]--></head><body bgcolor="#CFCDCD" lang=EN-US link="#0563C1" vlink="#954F72"><div class=WordSection1><div align=center><table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0 style='background:white;border:solid #D4D5D5 1.5pt'><tr><td width=823 colspan=3 style='width:616.95pt;border:none;padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='font-size:40.0pt;color:black'>  </span><span style='font-size:40.0pt;color:#581845'>⨑</span><span style='font-size:40.0pt;font-family:"Corbel",sans-serif;color: #e78fd9'>THERA</span><span style='font-size:40.0pt;font-family:"Corbel",sans-serif;color:#581845'>MEX</span><span style='font-size:40.0pt'><o:p></o:p></span></p></td></tr><tr><td width=30 valign=top style='width:22.5pt;border:none;padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><img width=30 height=1 style='width:.3125in;height:.0104in' id="Picture_x0020_50" src="cid:image002.png@01D6FFCA.631B2B90" ></span><o:p></o:p></p></td><td width=713 valign=top style='width:534.65pt;border:none;padding:0cm 0cm 0cm 0cm'><table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width=691 style='width:518.05pt;background:white'><tr><td style='padding:0cm 0cm 0cm 0cm'></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><img width=1 height=28 style='width:.0104in;height:.2916in' id="Picture_x0020_51" src="cid:image003.png@01D6FFCA.631B2B90" ></span><span style='font-size:12.0pt;font-family:"Times New Roman",serif'><o:p></o:p></span></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal align=center style='text-align:center'><b><span style='font-size:18.0pt;font-family:"Arial",sans-serif;color:black;text-transform:uppercase'>""" + Title + """</span></b><b><span style='font-size:18.0pt;font-family:"Arial",sans-serif;color:#005587;text-transform:uppercase'><o:p></o:p></span></b></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><img width=1 height=18 style='width:.0104in;height:.1875in' id="Picture_x0020_52" src="cid:image004.png@01D6FFCA.631B2B90" ></span><span style='font-size:12.0pt;font-family:"Times New Roman",serif'><o:p></o:p></span></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal align=center style='text-align:center;line-height:13.5pt'><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:black'>""" + date + """</span><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:#2B3A42'> 202</span><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:black'>1</span><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:#2B3A42'><o:p></o:p></span></p></td></tr><tr><td style='border:none;border-bottom:solid #e78fd9 1.5pt;padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><img width=1 height=27 style='width:.0104in;height:.2812in' id="Picture_x0020_53" src="cid:image005.png@01D6FFCA.631B2B90" ></span><span style='font-size:12.0pt;font-family:"Times New Roman",serif'><o:p></o:p></span></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'></td></tr><tr><td style='border:none;border-bottom:solid #581845 1.5pt;padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><o:p>&nbsp;</o:p></span></p><p class=MsoNormal><span style='color:black'>"""+ text +"""</span><o:p></o:p></p><p class=MsoNormal><o:p>&nbsp;</o:p></p></td></tr><tr><td style='border:none;padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='font-size:10.0pt;color:black'>If you have a question please contact </span><span style='color:black'><a href="mailto:productiongovernance@es.imshealth.com"><span style='font-size:10.0pt'>productiongovernance@es.imshealth.com</span></a></span><span style='font-size:10.0pt;color:black'> or raise a ticket to </span><span style='font-size:10.0pt;color:#203864'>“<b>JIRA PGT </b>”. </span><span style='font-size:10.0pt;color:black'>&nbsp;</span><span style='font-size:10.0pt'><o:p></o:p></span></p><p class=MsoNormal><span style='font-size:10.0pt'><o:p>&nbsp;</o:p></span></p><p class=MsoNormal><span style='font-size:10.0pt;color:black'>Thank you for your attention!</span><span style='font-size:10.0pt'><o:p></o:p></span></p><p class=MsoNormal><span style='font-size:10.0pt;font-family:"Times New Roman",serif'><o:p>&nbsp;</o:p></span></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:black'><o:p>&nbsp;</o:p></span></p><p class=MsoNormal style='line-height:15.0pt'><span style='font-size:10.5pt;font-family:"Segoe UI",sans-serif;color:#333333'>Kind regards<o:p></o:p></span></p><p class=MsoNormal><b><span style='color:#581845'>Production Governance <o:p></o:p></span></b></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal align=center style='text-align:center'><span style='font-size:9.0pt;font-family:"Arial",sans-serif;color:black'><o:p>&nbsp;</o:p></span></p><p class=MsoNormal align=center style='text-align:center'><o:p>&nbsp;</o:p></p><p class=MsoNormal align=center style='text-align:center'><span style='font-size:9.0pt;font-family:"Arial",sans-serif;color:#ABAEB1'>For Internal Use Only<o:p></o:p></span></p></td></tr><tr><td style='padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><img border=0 width=1 height=20 style='width:.0104in;height:.2083in' id="Picture_x0020_55" src="cid:image011.png@01D6FFCA.631B2B90" ></span><span style='font-size:12.0pt;font-family:"Times New Roman",serif'><o:p></o:p></span></p></td></tr></table></td><td width=80 valign=top style='width:59.8pt;border:none;padding:0cm 0cm 0cm 0cm'><p class=MsoNormal><span style='color:black'><img border=0 width=30 height=1 style='width:.3125in;height:.0104in' id="Picture_x0020_56" src="cid:image002.png@01D6FFCA.631B2B90" ></span><span style='font-size:12.0pt'><o:p></o:p></span></p></td></tr></table></div><p class=MsoNormal><span lang=FR><o:p>&nbsp;</o:p></span></p><p class=MsoNormal><span lang=FR><o:p>&nbsp;</o:p></span></p><p class=MsoNormal><span lang=FR><o:p>&nbsp;</o:p></span></p></div></body></html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text,"plain")
        part2 = MIMEText(html,"html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.msg.attach(part1)
        self.msg.attach(part2)



        context = ssl.create_default_context()

        # self.msg.set_content(content)
#'qgbl-smtprelay.quintiles.com' port=25
        # with smtplib.SMTP("smtp-mail.outlook.com",port=587) as smtp:
        #     smtp.starttls(context=context)
        #     smtp.login(self.msg[ "From" ],self.password)
        #     # smtp.send_message(self.msg)
        #     # for email in self.recipients:
        #     #     self.msg['To'] = email
        #     smtp.sendmail(self.msg[ 'From' ],self.recipients,self.msg.as_string())

#        with smtplib.SMTP("qgbl-smtprelay.quintiles.com",port=25) as smtp:
        with smtplib.SMTP('smtp.gmail.com',port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(self.msg[ "From" ],self.password)
            smtp.send_message(self.msg)
            # for email in self.recipients:
            #     self.msg['To'] = email
            smtp.sendmail(self.msg[ 'From' ],self.recipients,self.msg.as_string())


SendMessage.email(SendMessage(), 'env prod = ' + ' : SBPDS REPORT SUCCESS : ' + 'The process took seconds, ' + 'The process has updated ' +
 ' lines and created ' + ' new lines', 'SBPDS REPORT SUCCESS')
