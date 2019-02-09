import matplotlib.pyplot as plt

ax1 = plt.subplot(1, 2, 1)
x = [10, 20, 30]
y = [22, 38, 65]
ax1.plot(x, y)
ax1.set(title="Plotting", xlabel="x label")

ax2 = plt.subplot(1, 2, 2)
ax2.bar(["2016", "2017", "2018"], [70, 90, 80])
ax2.plot(100)

plt.show()
