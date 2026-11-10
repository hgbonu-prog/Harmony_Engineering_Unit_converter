# Engineering Unit Converter

## Project Description
The Engineering Unit Converter is a Python program developed for the CTE123 Python Mini Project. It converts common engineering measurements between metric and imperial units.

## Conversions Available
- Millimetres to inches
- Celsius to Fahrenheit
- Kilograms to pounds
- Kilometres per hour to metres per second
- Reverse conversions for all four pairs

## Formulas Used
- Inches = millimetres ÷ 25.4
- Fahrenheit = (Celsius × 9/5) + 32
- Pounds = kilograms × 2.20462
- Metres/second = kilometres/hour ÷ 3.6
- Reverse conversions use the inverse of each formula.

## How to Run
1. Install Python 3.
2. Download this repository.
3. Open a terminal in the project folder.
4. Run: `python engineering_unit_converter.py`

## Sample Output
```text
===== ENGINEERING UNIT CONVERTER =====
1. Millimetres to Inches
2. Celsius to Fahrenheit
3. Kilograms to Pounds
4. Kilometres/hour to Metres/second
5. Inches to Millimetres
6. Fahrenheit to Celsius
7. Pounds to Kilograms
8. Metres/second to Kilometres/hour
9. View Conversion History
10. Exit

Enter your choice: 1
Enter the value to convert: 50
Result: 1.97 inches

Enter your choice: 2
Enter the value to convert: 25
Result: 77.00 degrees Fahrenheit

Enter your choice: 9
===== CONVERSION HISTORY =====
1. 50 (mm to inches) = 1.97 inches
2. 25 (Celsius to Fahrenheit) = 77.00 degrees Fahrenheit
```

## Original Extra Feature
**Conversion History:** The program stores successful conversions during the current session. Users can select option 9 to review them.

## What I Learned
- Defining and calling Python functions
- Using loops and conditional statements
- Accepting and converting numeric input
- Handling invalid input
- Applying unit-conversion formulas in a practical program

## Author
Gbonu harmony kelechi 
ND1 Mechatronics engineering 
Yaba College of Technology (Yabatech)
