'''Create a module to create following functions
 • percentage
 • result -  based on percentage calculate pass/ fail , use if conditions
 • display – Enrollnment and Name
 Create a main file from which pass total marks and no. Of subjects to percentage function. And 
print Enrollnment, Name, percentage, result(Pass/Fail)'''

def details(eno,name):
    print("Enrollment no:",eno)
    print("Name:",name)

def percentage(total_marks,no_of_subj):
    percent = total_marks/no_of_subj
    print("The result is:",percent)

def result(percent):
    if percent > 35:
        print("You are pass")
    else:
        print("You are fail")