import random

print("Enter the number of friends joining (including you):")
number_of_friends = int(input())

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    name_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number_of_friends):
        name = input()
        name_dict[name] = 0
    total_bill = float(input("Enter the total bill value:\n"))
    split_bill = round(total_bill / number_of_friends, 2)
    for name in name_dict:
        name_dict[name] = split_bill

    print('Do you want to use the "Who is lucky" feature? Write Yes/No:')
    who_is_lucky = input()
    if who_is_lucky.lower() == 'yes':
        lucky_person = random.choice(list(name_dict.keys()))
        print('{} is the lucky one!'.format(lucky_person))
        name_dict[lucky_person] = 0

        remaining_friends = number_of_friends - 1
        new_bill = round(total_bill / remaining_friends, 2)

        for name in name_dict:
            if name != lucky_person:
                name_dict[name] = new_bill

    else:
        print("No one is going to be lucky")
        print(name_dict)
    print(name_dict)

