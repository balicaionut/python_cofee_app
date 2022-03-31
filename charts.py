import matplotlib.pyplot as plt


def method_to_rating_bar(methods):
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)
    axes.bar([1, 2, 3, 4], [3, 5, 7, 25], tick_label=["A", "B", "C", "D"])
    plt.show()