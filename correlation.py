import matplotlib.pyplot as plt

# 计算相关系数
# 这个函数的目的是计算两个列表 x 和 y 之间的皮尔逊相关系数。皮尔逊相关系数是一个度量两个变量之间线性关系的统计量，取值范围在 -1 到 1 之间。
def find_corr_x_y(x, y):
    # 如果列表 x 和 y 的长度不相等，抛出 ValueError 异常
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length")
    
    n = len(x)  # 获取列表的长度
    prod = [xi*yi for xi, yi in zip(x, y)]  # 计算 x 和 y 对应元素的乘积
    sum_prod_x_y = sum(prod)  # 计算乘积的和
    sum_x = sum(x)  # 计算 x 的和
    sum_y = sum(y)  # 计算 y 的和
    squared_sum_x = sum_x ** 2  # 计算 x 的和的平方
    squared_sum_y = sum_y ** 2  # 计算 y 的和的平方
    x_square = [xi**2 for xi in x]  # 计算 x 的每个元素的平方
    y_square = [yi**2 for yi in y]  # 计算 y 的每个元素的平方
    x_square_sum = sum(x_square)  # 计算 x 的平方和
    y_square_sum = sum(y_square)  # 计算 y 的平方和
    
    # 计算分子
    numerator = n*sum_prod_x_y - sum_x*sum_y
    # 计算分母的第一部分
    denominator_term1 = n*x_square_sum - squared_sum_x
    # 计算分母的第二部分
    denominator_term2 = n*y_square_sum - squared_sum_y
    # 计算分母
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    # 计算相关系数
    correlation = numerator / denominator
    
    return correlation

def scatter_plot(x, y):
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 4, 5, 6]
    corr = find_corr_x_y(x, y)
    print('The correlation coefficient is: {0}'.format(corr))
    scatter_plot(x, y)

    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    corr = find_corr_x_y(x, y)
    print('The correlation coefficient is: {0}'.format(corr))

    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    corr = find_corr_x_y(x, y)
    print('The correlation coefficient is: {0}'.format(corr))
