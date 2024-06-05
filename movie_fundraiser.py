##Jennifer Gotschalk 2020 / Mini Movie Fundraiser
name = ""
count = 0
max_tickets = 4
profit= 0

def int_check(question, low_num, high_num):
    error = "Please enter a whole number between {} and {}".format(low_num, high_num)
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low_num <= response <= high_num:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

while name != "xxx" and count < max_tickets:
    print("You have {} seats left".format(max_tickets - count))

    name = input("Name: ")
    if name == "xxx":
        break

    def not_blank(question):
        Valid = False
       
        while not Valid:
            response = input(question)

            if response != "":
                return response
            else:
                print("Sory, this can not be blank.")

    age = int_check("Age: ", 12, 130)
    count += 1
    print()

    if age < 16:
        ticket_price = 8.5
    elif age >= 16 and age < 65:
        ticket_price = 10.50
    else:
        ticket_price = 7.50

    profit_made = ticket_price - 5
    profit += profit_made
    print("{} : ${:.2f}" .format(name, ticket_price))

if count == max_tickets:
    print("You have sold all the available tickets.")
else:
    print("You have sold {} tickets.\nThere are places still available.".format(count))


