# WRITE YOUR FUNCTIONS HERE

#1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#3
def add_or_remove_cash(pet_shop,cash):
     pet_shop["cash"].append(cash)

#5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#7
def get_stock_count(customer):
    return len(customer["pets"])

#8/9
def get_pets_by_breed(pet_shop, breed):
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            return pet
    



#10/11
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    else:
        return None
    
#12

#13
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


#14
def get_customer_cash(customer):
    return customer["cash"]

#15

#16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#17
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)