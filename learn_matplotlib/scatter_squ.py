import matplotlib.pyplot as plt

x = list(range(1, 1001))
square = [i**2 for i in x]
plt.scatter(x, square, s=5, c=x, cmap=plt.cm.Greens, edgecolors='none')
plt.title("平方数", fontsize=24, fontproperties="SimSun")
plt.xlabel("数", fontsize=14, fontproperties="SimSun")
plt.ylabel("平方", fontsize=14, fontproperties="SimSun")
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('3q.png', bbox_inches='tight')
