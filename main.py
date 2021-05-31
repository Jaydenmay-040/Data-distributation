
import matplotlib.pyplot as plt
x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220.00, 330.00, 190.00, 340.00, 410.00, 445.00, 415.00]
# labeling and visuals
plt.xlabel("Temperatures(Degrees Celsius)")
plt.ylabel("Price in Rands(R)")
plt.title("Soup sales in relation to temperature")
plt.scatter(x, y)
plt.show()
