import time
import getpass
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#import subprocess
print("Thank You for choosing Bio-Informatics Google Meet Automatic Entry-GMAE!, Developer: Himanshu Girdhar")
options=Options()
o=getpass.getuser()
k=open("c:\\Users\\"+o+"\\BIGMAE_dir.txt","r")
global m
m=k.read()
k.close()
b=open(m+":/BIGMAE/gchrome_profile.txt","r")
gmeet_links=open(m+":/BIGMAE/gmeet_links.txt","r")
gmeet_links.seek(0)
f_line=gmeet_links.readline().strip() #omics
s_line=gmeet_links.readline().strip() #bda
t_line=gmeet_links.readline().strip() #ssce
iv_line=gmeet_links.readline().strip() #sbis
v_line=gmeet_links.readline().strip() #sdsa
vi_line=gmeet_links.readline().strip()
gmeet_links.close()
b.seek(0)
if b.read()=="":
    h=open(m+":/BIGMAE/gchrome_profile.txt","w")
    h.write("Profile "+ input("Please Enter Google Chrome IIITA profile number\t"))
    h.close()
b.seek(0)
global a
a=b.read().strip()
b.close()
def click1():
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[11]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span")))
    except:
        driver.quit()
        schedule()
        return
    button = driver.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[11]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div[1]")
    button.click()
    button = driver.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[11]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]")
    button.click()
    button = driver.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[11]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span")
    button.click()
    t=input("do yo want to attend different class?(y/n) \t")
    if t=="y" or t=="Y":
        driver.quit()
        notschedule()
    quit_d()
    return
def click2():
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/c-wiz/div/div/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a"))) 
    except:
        driver.quit()
        schedule()
        return
    button = driver.find_element(By.XPATH,"/html/body/c-wiz/div/div/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a")
    button.click()
    driver.switch_to.window(driver.window_handles[1])
    click1()
    return
def browser_c():
    options.add_argument("user-data-dir="+m+":/BIGMAE")
    #To prevent Selenium driven WebDriver getting detected a niche approach would include either/all of the below mentioned steps:
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"]) #work can only be done with only this
    
    options.add_argument(r"--profile-directory="+a)
    #options.add_argument("--disable-extensions") to disable all extensions
    options.add_argument("--disable-dev-shm-usage") # dev warnings will be disabled
    #options.add_argument("--no-sandbox")    may be my script will be considered as a malware to overcome i had used this command
    '''The sandbox is a C++ library that allows the creation of sandboxed processes — processes that execute within a very restrictive environment. The only resources sandboxed processes can freely use are CPU cycles and memory. For example, sandboxes processes cannot write to disk or display their own windows. What exactly they can do is controlled by an explicit policy. Chromium renderers are sandboxed processes.

    Functionally sandbox limits the severity of bugs in code running inside the sandbox. Such bugs cannot install persistent malware in the user‘s account (because writing to the filesystem is banned). Such bugs also cannot read and steal arbitrary files from the user’s machine.

    (In Chromium, the renderer processes are sandboxed and have this protection. After the NPAPI removal, all remaining plugins are also sandboxed. Chromium renderer processes are isolated from the system, but not yet from the web. Therefore, domain-based data isolation is not yet provided.'''
    s=Service(m+':\\BIGMAE\\chromedriver.exe')
    #options.add_experimental_option("detach", True)  The experimental option detach is what will keep the browser open
    global driver
    driver = webdriver.Chrome(service=s, options=options)
    driver.maximize_window()
def quit_d():
    #print("Do you want to kill chrome open by BIGMAE(BEST PRACTICE TO DO AFTER YOU USE THE SOFTWARE)?(y/n)")
    #g=input()
    #if g=="y" or g=="Y":
        #driver.quit()
    #subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
    #print("Do you want to kill all chrome instances?")
    #g=input()
    #if g=="y" or g=="Y":
        #subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
    print("Don't close this window! Untill you are done with chrome instance opened by BIGMAE as this will close the chrome also")
def notschedule():
    if 1==1:
        print("1. OMICS")
        print("2. SBDA")
        print("3. SSCE")
        print("4. SBIS")
        print("5. SDSA")
        print("6. Custom Class link NOTE:if a class link is added click on join manually rest software will take care otherwise just do the default")
        print("7. exit")
        for i in range(10):
            x=input("Enter your choice:\t")
            if x=="1":
                browser_c()
                driver.get(f_line)
                click1()
                break
            elif x=="2":
                browser_c()
                driver.get(s_line)
                click2()
                break
            elif x=="3":
                browser_c()
                driver.get(t_line)
                click2()
                break
            elif x=="4":
                browser_c()
                driver.get(iv_line)
                click2()
                break
            elif x=="5":
                browser_c()
                driver.get(v_line)
                click1()
                break
            elif x=="6":
                if vi_line=="":
                    print("Please add the class in g_meet.txt at the end")
                    break
                else:
                    browser_c()
                    driver.get(vi_line)
                    time.sleep(6)
                    driver.switch_to.window(driver.window_handles[1])
                    click1()
                    break
            elif x=="7":
                break
            else:
                print("Wrong input Please try again")

def schedule():
    if datetime.today().isoweekday()==1:
        if int(datetime.now().strftime("%H%M"))<1049 and int(datetime.now().strftime("%H%M"))>830 :
            browser_c()
            driver.get(s_line)
            click2()
            return
        elif int(datetime.now().strftime("%H%M"))<1245 and int(datetime.now().strftime("%H%M"))>1050 :
            browser_c()
            driver.get(f_line)
            click1()
            return
        elif int(datetime.now().strftime("%H%M"))>1430 and int(datetime.now().strftime("%H%M"))<1645 :
            browser_c()
            driver.get(t_line)
            click2()
            return
        else:
            print("No lecture at this time according to general schedule.. Please select any from the list")
            notschedule()
            return
    elif datetime.today().isoweekday()==2:
        if int(datetime.now().strftime("%H%M"))<1049 and int(datetime.now().strftime("%H%M"))>830 :
            browser_c()
            driver.get(v_line)
            click1()
            return
        elif int(datetime.now().strftime("%H%M"))<1245 and int(datetime.now().strftime("%H%M"))>1050 :
            browser_c()
            driver.get(f_line)
            click1()
            return
        elif int(datetime.now().strftime("%H%M"))>1430 and int(datetime.now().strftime("%H%M"))<1700 :
            browser_c()
            driver.get(s_line)
            click2()
            return
        else:
            print("No lecture at this time according to general schedule.. Please select any from the list")
            notschedule()
            return
    elif datetime.today().isoweekday()==3:
        if int(datetime.now().strftime("%H%M"))<1049 and int(datetime.now().strftime("%H%M"))>830 :
            browser_c()
            driver.get(s_line)
            click2()
            return
        elif int(datetime.now().strftime("%H%M"))<1245 and int(datetime.now().strftime("%H%M"))>1050 :
            browser_c()
            driver.get(t_line)
            click2()
            return
        elif int(datetime.now().strftime("%H%M"))>1430 and int(datetime.now().strftime("%H%M"))<1645 :
            browser_c()
            driver.get(v_line)
            click1()
            return
        else:
            print("No lecture at this time according to general schedule.. Please select any from the list")
            notschedule()
            return
    elif datetime.today().isoweekday()==4:
        if int(datetime.now().strftime("%H%M"))<1049 and int(datetime.now().strftime("%H%M"))>830 :
            browser_c()
            driver.get(iv_line)
            click2()
            return
        elif int(datetime.now().strftime("%H%M"))<1245 and int(datetime.now().strftime("%H%M"))>1050 :
            browser_c()
            driver.get(v_line)
            click1()
            return
        elif int(datetime.now().strftime("%H%M"))>1430 and int(datetime.now().strftime("%H%M"))<1645 :
            browser_c()
            driver.get(t_line)
            click2()
            return
        else:
            print("No lecture at this time according to general schedule.. Please select any from the list")
            notschedule()
            return
    elif datetime.today().isoweekday()==5:
        if int(datetime.now().strftime("%H%M"))<1049 and int(datetime.now().strftime("%H%M"))>830 :
            browser_c()
            driver.get(iv_line)
            click2()
            return
        elif int(datetime.now().strftime("%H%M"))<1245 and int(datetime.now().strftime("%H%M"))>1050 :
            browser_c()
            driver.get(f_line)
            click1()
            return 
        elif int(datetime.now().strftime("%H%M"))>1430 and int(datetime.now().strftime("%H%M"))<1645 :
            browser_c()
            driver.get(iv_line)
            click2()
            return
        else:
            print("No lecture at this time according to general schedule.. Please select any from the list")
            notschedule()
            return
    else:
        print("No lecture at this time according to general schedule.. Please select anyone from the list.\n")
        notschedule()
        return
def main():
    schedule()
if __name__=="__main__":
    main()
