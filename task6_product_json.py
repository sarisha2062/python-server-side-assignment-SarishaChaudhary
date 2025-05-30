import json

with open('product_json.json','r') as file:
    products = json.load(file)
    
print("{:<20}{:<20}{:<20}".format("Name","Price","Quantity"))
print("-"*50)

for items in products:
    print("{:<20}{:<20}{:<20}".format(items['Name'],items['Price'],items['Quantity']))