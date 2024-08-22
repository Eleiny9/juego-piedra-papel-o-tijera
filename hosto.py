import Matplotlib as plt 

data = np.random.randn(1000)

plt.figure(figsize = (10, 5))

plt.hist(data, bins = 30, alpha = 0.7)

plt.title("Histograma")
plt.show()