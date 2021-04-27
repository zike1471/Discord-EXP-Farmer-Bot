#Discord EXP Farmer Bot By Jason Mei
#Version 1.0.0
#Alpha phase~



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import math



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main function that calls everything
def mainLoop():
    #Enter information 
    print("Starting DiscordEXPFarmer V.1.0.0")
    kw1 = input("Enter keyword to spam: ")
    email = input("Enter email: ")
    pw = input("Enter password: ")
    spamChannelLink = input("Enter the channel url you want to spam in: ")



    
    #Opens Edge Driver 
    PATH = "C:/Users/Capta/Documents/edgedriver_win64/msedgedriver.exe"
    driver = webdriver.Edge(PATH)
    driver.implicitly_wait(3)
    driver.get(spamChannelLink)
  




    #Sign-in
    def signIn():
        time.sleep(2)
        user = driver.find_element_by_name("email")
        print("Entering email")
        user.send_keys(email)
        time.sleep(1)
        pwS = driver.find_element_by_name("password")
        pwS.send_keys(pw)
        print("Entering password")
        pwS.send_keys(Keys.RETURN)
        print("Login successful")
        time.sleep(5)
    signIn()



    #Exp spam
    def printer():
        #Enter number of messages
        numMessages = int(input("Number of messages to send: "))
        hours = numMessages/60
        exp = 20*numMessages


        
        #Calcualte time it'll take to send
        print("Sending ", end="")
        print(numMessages,end="")
        print(" messages will take about: ",end="")
        print(hours,end="")
        print(" hours.")


        
        #calculate exp gain
        print("You will get about ", end="")
        print(exp,end="")
        print(" exp")


        
        #exp loop
        def infiniteLoop():
            for x in range(1,numMessages+1):
                msgBox = driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div/div/div/div/div/div[3]/div[2]/div")
                msgBox.send_keys(kw1)
                msgBox.send_keys(Keys.RETURN)
                #print progress message
                print("DiscordEXPFarmer V.1.0.0 has searched ",end="")
                print(x,end="")
                print(" out of ",end="")
                print(numMessages,end = "")
                print(" times. ")
                #wait 1 minute 
                time.sleep(60)
        infiniteLoop()
    printer()
mainLoop()
print("DiscordEXPFarmer V.1.0.0 has successfully botted the searches. Enjoy the EXP you filithy farmer! peepoHYPERS!!!")
