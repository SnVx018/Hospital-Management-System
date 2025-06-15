import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Xha34gtoi90laCm",
    database="hospital_system",
    autocommit=True
    
)
from func_library import *




#START MENU
while(True):
    choice=int(input('''CHOOSE 1: FOR A NEW PATIENT TO CREATE ACCOUNT 
                    PRESS 2: TO CONTINUE WITH EXISTING
                    PRESS 3. To exit'''))
    if choice==1:
        patient_registration()
        print("REGISTRATION COMPLETE")
        c1=int(input("Enter 1 to continue or 2 to exit"))
        if c1==2:
            break
    if c1==1 or choice ==2:
        c2=int(input('''SELECT WHAT  YOU WANT TO DO TODAY:
                    1. Make an appointment
                    2. EXIT
                    press 1 or 2 to choose ur option
                  '''))
        if c2==1:
            c3=input('''SELECT THE DEPARTMENT
                        1.Cardiology
                        2.Neurology
                        3.Pediatrics
                        4.Ob/Gyn
                        5.Oncology
                        6.Orthopedics
                        7.Urology
                        8.Dermatology
                        9.Gaastroenterology
                        10.Nephrology
                        11.Pulmonolgy
                 
                        Else type 'E' to exit . ''')
            if c3=="E":
               break
            else:
               a=int(c3)                 
               mycursor.execute("SELECT first_name, last_name,employee_id from employees WHERE dept_id=%s", (a))
               print("Available Doctors in chosen departments")
               for x in mycursor:
                   print(x)
               print("Choose the relevent doctor employee_id")
               c4=int(input())
               print("Choose Available timing by taking the timing_slot")
               mycursor.execute("EXECUTE appointment_booking(%s)", (c4))
        elif c2==2:
            break