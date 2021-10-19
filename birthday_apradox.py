import datetime, random

def get_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a

print('''The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct',
          'Nov', 'Dec')

while True:
    print("How many birthdays should i generate (max 100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_b_days = int(response)
        break
print()

print('Here are', num_b_days, 'birthdays:')
birthdays = get_birthdays(num_b_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = months[birthday.month - 1]
    date_text = '{} {}'.format(month_name, birthday.day)
    print(date_text, end='')
print()
print()

match = get_match(birthdays)

print('In this simulation, ', end='')
if match != None:
    month_name = months[match.month - 1]
    dateText = '{} {}'.format(month_name, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

print('Generating', num_b_days, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
        birthdays = get_birthdays(num_b_days)
        if get_match(birthdays) != None:
            simMatch = sim_match + 1
print('100,000 simulations run.')