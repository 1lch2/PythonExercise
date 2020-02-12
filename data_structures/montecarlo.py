import random
import math
import numpy as np
import matplotlib.pyplot as plt 


# Calculating Pi using Monte Carlo algorithm.
def montecarlo_pi(times:int):
    inside = 0
    total = times

    for i in range(times):
        x_i = random.random()
        y_i = random.random()
        delta = x_i ** 2 + y_i **2 - 1

        if delta <= 0:
            inside += 1
    
    approx_pi = 4 * inside / total
    print('\nRandom test: ' + str(times))
    print('Approximation of pi is:{:.8f}'.format(approx_pi))

    return approx_pi


if __name__ == '__main__':
    numlist = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 30000000, 50000000, 75000000, 100000000]
    x_list = list(np.log10(numlist))
    pi_ = []
    for times in numlist:
        pi_.append(montecarlo_pi(times))

    plt.figure()
    plt.plot([min(x_list), max(x_list)], [math.pi, math.pi], color='red', label='true value')
    plt.plot(x_list, pi_, 'b.-', label='approximation')

    plt.legend()
    plt.xlabel('log10(n)')
    plt.ylabel('pi')

    my_y_ticks = np.arange(3, 3.4, 0.02)
    plt.yticks(my_y_ticks)
    plt.ylim((min(pi_)-0.1, max(pi_)+0.1))

    plt.show()
