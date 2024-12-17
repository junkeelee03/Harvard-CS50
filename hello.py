
name = input("What's your name? ")

# removing whitespace from name and capitalize name
name = name.strip().title()
# ONLY REMOVES FROM THE LEFT AND RIGHT OF EVERYTHING TYPED, NOT EVERYTHING 
# can string (ironically) functions together

# fstring
print(f"Hello, {name}")

# FUNCTIONS
# usually starts with def main():, and at the end calling back main()
# if you need a return value, it is usually at the end of the function with the command return()
def main(): 
