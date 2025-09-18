from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Nicky's Ice cream shop"
owner_name = "Nicolle Tomas"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Vanilla", "Chocolate", "Pistachio"]
beverages = ["Avocado", "Strawberry"]

# Tuple data type
business_hours = ("9:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Vanilla": 75.00,
    "Chocolate": 75.00,
    "Pistachio": 80.00,
    "Avogado": 80.00,
    "Strawberry": 80.00
}

# Stock data type (list for each product)
stocks = [15, 30, 20, 50, 40]  # example values


# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Vanilla']:.2f}", target="price1")
display(f"{stocks[0]} pcs", target="stock1")
display(product_names[1], target="prod2")
display(f"₱{menu['Chocolate']:.2f}", target="price2")
display(f"{stocks[0]} pcs", target="stock2")
display(product_names[2], target="prod3")
display(f"₱{menu['Pistachio']:.2f}", target="price3")
display(f"{stocks[0]} pcs", target="stock3")
display(beverages[0], target="prod4")
display(f"₱{menu['Avogado']:.2f}", target="price4")
display(f"{stocks[0]} pcs", target="stock4")
display(beverages[1], target="prod5")
display(f"₱{menu['Strawberry']:.2f}", target="price5")
display(f"{stocks[0]} pcs", target="stock5")


# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in Available", target="orderType")