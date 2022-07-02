## Specs

#Receive the following arguments from the user:

#- kilometers to drive
#- liters-per-kilometer usage of the car 
#- price per liter of fuel

#Calculate the cost of the trip and display it to the user in the console.

user_kilometers = int(input("insert kilometers to drive: "))
user_liters_km = int(input("insert litres per km usage of the car: "))
price_litre = int(input("Insert price per litre of fuel: "))

total_litres = user_kilometers * user_liters_km
cost = total_litres * price_litre

print (f"The cost of the trip is {cost} dollars")


