#Science stream results sheet project

#Grade make function
def grade(marks):
    if(marks>=75):
        x="A"
        return x
    elif(marks>=65):
        x="B"
        return x
    elif(marks>=55):
        x="C"
        return x
    elif(marks>=35):
        x="S"
        return x
    else:
        x="F"
        return x                

#Z-score make function
def z_score(subject,marks):
    if(subject.lower()=="combined mathematics"):
        Z=(marks-43.18)/23.94
        return Z
    elif(subject.lower()=="physics"):
        Z=(marks-42.38)/15.68
        return Z
    elif(subject.lower()=="chemistry"):
        Z=(marks-44.10)/17.28
        return Z
    elif(subject.lower()=="biology"):
        Z=(marks-46.07)/15.01
        return Z
    elif(subject.lower()=="information and communication technology"):
        Z=(marks-52)/12
        return Z
    elif(subject.lower()=="agricultural science"):
        Z=(marks-40.61)/11.11
        return Z


print("===Your Examination Results===")
name=str(input("Enter Your Name: "))


print("~...Select Your Subjects...~")
print(">> Combined Mathematics")
print(">> Physics")
print(">> Chemistry")
print(">> Biology")
print(">> Information And Communication Technology")
print(">> Agricultural Science")

subject_01=str(input("Enter your first subject: "))
subject_02=str(input("Enter your second subject: "))
subject_03=str(input("Enter your third subject: "))

while True:
    print("Enter your",subject_01,"marks:",end=" ")
    marks_01=str(input())
    try:
        marks_01=float(marks_01)
        break
    except:
        print("Please Try Again")

while True:
    print("Enter your",subject_02,"marks:",end=" ")
    marks_02=str(input())
    try:
        marks_02=float(marks_02)
        break
    except:
        print("Please Try Again")

while True:
    print("Enter your",subject_03,"marks:",end=" ")
    marks_03=str(input())
    try:
        marks_03=float(marks_03)
        break
    except:
        print("Please Try Again")  

print("~~~",name,",Your Results~~~")
print(" ",subject_01,"-",grade(marks_01))
print(" ",subject_02,"-",grade(marks_02))
print(" ",subject_03,"-",grade(marks_03))

sub_01=z_score(subject_01,marks_01)
sub_02=z_score(subject_02,marks_02)
sub_03=z_score(subject_03,marks_03)

final_z_score=(sub_01+sub_02+sub_03)/3

print(" ","Z-Score-",final_z_score)
exit()




