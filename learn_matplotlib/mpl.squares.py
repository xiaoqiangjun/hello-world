import matplotlib.pyplot as plt

x = range(1, 6)
square = [i**2 for i in x]
plt.plot(x, square, linewidth=5)
plt.title("平方数", fontsize=24, fontproperties="SimSun")
plt.xlabel("数", fontsize=24, fontproperties="SimSun")
plt.ylabel("平方", fontsize=24, fontproperties="SimSun")
plt.tick_params(axis='both', labelsize=14)  
plt.show()