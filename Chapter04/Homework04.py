months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]
for month in months:
    if month[0] == "J":
        print(month)

# months_count = 0
# while months_count < 12:
#     if months[months_count][0] == "J":
#         print(months[months_count])
#     months_count = months_count + 1

for number in range(0, 100):
    if number % 2 == 0 and number % 5 == 0:
        print(number)

horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"
for letter in horton:
    if letter in vowels:
        print(letter)
