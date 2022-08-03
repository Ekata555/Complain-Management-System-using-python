print("***********************************************************************************************")
print("*************************Complaint Management System For Department****************************")
print("***********************************************************************************************")
from datetime import datetime
now=datetime.now()
date_time=now.strftime("%d/%m/%Y,%H:%M:%S")
print("##############################",date_time,"############################################")

class Student_Details:

    def student_complain(self,complain_box):
        self.S_Name     = input("Enter Your  Name    :")
        self.S_RollNo   = input("Enter Your RollNo   :")
        self.S_Branch   = input("Enter Your Branch   :")
        self.S_Year     = input("Enter Your  Year    :")
        self.S_Gender   = input("Enter Your Gender   :")
        self.S_MobileNo = input("Enter Your MobileNo :")
        self.S_EmailID  = input("Enter Your EmailID  :")
        self.S_complain =input("Enter Your Complain  :")
        complain_box[self.S_Name]=self.S_RollNo,self.S_Branch,self.S_Year,self.S_Gender,self.S_MobileNo,self.S_EmailID,self.S_complain

        
        print("***********Complain Record Added****************************************")
class Parent_Details:
    def parent_complain(self, complain_box):
        self.P_Name     = input("Enter Your  Name    :")
        self.P_MobileNo = input("Enter Your MobileNo :")
        self.P_complain = input("Enter Your Complain :")
        complain_box[self.P_Name] = self.P_MobileNo,self.P_complain
        print("********Complain Record Added*********************************************")

class Faculty(Parent_Details,Student_Details):
    def show(self,complain):
        print("***************************************************************************")
        print("***Student complaints and Parent complaints registered successfully!!!*****")
        print("***************************************************************************")
        
        for key,value in complain.items():
            print(key,value)
            print('\n')
            
            

F=Faculty()
complain_box = {}
while(True):

    print("1.Student")
    print("2.Parent")
    print("3.Faculty")
    print("4.Exit")
    choice = int(input("Who you are!!\U0001F914"))
    if (choice == 1):
        F.student_complain(complain_box)
    elif choice == 2:
        F.parent_complain(complain_box)
    elif choice==3:
        F.show(complain_box)
    else:
        break
