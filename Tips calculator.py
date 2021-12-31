print("Welcome to the tip Calculator")

total_bill = input("what is the total bill? ")
new_bill = int(total_bill)
tip = input("What is the tip per person? ")
new_tip = float(tip)
no_person = input("what is the number of persons? ")
newnumber_person = int(no_person)
each_personbill = new_bill/newnumber_person
new_tipbill = each_personbill + new_tip

print(f"your total bill is {new_tipbill}")