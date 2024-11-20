def vending_machine():
    products = {
        1: "სნიკერსი",
        2: "კიტკატი",
        3: "ლეისი",
        4: "დორნიტო",
        5: "მარშმელო"
    }
    
    print("საიდუმლო ვენდინგ მანქანა")
    print("აირჩიეთ პროდუქტი ნომრით:")
    
    for key, value in products.items():
        print(f"{key}: {value}")
    
    choice = int(input("შეიყვანეთ პროდუქტის ნომერი: "))
    
    if choice in products:
        print(f"თქვენ აირჩიეთ: {products[choice]}")
    else:
        print("არასწორი არჩევანი")


vending_machine()
