def calculate_crack_spread(crude_oil, gasoline, distillates):
    """
    Calculates the 3-2-1 crack spread.
    :param crude_oil: pandas Series, prices of crude oil
    :param gasoline: pandas Series, prices of gasoline
    :param distillates: pandas Series, prices of distillates
    :return: pandas Series, the 3-2-1 crack spread
    """
    return 3 * crude_oil - 2 * gasoline - distillates

def calculate_moving_average(series, window=200):
    """
    Calculates the moving average.
    :param series: pandas Series, input data
    :param window: int, window size for the moving average
    :return: pandas Series, the moving average
    """
    return series.rolling(window=window).mean()

def calculate_volatility(series, window=200):
    """
    Calculates the volatility (standard deviation).
    :param series: pandas Series, input data
    :param window: int, window size for the calculation
    :return: pandas Series, the volatility
    """
    return series.rolling(window=window).std()