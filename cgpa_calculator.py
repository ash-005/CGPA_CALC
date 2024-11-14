grades = {'O':10, 'A':9, 'B':8, 'C':7, 'D':6}
creds = []
grade = []
print("-----WELCOME TO GPA CALCULATOR-----")

def calculate_gpa():
    number_of_subjects = int(input("Enter the number of subjects: "))
    for i in range(0,number_of_subjects):
                             grade_obt = input("Enter the grade obtained: ")
                             grade.append(grade_obt)
                             cred = int(input("Enter the credits for the courses: "))
                             creds.append(cred)
    print("GRADES: ",grade)
    print("CREDITS: ",creds)
    for i in range(0,number_of_subjects):
        print(grades[i])
        #if  == grades[i]:
        
ch = 'y'
while ch.lower() == 'y':
    user_choice = int(input("1. CALCULATE GPA\n2. CALCULATE CGPA\n3. EXIT\n"))
    if user_choice == 1:
        calculate_gpa()
    elif user_choice == 2:
        calculate_cgpa()

    else:
        exit()
    ch = input("continue? y/n")
