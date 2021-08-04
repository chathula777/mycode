#!/usr/bin/python3
import math
import os
print('''
************************************************************************
*                                                                      *
*  WELCOME TO NEW JERSEY DEPARTMENT OF LABOR AND WORKFORCE DEVELOPMENT *
*                                                                      *
************************************************************************
\n''')

name = input("Please enter your Name: \n").title()

residence = input("Have you maintained your permanent home in New Jersey for more than 12 months? Please Enter Yes or No  \n").title()

if residence == "No":
    print(f"Hi {name}! You do not qualify for New Jersey Unemployment Payments at this time. Please check with us again in the future.")
    exit()
else:
    print('''

   ***********************************************************************************
   *                                                                                 *
   * Please check our latest schedule for cerifying for your unexmployment benefits  *
   *                                                                                 *
   ***********************************************************************************
    \n''')


ssn =int(input("Please enter the last four digits of your Social Security Number: \n "))


weekly_income = float(input("What was your weekly income before you lost your last employment? \n "))

unemployment_payment =(round(weekly_income * 0.70))
    

        

    
while weekly_income != 0:
         

        if (0000 <= ssn <= 1999):
            print(f"Hi {name}  Please file your unemployment claim on ***SUNDAY*** between 8a.m and 5p.m on on www.myunemployment.nj.gov. Your estimated weekly unemployment payment will be ${unemployment_payment}")
            break
        elif  (2000 <= ssn <= 3999):
            print(f"Hi {name}! Please file your unemployment claim on ***MONDAY*** between 8a.m and 5p.m on on www.myunemployment.nj.gov. Your estimated weekly unemployment payment will be ${unemployment_payment} ")
            break
        elif  (4000 <= ssn <= 5999):
            print(f"Hi {name}! Please file your unemployment claim on ***TUESDAY*** between 8a.m and 5p.m on on www.myunemployment.nj.gov. Your estimated weekly unemployment payment will be ${unemployment_payment} ")
            break
        elif  (6000 <= ssn <= 7999):
            print(f"Hi {name}!  Please file your unemployment claim on ***WEDNESDAY*** between 8a.m and 5p.m on on www.myunemployment.nj.gov. Your estimated weekly unemployment payment will be ${unemployment_payment} ")
            break
        elif  (8000 <= ssn <= 9999):
            print(f"Hi {name}! Please file your unemployment claim on ***THURSDAY***  between 8a.m and 5p.m on on www.myunemployment.nj.gov. Your estimated weekly unemployment payment will be ${unemployment_payment}")
            break
        else:              
            print("Please enter a valid social security number in XXXX format. Number must be between 0001 and 9999 !")
            break
    


