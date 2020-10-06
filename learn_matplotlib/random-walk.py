from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    """随机漫步类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步属性"""
        self.num_points = num_points
        """起始于原点"""
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算所有点"""
        while len(self.x_value) < self.num_points:
            x_step = choice([ 1]) * choice([0, 1, 2, 3, 4,5])
            y_step = choice([ 1]) * choice([0, 1, 2, 3, 4,5])
            self.x_value.append(self.x_value[-1] + x_step)
            self.y_value.append(self.y_value[-1] + y_step)


if __name__ == "__main__":
    rw = RandomWalk(100)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value,
                rw.y_value,
                c=point_numbers,
                cmap=plt.cm.Blues,
                edgecolors='none',
                s=10)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_value[-1],
                rw.y_value[-1],
                c='red',
                edgecolors='none',
                s=50)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

