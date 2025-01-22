# Find the range bwteen the maximum and minimum values of a list of numbers
def find_range(data):
    lowest = min(data)
    highest = max(data)
    return lowest, highest, highest - lowest

# calculate variance
def calculate_variance(numbers):
    mean = sum(numbers)/len(numbers)
    variance = sum([(x - mean)**2 for x in numbers])/len(numbers)
    return variance

# calculate standard deviation
def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, range = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, range))

    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

    std_deviation = calculate_standard_deviation(donations)
    print('The standard deviation of the list of numbers is {0}'.format(std_deviation))