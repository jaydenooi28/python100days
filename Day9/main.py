note = {
    "white":"bai",
    "black":"hei",
}
print(note["black"])
# # add item
# note["red"] = "hong"


# # create an empty dict
# empty = {}

# # delete(wipe) the content
# # note = {}

# # edit an item
# note["red"] = "ang"

# # loop 
# # for key in note:
# #     print(key)
# #     print(note[key])


# # nesting a list in a dictionary 
# travel_log1 = {
#     "France": ["Paris","Lille","Dijon"],
#     "Germany":["Berlin","Hamburg"]
# }

# # nexting a dic in a dic 
# travel_log2 = {
#     "France": {"cities_visited":["Paris","Lille","Dijon"],"total_vists":2},
#     "Germany":{"cities_visited":["Berlin","Hamburg"],"total_vists":2}
# }

# # nesting dictionaru in a list 
# travel_log3 = [
#      {"country": "France",
#       "cities_visited":["Paris","Lille","Dijon"],
#       "total_vists":2
#       },


#     {"country": "Germany",
#      "cities_visited":["Berlin","Hamburg"],
#      "total_vists":2
#      }
# ]
# print(travel_log3[1]["country"])