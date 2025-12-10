bill = int(input("What is the total bill?"))
tip = int(input("What percent of tip do you want to give?"))
num_of_ppl = int(input("How many people are splitting the bill?"))

total_bill = bill + (tip*bill)/100 
amt_per_person = round(total_bill/num_of_ppl,2)

print(f"Final amount per person is {amt_per_person}")
