
# functions with Outputs

def format_name(f_name,l_name):
    if f_name =="" or l_name =="":
        return "bro please enter something"
    name = f_name + " " +l_name
    c_name = name.title()
    return c_name

# f_name = "jayden"
# l_name = "ooi"
# x = format_name(f_name,l_name)
# print(x)

print(
    format_name(
        input("What is you first name: "),
        input("What is you last name: ")
    )
)
