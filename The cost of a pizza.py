# Constants
HST = 0.13
LABOUR_COST = 0.75
RENT_COST = 1.00
MATERIAL_COST_PER_INCH = 0.50

def main():
    # 1. Input: Ask the user for the diameter
    # Use float() so users can enter decimals (e.g., 12.5)
    try:
        diameter = float(input("Enter the diameter of the pizza in inches: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # 2. Process: The Formulas
    subtotal = (LABOUR_COST + RENT_COST) + (MATERIAL_COST_PER_INCH * diameter)
    tax = subtotal * HST
    total = subtotal + tax

    # 3. Output: Display results formatted to 2 decimal places
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Tax:      ${tax:.2f}")
    print(f"Total:    ${total:.2f}")

# This tells Python to run the main function
if __name__ == "__main__":
    main()