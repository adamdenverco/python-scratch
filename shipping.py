
weight = 4.8
cost = 0
ground_ship_cost = 0
drone_ship_cost = 0

# Ground shipping
if weight <= 2:
  ground_ship_cost += weight * 1.5 + 20
elif weight <= 6:
  ground_ship_cost += weight * 3 + 20
elif weight <= 10:
  ground_ship_cost += weight * 4 + 20
else:
  ground_ship_cost += weight * 4.75 + 20

ground_ship_cost_premium = ground_ship_cost + 105

print("ground: " + str(ground_ship_cost))
print("ground prem: " + str(ground_ship_cost_premium))

# Drone shipping
if weight <= 2:
  drone_ship_cost += weight * 4.5
elif weight <= 6:
  drone_ship_cost += weight * 9
elif weight <= 10:
  drone_ship_cost += weight * 12
else:
  drone_ship_cost += weight * 14.25

print("drone: " + str(round(drone_ship_cost, 2)))

