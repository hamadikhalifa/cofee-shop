from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
c1 = Customer("hamadi")
c2 = Customer("Ekidor")
c3 = Customer("maccellow")
c4 = Customer("david")

# Create coffees
americano = Coffee("Americano")
espresso = Coffee("Espresso")

# Create orders
c1.create_order(americano,7.0)
c1.create_order(espresso,5.5)
c2.create_order(americano,5.0)
c2.create_order(americano,6.4)

# Print customer orders
print(f"{c1.name}'s Orders:")
for order in c1.orders():
    print(f"- {order.coffee.name}: ${order.price}")

print(f"{c2.name}'s Orders:")
for order in c2.orders():
    print(f"- {order.coffee.name}: ${order.price}")

# Print coffee stats
print(f"\n{americano.name} has {americano.num_orders()} orders.")
print(f"Average price for {americano.name}: ${americano.average_price():.2f}")

# Most aficionado for a coffee
most = Customer.most_aficionado(americano)
if most:
    print(f"\nCustomer who spent the most on {americano.name}: {most.name}")
else:
    print(f"No one has ordered {americano.name} yet.")
