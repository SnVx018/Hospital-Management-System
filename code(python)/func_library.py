import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Xha34gtoi90laCm",
    database="hospital_system",
    autocommit=True
)
mycursor=mydb.cursor()

from datetime import date,datetime,time
  
  

 
    #convert date in string to date time
    
def d_change(s):
    da = date(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
    return da
    

    
    #enter the patients_detail
def patient_registration():
    d=0
    fname=input("Enter Patients first name")
    lname=input("Enter Patients last name")
    B_date_str=input("Enter a date in YYYYMMDD format")
    sex=input("Enter the sex of the patient")
    regd_date=date.today()
    B_date=d_change(B_date_str) 
    if B_date>regd_date:
       d= (B_date-regd_date).days
    else:
            d=(regd_date-B_date).days
    if d>=6570:
            guardian_name=None
            guardian_sex=None
            guardian_birth_date=None
    else:
            guardian_name=input("Enter guardian full name")
            guardian_sex=input("Enter guardian sex")
            guardian_birth_datestr=input("Enter a date in YYYYMMDD format")
            guardian_birth_date=d_change(guardian_birth_datestr)
    phone_no=input("Enter the phone no.")
    mycursor.execute("INSERT INTO patients (firstname, lastname, birth_date, sex, regd_date, guardian_name, guardian_sex, guardian_birth_date,phone_no) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (fname,lname,B_date,sex,regd_date,guardian_name,guardian_sex,guardian_birth_date,phone_no))




#Enter the patient next of kin details
def patient_next_of_kin():
    patient_id=int(input('Enter the patient_id'))
    first_name=input("Enter the first name")
    last_name=input("Enter the last name")
    b_datestr=input("Enter the birth date in YYYYMMDD format")
    sex=input("Enter the gender of the next of kin")
    phone_no=input("Enter the next of kin phone no.")
    nok_b_date=d_change(b_datestr)
    mycursor.execute("INSERT INTO patient_next_of_kin (patient_id, firstname, lastname, birth_date, sex, phone_no) VALUES(%s,%s,%s,%s,%s,%s)", (patient_id, first_name, last_name, nok_b_date,sex, phone_no))



#Enter the departments
def departments():
    dept_name=input("Enter the Department Name")
    mycursor.execute("INSERT INTO departments (department_name) VALUES(%s)", (dept_name))



#Enter the employee details
def employee_registration():
    fname=input("Enter employee first name")
    lname=input("Enter employee last name")
    sex=input("Enter employee sex")
    birth_date_str=input("Enter the employee's birth date in YYYYMMDD format")
    hire_date_str=input("Enter the employee's hire date in YYYYMMDD format")
    birth_date=d_change(birth_date_str)
    hire_date=d_change(hire_date_str)
    dept_id=int(input("Enter department id"))
    phone_no=input("Enter phone no")
    mycursor.execute("INSERT INTO employees (first_name, last_name, sex, birth_date, hire_date, dept_id, phone_no) VALUES(%s,%s,%s,%s,%s,%s,%s)",(fname,lname,sex,birth_date,hire_date,dept_id,phone_no))




#Enter the roles
def roles_input():
     positions=input("Enter the positions")
     mycursor.execute("INSERT INTO roles (positions) VALUES(%s)", (positions))




#Enter employee_roles
def employees_role():
    employee_id=int(input("Enter the employee id"))
    role_id=int(input("Enter the role id"))
    mycursor.execute("INSERT INTO employee_role (employee_id,role_id) VALUES(%s,%s)", (employee_id,role_id))




#Enter employee salary
def employee_salary():
    employee_id=int(input("Enter the employee_id"))
    salary=input(("Enter the employee salary"))
    mycursor.execute("INSERT INTO salary (employee_id,salary) VALUES(%s,%s)", (employee_id,salary))



#Test database
def tests():
    test_name=input("Enter the name of the test")
    mycursor.execute("INSERT INTO test (test_name) VALUES(%s)", (test_name))




#ACESS database input
def accessID():
    patient_id=int("Enter patient_id")
    mycursor.execute("INSERT INTO accessid (patient_ID) VALUES(%s)", (patient_id))




#acess details
def accessdetails():
     access_ID=int("Enter access code/ access id")
     e_id=int("Enter the employee id to be associated with the code")
     mycursor.execute("INSERT INTO accessdetails (access_ID,employee_assigned) VALUES(%s,%s)", (access_ID,e_id)) 


#LAB WORK
def labwork():
     test_id=int("Input the test id of the trst conducted")
     a_id=int("Input the access code")
     test_details=input("Enter the details about the test ")
     mycursor.execute("INSERT INTO lab_work (test_id,access_id,test_details) VALUES(%s,%s,%s)",(test_id,a_id,test_details))




#Rooms
def rooms():
     room_type=input("Enter the roomm type")
     room_status=input("Enter the room status")
     mycursor.execute("INSERT INTO rooms(room_type,room_status) VALUES(%s,%s)",(room_type,room_status))


def roomdata():
     room_id=int(input("Enter the room id/ room number"))
     patient_id=int(input("Enter the patient assigned the room"))
     mycursor.execute("INSERT INTO room_data (room_id,patient_id) VALUES(%s,%s)", (room_id, patient_id))
    



'''
APPPOINTMENT SYSTEM  
1.the entire work day is divided into 15 minute slots. Then
2.Each doctor has a shift in which they work ie they will receive appointments
3.When patient will try to book appointment , firts they will select doctor and only those timing slots will be provided which fall in the doctors shift times
4.Selecting the shift times maybe by their slot id only since this is prelimnary
5.all apointments stored in that time with slot date and doctor in appointments table
'''
def time_convert(s):
    t=time(s[:2],s[2:])
    return (t)
     

def timings():
    start_time_str=(input("Enter start time in HHMM format"))
    end_time_str=(input("Enter end time in HHMM format"))
    start_time=time_convert(start_time_str)
    end_time=time_convert(end_time_str)
    mycursor.execute("INSERT INTO timing_slots (start_time, end_time) VALUES(%s, %s)", (start_time,end_time))



def doctorshifts():
    employee_id=int(input("Enter the employee id of the doctor whose shift time you are setting"))
    shift_start_timestr=(input("Enter shift start time in HHMM format"))
    shift_endt_timestr=(input("Enter shift end time in HHMM format"))
    shift_start_time=time_convert(shift_start_timestr)
    shift_end_time=time_convert(shift_endt_timestr)
    mycursor.execute("INSERT INTO doctor_shift(employee_id,shift_start_time, shift_end_time) VALUES(%s, %s, %s)", (employee_id,shift_start_time,shift_end_time))




def appointments():
     time_slot=int("Enter the time slot (id)")
     booking_date_str=input("Enter the date in YYYYMMDD format")
     booking_date=d_change(booking_date_str)
     booked_doctor=int(input(("Enter the employee id of the booked doctor")))
     patient_id=int(input("Enter the patient_id"))
     mycursor.execute("INSERT INTO appointments(time_slot, booking_date, booked_doctor, patient_id) VALUES(%s, %s,%s,%s)", (time_slot, booking_date, booked_doctor, patient_id))




#CONSULTATIONS giving detail on doctor reports
def consultations():
    patient_id=int("Enter patient id")
    employee_id=int("Enter the doctor id")
    choice=input("Enter Y if there is appointment id else enter N")
    if choice == "Y":
        appointment_id=int(input("Enter appointment id"))
    else:
        appointment_id=None
    consultation_date_str=input("Enter date of consultation in YYYYMMDD format")
    consultation_date=d_change(consultation_date_str)
    consultation_time_str=int("Enter time of consultation in HHMM format")
    consultation_time=time_convert(consultation_time_str)
    consultation_info=None
    mycursor.execute("INSERT INTO consultations(patient_id, employee_id, appointment_id, consultation_date, consultation_time, consultation_info) VALUES(%s, %s,%s,%s,%s,%s)", (patient_id,employee_id,appointment_id,consultation_date,consultation_time,consultation_info))




#PROCEDURES
def procedures():
    procedure_name=input("Enter the the procedure detail")
    patient_id=int(input("Enter the patient id"))
    employee_id=int(input("Enter the Ewmployee id"))
    choice=input("Enter Y if there is consultation id else enter N")
    if choice == "Y":
        consultation_id=int(input("Enter appointment id"))
    else:
        consultation_id=None
    mycursor.execute("INSERT INTO procedures (procedure_name, patient_id, employee_id, consultation_id) VALUES(%s,%s,%s,%s)" , (procedure_name,patient_id,employee_id,consultation_id))



#INVOICE GENERATING SYSTEM
def invoiceid():
    mycursor.execute("INSERT INTO invoiceid VALUES(%s)", (None))




def invoice_details():
    line_item=input("Enter invoice detail(order summary) ")
    invoice_id=int("Enter the invoice id")
    choice=input("Enter Y if there is procedure id else enter N")
    if choice == "Y":
        procedure_id=int(input("Enter appointment id"))
    else:
        procedure_id=None
    mycursor.execute("INSERT INTO invoice_id_detail(line_item,invoice_id,procedure_id) VALUES(%s,%s,%s)", (line_item,invoice_id,procedure_id))




def billing_reg():
    patient_id=int(input("Enter the patient_id"))
    invoice_id=int(input("Enter the invoice id"))
    bill_date=date.today()
    now=datetime.now()
    bill_time=now.time()
    payment_status=("Enter C if payment is complete else type N")
    if payment_status=="C":
        payment_status="COMPLETED"
        payment_date=date.today()
        payment_type=("I for Insurance CC for credit card or C for cash")
    else:
        payment_status="INCOMPLETE"
        payment_date=None
        payment_type=None
    mycursor.execute("INSERT INTO billing(patient_id ,invoice_id, bill_date, bill_time, payment_staus,payment_date,payment_type) VALUES(%s,%s,%s,%s,%s,%s,%s)", (patient_id,invoice_id,bill_date,bill_time,payment_status,payment_date,payment_type))
    