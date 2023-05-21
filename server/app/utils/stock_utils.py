def calculate_cumulative_return(stock_data):
    initial_value = stock_data[0]["value"]
    final_value = stock_data[-1]["value"]
    return (final_value - initial_value) / initial_value


def calculate_annualized_return(stock_data):
    days = len(stock_data)
    years = days / 365
    cumulative_return = calculate_cumulative_return(stock_data)
    return ((1 + cumulative_return) ** (1 / years)) - 1


def calculate_annualized_volatility(stock_data):
    prices = [d["value"] for d in stock_data]
    returns = []
    for i in range(1, len(prices)):
        returns.append((prices[i] - prices[i-1]) / prices[i-1])
    return sum(returns) / len(returns)