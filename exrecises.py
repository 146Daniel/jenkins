'''''
fruit = ['apples','1','5','12.5']
print(fruit)
fruit.append("banana")
print(fruit)
fruit.remove("5")
print(fruit)
'''''
'''''

car_brand_dict = {
    'toyota': ["camry", "avalon", "tacoma", "sequoia"],
    'volvo': ["240", "850", "xc90", "s80"],
    'mercedes': ["gle", "eqe", "eqs"]
}

def model_exists(brand, model):
   
    brand = brand.lower() 
    model = model.lower()  
    
    if brand in car_brand_dict:
        return model in [m.lower() for m in car_brand_dict[brand]]
    else:
        return False
    
print(model_exists("toyota", "Camry")) 
print(model_exists("volvo", "XC60"))    
print(model_exists("Mercedes", "eqs"))
print(model_exists("Mercedes", "eQs"))
print(model_exists("Mercedes", "eQx"))

'''''

'''''
x = str.lower(input("Enter a text: "))
print(x)
'''''