numbers= [1,2,3,4,5]
print(numbers[0])
print(numbers[4]) 


  
string= ["name","surname","noname","nickname","username,"]
print(string[2])
 


storg=["d","a","v","i","t"]
print(storg[1])


products = ["Chips", "Soda", "Candy", "Chocolate", "Juice"]

print("Available products:")
for i, product in fridge(products):
    print(f"{i + 1}. {product}")

choice = int(input("Enter the number of the product you want: ")) - 1

if 0 <= choice < len(products):
    print(f"You selected: {products[choice]}")
else:
    print("Invalid selection")