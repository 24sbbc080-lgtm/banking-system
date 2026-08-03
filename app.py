"""
Loan Eligibility System
Business Rules:
1. Salary must be at least ₹50,000
2. Credit Score must be at least 700
"""

import sys

MIN_SALARY = 50000
MIN_CREDIT_SCORE = 700


def check_loan_eligibility(salary, credit_score):
    """Returns True if customer is eligible for a loan."""
    return salary >= MIN_SALARY and credit_score >= MIN_CREDIT_SCORE


def run_tests():
    print("\n========== Running Automated Tests ==========\n")

    assert check_loan_eligibility(60000, 750) == True
    print("✔ Test 1 (Eligible Customer) - PASSED")

    assert check_loan_eligibility(30000, 750) == False
    print("✔ Test 2 (Low Salary Customer) - PASSED")

    assert check_loan_eligibility(60000, 650) == False
    print("✔ Test 3 (Low Credit Score Customer) - PASSED")

    print("\nAll test cases passed successfully.")
    print("Application is ready for deployment.")


def main():
    print("=" * 50)
    print("        SecureBank Loan Eligibility System")
    print("=" * 50)

    try:
        name = input("Enter Customer Name : ")
        salary = float(input("Enter Monthly Salary (₹): "))
        credit_score = int(input("Enter Credit Score : "))

        print("\n----------- Customer Details -----------")
        print(f"Customer Name : {name}")
        print(f"Monthly Salary: ₹{salary:,.2f}")
        print(f"Credit Score  : {credit_score}")

        print("\n----------- Loan Result -----------")

        if check_loan_eligibility(salary, credit_score):
            print(f" Congratulations {name}!")
            print("You are ELIGIBLE for the loan.")
        else:
            print(f" Sorry {name}.")
            print("You are NOT ELIGIBLE for the loan.")

            if salary < MIN_SALARY:
                print("- Reason: Monthly salary is below ₹50,000.")

            if credit_score < MIN_CREDIT_SCORE:
                print("- Reason: Credit score is below 700.")

    except ValueError:
        print("\nInvalid input! Please enter valid numeric values.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        main()