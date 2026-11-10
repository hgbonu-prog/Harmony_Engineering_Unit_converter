# CTE123 Python Mini Project: Engineering Unit Converter
# This program converts common engineering measurements.
# Extra feature: it keeps a history of successful conversions.

def get_number(prompt):
    """Get a valid numeric value from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def convert_value(choice, value):
    """Convert a value based on the selected conversion."""
    if choice == "1":
        return value / 25.4, "inches"
    elif choice == "2":
        return (value * 9 / 5) + 32, "degrees Fahrenheit"
    elif choice == "3":
        return value * 2.20462, "pounds"
    elif choice == "4":
        return value / 3.6, "metres per second"
    elif choice == "5":
        return value * 25.4, "millimetres"
    elif choice == "6":
        return (value - 32) * 5 / 9, "degrees Celsius"
    elif choice == "7":
        return value / 2.20462, "kilograms"
    elif choice == "8":
        return value * 3.6, "kilometres per hour"
    else:
        return None, None


def show_menu():
    print("\n===== ENGINEERING UNIT CONVERTER =====")
    print("1. Millimetres to Inches")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Kilometres/hour to Metres/second")
    print("5. Inches to Millimetres")
    print("6. Fahrenheit to Celsius")
    print("7. Pounds to Kilograms")
    print("8. Metres/second to Kilometres/hour")
    print("9. View Conversion History")
    print("10. Exit")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
            value = get_number("Enter the value to convert: ")
            result, unit = convert_value(choice, value)

            names = {
                "1": "mm to inches",
                "2": "Celsius to Fahrenheit",
                "3": "kg to pounds",
                "4": "km/h to m/s",
                "5": "inches to mm",
                "6": "Fahrenheit to Celsius",
                "7": "pounds to kg",
                "8": "m/s to km/h"
            }
            print(f"Result: {result:.2f} {unit}")
            history.append(f"{value:g} ({names[choice]}) = {result:.2f} {unit}")

        elif choice == "9":
            print("\n===== CONVERSION HISTORY =====")
            if history:
                for number, item in enumerate(history, start=1):
                    print(f"{number}. {item}")
            else:
                print("No conversions have been recorded yet.")

        elif choice == "10":
            print("Thank you for using the converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 10.")


if __name__ == "__main__":
    main()
