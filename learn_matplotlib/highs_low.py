import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'learn_matplotlib/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # for index, col_header in enumerate(header_row):
    #     print(index, col)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', linewidth=0.5)
plt.plot(dates, lows, c='blue', linewidth=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.margins(x=0)
plt.title("气温变化（2014）", fontproperties="SimSun", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("温度（F）", fontproperties="SimSun", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()