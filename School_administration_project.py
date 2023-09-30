#           School Administration Program
#1. Entering or asking user to enter Student information.
#2. Pre-processing the collected data. i.e.. Converting the data into a different format that will be easier for us to process.
#3. Writing all the pre-processed data into a File.

import csv

def write_into_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer= csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["NAME" , "AGE", "DOB", "MOBILE NUMBER", "E-MAIL ID"])
        
        writer.writerow(info_list)

if __name__=='__main__':    
    condition=True
    student_num=1
    
    while (condition):
        student_info=input("Enter The Name,Age,DOB,Mobile Number,E-Mail ID for Student {} : ".format(student_num))
        #print("Entered Information: "+student_info)
        
        #split
        student_info_list=student_info.split(' ')               #Split
        #print("Splitted info of students : "+str(student_info_list))
        
        print("\nThe Entered information is : \n Name: {}\n Age: {}\n DOB: {}\n Mobile Number: {}\n EMail-ID: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4]))
        
        choice_check=input("Is entered information correct or not? (yes/no): ")
        if choice_check=="yes":
            write_into_csv(student_info_list)                   #calling function
            
            condition_check=input("Enter (Yes/No) if u want to enter the information for another student: ")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False
            else:
                print("Invalid Input...")
                condition=False
        elif choice_check=="no":
            print("\n Please re-enter the code!!!")