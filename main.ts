// Constants
let HST = 0.13
let LABOUR_COST = 0.75
let RENT_COST = 1
let MATERIAL_COST_PER_INCH = 0.5
// 1. Ask for pizza diameter
let diameter = game.askForNumber("Enter diameter (inches):")
// 2. Calculate subtotal
// Formula: (Labour + Rent) + (Material Cost * Diameter)
let subtotal = LABOUR_COST + RENT_COST + MATERIAL_COST_PER_INCH * diameter
// 3. Calculate tax and total
let tax = subtotal * HST
let total = subtotal + tax
// 4. Display the result to the user
game.showLongText("Subtotal: $" + ("" + subtotal), DialogLayout.Bottom)
game.showLongText("Tax: $" + ("" + tax), DialogLayout.Bottom)
game.showLongText("Total: $" + ("" + total), DialogLayout.Bottom)
