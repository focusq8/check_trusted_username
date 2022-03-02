from requests import Session

requests_sessions = Session()

def login_web():
    global get_csrftoken , get_sessions , username

    username = input(f'\n\n[ + ] Enter Your Username: ')
    password = input(f'\n[ + ] Enter Your Password: ') 

    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    headers_login = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,ar;q=0.8",
        "content-length": "317",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken=QPYyY1OkYQbU5F6VQOWXdNHJhiP9IwFY",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-ch-ua": '" Not;A Brand";v="99", "Chromium";v="98" , "Microsoft Edge";v="98"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62",
        "x-asbd-id": "198387",
        "x-csrftoken": "QPYyY1OkYQbU5F6VQOWXdNHJhiP9IwFY",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR1KZ8mFH_XuwnlCjaDXJPbYdAilnj1X4S5VVol7qrRH1Zhc",
        "x-instagram-ajax": "c14f5c1119e5",
        "x-requested-with": "XMLHttpRequest"
        }

    login_data = {
        "username": f"{username}",
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
        "queryParams": {},
        "optIntoOneTap": "false",
        "trustedDeviceRecords": {}
        }
   
    req_login = requests_sessions.post(url_login, headers=headers_login, data=login_data) 
    try:    
         
        if '"authenticated":true' in req_login.text:
            print(f'@{username} Logged In √ \n')
            get_sessions = req_login.cookies['sessionid']
            get_csrftoken = req_login.cookies.get_dict()['csrftoken']
            Check_user()
        else:
            input(req_login.text)

    except ValueError:
        print(req_login.text)
        input(f"[ ! ] Excepted Error ! Check On Your Username And Password")
        exit()

def Check_user():

    url_get_info = 'https://www.instagram.com/accounts/edit/?__a=1&__d=dis'
    headers_get_info = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'cookie': f"ig_nrcb=1; mid=YfyRDwALAAE2u2Xao59RvgY4Kie1; ig_did=24EAD7A2-41F3-458B-81B2-4C4E87CE77AE; csrftoken={get_csrftoken}; sessionid={get_sessions};",
        'referer': f'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        "sec-ch-ua": '" Not;A Brand";v="99", "Chromium";v="98" , "Microsoft Edge";v="98"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
        "x-asbd-id": "198387",
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1KZ8mFH_XuwnlCjaDXJPbYdAilnj1X4S5VVol7qrRH1Zhc',
        'x-requested-with': 'XMLHttpRequest'
        }

    req_get_info = requests_sessions.get(url_get_info, headers=headers_get_info)
    try:
        trusted_username = str(req_get_info.json()['form_data']['trusted_username'])
        if  trusted_username == username:
            input("it has")
        elif trusted_username != username:
            input(f"it has another , {trusted_username}")
        else:
            input("not sure")
    except:      
        input("it has not")

login_web()