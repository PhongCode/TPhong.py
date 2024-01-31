from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from time import sleep

class web:
    def __init__(self, uid, pword, ma2fa, key_cap):
        self.uid= uid
        self.pword= pword
        self.ma2fa= ma2fa
        self.key_cap= key_cap
        self.key_capfull = 'max1_'+key_cap

        account= "C:\\Users\\ADMIN\\Documents\\Account Chrome\\"+ self.uid
        chrome_option = Options()
        chrome_option.add_argument('--user-data-dir='+ account)
        chrome_option.add_extension('Max1_CaptCha69.Com_v1.11.2_0.crx')
        chrome_option.add_extension('Auto_Click_Submit_CaptCha69.Com.crx')
        self.chrome = webdriver.Chrome(chrome_option)
        self.chrome.set_window_rect(10,10,450,650)
#client-key-input
#client-key-save-btn
    def x_home(self):
        self.chrome.get('https://twitter.com/home?lang=en')
    
    def x_login(self):
            try:#đăng nhập
                self.chrome.get('https://twitter.com')
                sleep(3)
                elements = self.chrome.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/div/span')
                name = [na.text for na in elements]
                if name[0]=='Already have an account?':
                    self.chrome.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div').click()
                    sleep(5)
                    self.chrome.find_element(By.NAME,'text').click()
                    self.chrome.find_element(By.NAME,'text').send_keys(self.uid)
                    sleep(3)
                    try:
                        self.chrome.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]/div').click()
                    except:
                        pass
                    sleep(7)
                    try:
                        self.chrome.find_element(By.NAME,'password').click()
                    except:
                        pass
                    self.chrome.find_element(By.NAME,'password').send_keys(self.pword)
                    try:
                        self.chrome.execute_script(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click()
                    except:
                        pass
                    sleep(4.5)
            except:
                sleep(1)
                pass
            
            try:#check bị chặn 
                elements=self.chrome.find_elements(By.XPATH,'//*[@id="modal-header"]/span/span')
                name = [na.text for na in elements]
                if name[0] == 'Suspicious login prevented':
                    self.chrome.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div').click()
                    text='Suspicious login prevented'
                    print(text)  
                    sleep(5)
                    text ='error'
                    return text
            except:
                sleep(1)
                pass

            try:##nhập mã 2fa
                sleep(4)
                elements= self.chrome.find_elements(By.XPATH,'//*[@id="modal-header"]/span/span')
                name = [na.text for na in elements]
                if name[0] == 'Enter your verification code':
                    id_ma = 'https://2fa.live/tok/' + self.ma2fa
                    web = requests.get(id_ma)
                    data = web.text
                    data = data.split(':')
                    data = data[1].split('"')
                    ma = data[1]+'\n'
                    print('Mã 2fa bạn là: '+ ma)
                    self.chrome.find_element(By.NAME,'text').send_keys(ma)
            except:
                sleep(1)
                pass

            try: #Hmm...this page doesn’t exist. Try searching for something else.
                elements = self.chrome.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/span/span')
                name = [na.text for na in elements]
                if name[0] == 'Hmm...this page doesn’t exist. Try searching for something else.':
                    self.chrome.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/a/span').click()
                    sleep(7)
            except:
                sleep(1)
                pass

            try:#check mail chưa hoàn thiện
                elements = self.chrome.find_elements(By.XPATH,'/html/body/div[2]/div/div[1]')
                name =[na.text for na in elements]
                if name[0] == 'Your account has been locked.':
                    self.chrome.find_element(By.XPATH,'/html/body/div[2]/div/form/input[6]').click()
                    print('Do chưa có acc dạng gửi code về mail nên admin chưa làm thông cảm nếu dính phải dạng này hãy làm tay đỡ đơi cập nhật') 
                    sleep(5)
            except:
                sleep(1)
                pass

            try:
                elements = self.chrome.find_elements(By.XPATH,'/html/body/div[2]/div/div[1]')
                name = [na.text for na in elements]
                if name == '\nPassword change required\n':
                    self.chrome.find_element(By.XPATH,'/html/body/div[2]/div/a').click()

            except:
                pass

            try:
                elements = self.chrome.find_elements(By.XPATH,'/html/body/div[2]/div/div[1]')
                name = [na.text for na in elements]
                if name == '\nHow do you want to reset your password?\n':
                    self.chrome.find_element(By.XPATH,'/html/body/div[2]/div/form/input[2]').click()

            except:
                pass

            try:#Options(lỗi captcha mới có)
                elements = self.chrome.find_elements(By.XPATH,'/html/body/div[1]/div/ul/li/span')
                name = [na.text for na in elements]
                so_lan_giai = 0
                while name[0] == 'Options':
                    if so_lan_giai < 4:
                        print(f'đang giải captcha {so_lan_giai + 1}')
                        sleep(30)
                        so_lan_giai +=1
                        elements = self.chrome.find_elements(By.XPATH,'/html/body/div[1]/div/ul/li/span')
                        name = [na.text for na in elements]
                    else:
                        print('Giải tay đi do sợ tốn tiền bạn á')
                        elements = self.chrome.find_elements(By.XPATH,'/html/body/div[1]/div/ul/li/span')
                        name = [na.text for na in elements]
                        sleep(5)
            except:
                sleep(1)
                pass

            try:#đã giải xong
                elements = self.chrome.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/span/span')
                name = [na.text for na in elements]
                if name[0] == 'Everyone can reply':
                    text = self.check_login()
                    if text =='done':
                        print('đã giải xong')
            except:
                sleep(1)
                pass
  
            try:
                elements = self.chrome.find_elements(By.XPATH,'/html/body/div[2]/div/div[1]')
                name =[na.text for na in elements]
                if name[0] == 'Account unlocked.':
                    self.chrome.find_element(By.XPATH,'/html/body/div[2]/div/form/input[6]').click()
                    sleep(3)
            except:
                sleep(1)
                pass

    def add_key_captcha(self):
        self.chrome.get('chrome-extension://pabjfbciaedomjjfelfafejkppknjleh/popup.html')
        sleep(4)
        self.chrome.find_element(By.ID,'client-key-input').clear()
        sleep(1)
        self.chrome.find_element(By.ID,'client-key-input').send_keys(self.key_capfull)
        sleep(1)
        self.chrome.find_element(By.ID,'client-key-save-btn').click()
        sleep(1.5)

        try:
        #setup recaptcha2
            self.chrome.find_element(By.ID,'captcha-dropdown-btn-ReCaptcha2').click()
            sleep(0.5)
            self.chrome.find_element(By.ID,'settings-Recaptcha-delay-between-click-switch').click()
            sleep(0.5)        
            self.chrome.find_element(By.ID,'settings-ReCaptcha2-delay-between-click-value').send_keys(2000)
            self.chrome.find_element(By.ID,'settings-ReCaptcha2-delay-start').send_keys(2000)
            sleep(0.5)
            self.chrome.find_element(By.ID,'captcha-dropdown-btn-ReCaptcha2').click()
            sleep(1)
        #setup hcaptcha
            self.chrome.find_element(By.ID,'captcha-dropdown-btn-HCaptcha').click()
            sleep(0.5)
            self.chrome.find_element(By.ID,'settings-hCaptcha-delay-between-click-switch').click()
            sleep(0.5)
            self.chrome.find_element(By.ID,'settings-HCaptcha-delay-between-click-value').send_keys(2000)
            self.chrome.find_element(By.ID,'settings-HCaptcha-delay-start').send_keys(2000)
            sleep(0.5)
            self.chrome.find_element(By.ID,'captcha-dropdown-btn-HCaptcha').click()
            sleep(1)        
        #setup funcaptcha
            self.chrome.find_element(By.ID,'captcha-dropdown-btn-FunCaptcha').click()
            sleep(0.5)
            self.chrome.find_element(By.ID,'settings-FunCaptcha-delay-between-click-switch').click()
            sleep(0.5)
            self.chrome.find_element(By.ID,'settings-FunCaptcha-delay-between-click-value').send_keys(2000)
            self.chrome.find_element(By.ID,'settings-FunCaptcha-delay-start').send_keys(2000)
            sleep(0.5)
            self.chrome.find_element(By.ID,'captcha-dropdown-btn-FunCaptcha').click()
            sleep(1)
        except:
            print('Lỗi phần thêm extetion')

   
    def check_key_captcha(self):
        web = requests.get('https://captcha69.com/check-thread/thread_'+self.key_cap)
        data = web.text
        key = data.split('</br>')
        if key == '{"Thread_is_Run":0,"Max_Thread_of_Thread":0,"Max_Thread_of_Point":0,"Points":0,"status":"ERROR_API_KEY_NOT_EXITS"}':
            text ='key_loi'
            print('Không tìm thấy key của bạn')
            return text
        else:
            print('Key của bạn còn '+key[3])
            text = 'key_done'
            return text

    def check_login(self):
        self.chrome.get('https://twitter.com/'+self.uid)
        sleep(2.5)
        self.chrome.get('https://twitter.com/'+self.uid)
        sleep(2.5)

        try:
            elements = self.chrome.find_elements(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/span')
            name = [na.text for na in elements]
            if name[0] == 'Turn on notifications':
                sleep(0.5)
                self.chrome.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div').click()
                sleep(2)
        except:
            pass

        try:
            elements = self.chrome.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div[2]/div/div[1]/span')
            name = [na.text for na in elements]
            if name[0] == 'Caution: This account is temporarily restricted':
                text = 'error'
                print('tài khoản bị hạn chế')
                return text
        except:
            pass

        try:#check id
            elements = self.chrome.find_elements(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/span')
            name = [na.text for na in elements]
            sleep(2.5)
            if str(name[0]) == '@'+self.uid:
                print(f'Login thành công hoặc live id của bạn là {self.uid}')
                text ='done'
                return text
        except:
            print(f'Đăng nhập lỗi lại id {self.uid}')
            text='error'
            return text

    def get_cookie(self):
        try:
            cookies_list = self.chrome.get_cookies()
            cookieString = ""
            for cookie in cookies_list[:-1]:
                cookieString = cookieString + cookie["name"] + "="+cookie["value"]+"; "
            cookieString = cookieString  + cookies_list[-1]["name"] + "="+ cookies_list[-1]["value"]
            data= cookieString
            sleep(1.5)
            print(f'Đã lấy cookie của {self.uid}')
            return str(data)
        except:
            print(f'khong lay cookie cua acc {self.uid} duoc')
            pass
    
    def quit(self):
        self.chrome.quit()
##############################################################################################################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##############################################################################################################################################
def get_data(num, file):
    data = ''
    f = open(file, 'r')
    for i in range(num):
        data = f.readline()
    data = data.split('|')
    f.close()
    return data

def add_data(text,file):
    f = open(file, 'a')
    f.write(text+'\n')
    f.close() 

def reset(text):
    f= open(text, 'w')
    f.write('')
    f.close()

def sum_data(arr):
    data = arr[0]
    for i in range(len(arr)-1):
        if i > 0:
            data = data + '|' + arr[i]
    return data
    

if __name__ == '__main__':
    print('[1] login nick X mới hoặc login lại\n[2] Auto lấy cookie hàng loạt + đăng nhập lại khi bị văng(có hỗ trợ captcha69_max1)\n[3] Thêm key captcha69_max1(key dùng cho tất cả acc nha)\n')
    print('------------------------------------------------------------------------------------')
    job= input('hãy điền việc bạn muốn làm: ')

    if job=='1':
        reset('themtaikhoan.txt')
        sl_add= input('Số acc mới muốn thêm vô: ')
        for i in range(int(sl_add)):#get dữ liệu
            account = input(f'[{i+1}] id|pass|2fa(nếu có không thì để trống dưới dạng id|pass|): ')
            add_data(account,'themtaikhoan.txt')

        for i in range(int(sl_add)):#truyền dữ liệu để đăng nhập
            data = get_data(i+1,'themtaikhoan.txt')
            uid = data[0]
            pword= data[1]+'\n'
            ma2fa= data[2]
            key=''
            url = web( uid, pword, ma2fa, key)
            for i in range(3):
                url.x_login()
                print('Đã check')
            check=url.check_login()
            if check =='done':
                print(f'Đã login thành công {uid}')
                add_data(sum_data(data),'account.txt')
                add_data(sum_data(data), 'Nokey_extention.txt')

            if check =='error':
                print(f'Login thất bại thành công {uid}')

    if job=='2':
        id_loi=[]            
        reset('cookieX.txt')
        sl= input('Số tài khoản muốn lấy Cookie: ')
        for i in range(int(sl)):
            num= 1
            data = get_data(i+1,'account.txt')
            uid = data[0]
            pword= data[1]+'\n'
            ma2fa= data[2]
            key=''
            url = web( uid, pword, ma2fa, key)
            url.x_home()
            sleep(1)
            check= url.check_login()
            num=0
            while True:
                if check == 'done':
                    data = url.get_cookie()
                    add_data(data,'cookieX.txt')
                    url.quit()
                    break
                if check == 'error':
                    url.x_login()
                    sleep(3)
                    check= url.check_login()
                    print(f'Thất bại lần {num}')
                    num+=1
                    if num >5:
                        break

    if job=='3':
        key= input('Nhập key trên web của bạn(loại max-1): ')
        f = open('Nokey_extention.txt', 'r')
        size=[]
        print(len(size))
        size=f.readlines()
        f.close()

        for i in range(len(size)+1):
            data = get_data(i+1 , 'Nokey_extention.txt')
            print(data)
            uid = data[0]
            pword= data[1]+'\n'
            ma2fa= data[2]
            url = web( uid, pword, ma2fa, key)

            text= url.check_key_captcha()
            if text =='key_loi':
                a=0
                while a<3: #check key
                    key= input('Nhập key trên web của bạn(loại max-1): ')
                    text= url.check_key_captcha()
                    if text == 'key_done':
                        print('Done')
                        a =4
                    if text == 'key_loi':
                        print('Error key')
                        a+=1

            if text == 'key_done':#add extetion bat key
                url.add_key_captcha()
                reset('Nokey_extetion.txt')
                sleep(1)
                url.quit()
            url.quit()
