# Kiambu Dairy Co-op Payment Calculator

## What it does
Calculates total amount owed to farmer based on litres supplied and current buying price.

## How to Run
1. Download both files: dairy_calculator.py and price.txt
2. Keep them in same folder
3. Run: python dairy_calculator.py
4. Enter farmer name and litres

## How to Update Weekly Price
1. Open price.txt in Notepad
2. Delete old price, type new price e.g. 58.5
3. Save file. No need to change code.

Example output:
Farmer : Wafula
Litres : 10.0
Price  : KES 55.00/litre
Total  : KES 550.00

## Files
- dairy_calculator.py - main program
- price.txt - weekly price (manager edits this)

## Assumptions
- Price stored in price.txt
- Tool calculates one farmer at a time
- No history saving in v1.0
