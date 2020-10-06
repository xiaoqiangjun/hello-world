from random import randint
import pygal


class Die():
    """表示骰子的类"""
    def __init__(self, num_sides=6):
        """默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """掷骰子"""
        return randint(1, self.num_sides)


if __name__ == "__main__":
    die_1 = Die()
    die_2 = Die()

    results = []
    for _ in range(12000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    for value in range(2, die_1.num_sides + die_2.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print(frequencies)

    hist = pygal.Bar()
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "点数"
    hist.y_title = "频率"
    hist.add('2D6', frequencies)
    hist.render_to_file('2D6.svg')