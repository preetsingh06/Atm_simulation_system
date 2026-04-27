from deposit_money import deposit_money
from display_balance import display_balance
from statement import show_statement
from withdraw_money import withdraw_money


def run_atm():
    while True:
        print("\n\n")
        print("|"+ "-"*26 + "|")
        print("|------- ATM Menu : -------|")
        print("|"+ "-"*26 + "|")
        print("|-- 1. Display Balance ----|")
        print("|---2. Deposit Money ------|")
        print("|---3. Withdraw Money -----|")
        print("|---4. Statement ----------|")
        print("|---5. Exit ---------------|")
        print("|"+ "-"*26 + "|")
        
        print()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            display_balance()
        elif choice == "2":
            
            try:
                amount = float(input("\nEnter amount to deposit: ").strip())
                deposit_money(amount)
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("\nEnter amount to withdraw: ").strip())
                withdraw_money(amount)
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == "4":
            show_statement()
        elif choice == "5":
            print("\nThank you for using the ATM.\n")
            break
        else:
            print("\nInvalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    run_atm()
