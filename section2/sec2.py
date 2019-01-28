class Beverage():
    def __init__(self, beverage_name, cost):
        self.name = beverage_name
        self.cost = cost


class Coffee(Beverage):
    def __init__(self, beverage_name, cost, strength):
        super().__init__(beverage_name,cost)
        self.strength = strength

    def stronger_than(self, other_coffee_instance):
        if (self.strength > other_coffee_instance.strength):
            return True
        else:
            return False

    def add_milk(self):
        pass
	  
arabica = Coffee("arabica", 2.0, 4)
robusta = Coffee("robusta", 2.5, 5)

#Is arabica coffee stronger than robusta coffee?

print(arabica.stronger_than(robusta)) 
print(robusta.stronger_than(arabica)) 

class Milk(Beverage):
    def __init__(self):
        pass

#### HELP! I want milk in my coffee:
## 1. Define a subclass Milk of class Beverage. It should inherit all the instance variables, but it 
#     should also have a dairy that is a boolean value (e.g. soy_milk.dairy would probably be False).
#     The default cost for this milk should be 0, but this attribute would be quite useful for fancy
#     milks like almond milk. 
## 2. Write a method that adds milk to your coffee called add_milk. This should take an instance of 
#     Milk class and add its cost to the coffee instance's cost. 
## 3. Create an instance of almond milk and add that to your cup of arabica! 


