import matplotlib.pyplot as plt


def show_statistics(b, w):
    y_values = [iteration for iteration in range(len(b))]
    plt.plot(y_values, b, 'g')
    plt.plot(y_values, w, 'r')
    plt.show()
