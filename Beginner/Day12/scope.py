################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")# return 2

# increase_enemies()
# print(f"enemies outside function: {enemies}")# return 1

# # local scope

# def drink_potion():
#   potion_strength =2
#   print (potion_strength)
# drink_potion()
# # returns 2

# print (potion_strength)
# # return error

# Gloval Scope
# player_health = 10 

# def drink_potion():
#   potion_strength = 2
#   print (player_health)
# # returns 10

# modify global scope

enemies = 1
def increase_enemies():

  print(f"enemies inside function: {enemies}")# return 2
  return enemies + 1 

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")# return 1