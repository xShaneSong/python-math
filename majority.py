'''
Calculate the majority element in a list of numbers
'''

from collections import Counter

# Calculate the majority element in a list of numbers
def calculate_majority(numbers):
    c = Counter(numbers)
    return c.most_common(1)[0][0]

# Frequency table for a list of numbers
def frequency_table(numbers):
    table = Counter(numbers)
    for number in table.most_common():
        print('{0}\t{1}'.format(number[0], number[1]))

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    majority = calculate_majority(donations)
    print('The majority of the list of numbers is: {0}'.format(majority))

    frequency_table(donations)