from random import random
from statistics import mean, median, stdev
from numpy import percentile
from scipy.stats import norm
from matplotlib import pyplot as plt

def getInput():
    # equity = input('Enter the name of the equity: ')
    # price = input('Enter the recent price: ')
    # sdev = input('Enter the standard deviation for a day (volatility): ')
    # months = input('Number of months to project: ')
    # simulations = input('Number of times to run the simulation: ')
    # price = float(price)
    # sdev = float(sdev)
    # months = int(months)
    # simulations = int(simulations)

    equity = 'My portfolio'
    price = 1000
    sdev = 0.0203416
    months = 240
    simulations = 100
    ret = 0.07

    print("Calculating...")

    drift = (ret/12) - (sdev**2)/2
    inputs = [equity, price, sdev, months, simulations, drift]
    return inputs

def analysis(inputs):
# Creating our overall results list
    results = []
    simulation = 0
    while simulation < inputs[4]:
        prices = [inputs[1]]
        new_price = inputs[1]
        count = 0
        while count < inputs[3]:
            ran_num = random()
            norminv = norm.ppf(ran_num, loc = 0, scale = inputs[2])
            new_price = new_price*(1+norminv+inputs[5])
            count += 1
            prices.append(new_price)

        # Adds list of current simulation to overall list of results
        results.append(prices)
        simulation += 1
    #print(results)
    return results

def getStats(results, inputs):
    terminalValues = []
    for i in results:
        terminalValues.append(i[inputs[3]])
    print('Mean: ', mean(terminalValues))
    print('Median: ', median(terminalValues))
    print('Standard deviation: ', stdev(terminalValues))
    print('5%: ', percentile(terminalValues, 5))
    print('95%: ', percentile(terminalValues, 95))
    print('25%: ', percentile(terminalValues, 25))
    print('75%: ', percentile(terminalValues, 75))


def plot(results, inputs):
    months_x = range(0, inputs[3] + 1)
    for y in results:
        price_y = y
        plt.plot(months_x, price_y)
    plt.xlabel('Number of months')
    plt.ylabel('Price')
    plt.title('Monte Carlo Simulation ' + '(' + inputs[0] + ')')
    plt.show()

def main():
    inputs = getInput()
    results = analysis(inputs)
    getStats(results, inputs)
    plot(results, inputs)


if __name__ == '__main__':
    main()
