# Constants
HST = 0.13
LABOUR_COST = 0.75
RENT_COST = 1
MATERIAL_COST_PER_INCH = 0.5
# 1. Ask for pizza diameter
diameter = game.ask_for_number("Enter diameter (inches):")
# 2. Calculate subtotal
# Formula: (Labour + Rent) + (Material Cost * Diameter)
subtotal = LABOUR_COST + RENT_COST + MATERIAL_COST_PER_INCH * diameter
# 3. Calculate tax and total
tax = subtotal * HST
total = subtotal + tax
# 4. Display the result to the user
game.show_long_text("Subtotal: $" + ("" + str(subtotal)), DialogLayout.BOTTOM)
game.show_long_text("Tax: $" + ("" + str(tax)), DialogLayout.BOTTOM)
game.show_long_text("Total: $" + ("" + str(total)), DialogLayout.BOTTOM)