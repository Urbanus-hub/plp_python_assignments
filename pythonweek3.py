# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
	"""
	Calculates the final price after applying a discount.
	If the discount is 20% or higher, applies the discount.
	Otherwise, returns the original price.
	"""
	if discount_percent >= 20:
		discount_amount = price * (discount_percent / 100)
		return price - discount_amount
	else:
		return price

# Prompt the user to enter the original price and discount percentage
try:
	price = float(input("Enter the original price of the item: "))
	discount_percent = float(input("Enter the discount percentage: "))
	# Calculate the final price using the function
	final_price = calculate_discount(price, discount_percent)
	# Print the result
	if discount_percent >= 20:
		print(f"Final price after {discount_percent}% discount: {final_price}")
	else:
		print(f"No discount applied. Final price: {final_price}")
except ValueError:
	print("Invalid input. Please enter numeric values.")