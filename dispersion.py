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

# calculate covariance
def calculate_covariance(x, y):
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length")
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))) / len(x)
    return covariance

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, range_ = find_range(donations)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highest, range_))

    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

    std_deviation = calculate_standard_deviation(donations)
    print('The standard deviation of the list of numbers is {0}'.format(std_deviation))

    donations_y = [110, 65, 75, 920, 110, 210, 510, 510, 513, 610, 1010, 1210]
    covariance = calculate_covariance(donations, donations_y)
    print('The covariance of the two lists of numbers is {0}'.format(covariance))