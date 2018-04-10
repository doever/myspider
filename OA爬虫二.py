import requests
import time

headers={"Host":"192.168.1.90:8080",
         "Referer":"http://192.168.1.90:8080/wui/theme/ecology8/page/login.jsp?emplateId=12&logintype=1&gopage=&languageid=7&message=16",
         "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }

session = requests.session()
login_url = 'http://192.168.1.90:8080/login/VerifyLogin.jsp'
data = {"loginfile": "/wui/theme/ecology8/page/login.jsp?templateId=12&logintype=1&gopage=",
        "logintype": "1",
        "fontName": "微软雅黑",
        "message": "16",
        "gopage": "",
        "formmethod": "post",
        "rnd": "",
        "serial": "",
        "username": "",
        "isie": "false",
        "islanguid": "7",
        "loginid": "SH17032801",
        "userpassword": "11111111",
        "submit": "登录"
        }
res = session.post(login_url,data=data,headers=headers)
print(res.status_code)
res.encoding="UTF-8"
f=open("C:/users/administrator/desktop/11.txt","wb")
f.write(res.content)
f.close()
##ViewRequestIframe.jsp?requestid=338212&isovertime=0&_workflowid=44&_workflowtype=5
oa_url="http://192.168.1.90:8080/workflow/request/ViewRequest.jsp?requestid=338212&_workflowid=44&_workflowtype=5&isovertime=0"
#oa_url="http://192.168.1.90:8080/js/hrm/getdata.jsp?cmd=compareTime&arg0=1&arg1="
# oa_url="http://192.168.1.90:8080/wui/theme/ecology8/page/getRemindInfo.jsp?1=1518143453348="
res2 = session.get(oa_url)
time.sleep(10)
print(res2.status_code)
res2.encoding="UTF-8"
g=open("C:/users/administrator/desktop/12.txt","wb")
g.write(res2.content)
g.close()
