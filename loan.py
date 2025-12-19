# Loan qualification program

def check_loan_eligibility():
    print("Loan Qualification Checker")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    credit_score=float(input("Enter your credit score: "))
    salary = float(input("Enter your monthly salary: "))
    existing_loan = input("Do you have an existing loan? (yes/no): ")

    if age < 18:
        print(f"Sorry {name}, you must be at least 18 years old to qualify for a loan.")
        return
    
    if existing_loan == "yes":
        print(f"Sorry {name}, you are not eligible as you already have an existing loan.")
        return
    if credit_score < 700: 
        print(f"Sorry {name}, your credit score must be at least 700 to qualify for a loan.")
        return
    
    if salary < 20000:  
        print(f"Sorry {name}, your salary must be at least $2000 to qualify for a loan.")
        return
    print(f"Congratulations {name}! You qualify for a loan.")

check_loan_eligibility()
