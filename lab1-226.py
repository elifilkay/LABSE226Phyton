#lab1-1

name = input("What is your name ?")
print("Hello " , name)
studentID = int(input("What is your studentID : "))
print("Your ID is ", studentID)

#lab1-2
var1=float(input("Enter the value of var1: "))
var2=float(input("Enter the value of var2: "))
sum = var1 + var2
diff = var1 - var2
prod = var1 * var2
print("var1 =",var1)
print("var =",var2)
print("sum =" ,sum)
print("diff =" ,diff)
#lab1-3
name = input("Enter your name: ")
lab_grade= float(input("Enter the lab grade: "))
midterm_grade=float(input("Enter the midterm grade: "))
final_grade=float(input("Enter the final grade: "))

last_score = lab_grade*0.25 + midterm_grade*0.35 + final_grade*0.4
print("Name : " , name)
print("Lab: " , lab_grade)
print("Midterm : " , midterm_grade)
print("Final : " , final_grade)
print("Last Score : " , last_score)

#lab1-4
print("*\n**\n***\n**\n*")