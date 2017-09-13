import json, sys

# calculate price for each item in a cart
def calculateItemPrice(item, data_price):
	# get item options 
	option = item['options']

	# loop price list to find item price
	for price in data_price:
		if price['product-type'] == item['product-type']:
			hasOption = True
			# compare Key-value pairs of strings
			for opt, val in price['options'].items():
				if option[opt] not in val:
					hasOption = False
					break
			# if all options satisfy item options, item price found
			if hasOption: 
				# found item 'base_price' in price list
				base_price = price['base-price']
				break

	artist_markup = item['artist-markup']
	quantity = item['quantity']
				
	# calculate (base_price + round(base_price * artist_markup)) * quantity
	return (round(artist_markup / 100 * base_price) + base_price) * quantity

if __name__ == "__main__":

	if len(sys.argv) != 3:
		print("usage: python main.py cart-4560.json base-prices.json")
		exit(1)
	else:
		cart_file = sys.argv[1]
		price_file = sys.argv[2]

	# read cart data and price data
	with open(cart_file) as data_file:
		data_cart = json.load(data_file)

	with open(price_file) as data_file:
		data_price = json.load(data_file)

	total = 0
	for cart in data_cart:
		print(calculateItemPrice(cart))
		total += calculateItemPrice(cart)
	print(total)

