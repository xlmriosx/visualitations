import matplotlib.pyplot as plot
import seaborn as sns

iris = sns.load_dataset('iris')

print(iris.head())

sns.jointplot(data=iris, x = 'sepal_length', y = 'petal_length')
plot.show()

sns.scatterplot(data=iris, x = 'sepal_length', y = 'petal_length', hue = 'species')
plot.show()

sns.jointplot(data=iris, x = 'sepal_length', y = 'petal_length', hue = 'species')
plot.show()

sns.jointplot(data = iris, x = 'sepal_width', y = 'petal_width', hue = 'species', palette = 'inferno')
plot.show()

sns.lmplot(data = iris, x = 'sepal_width', y = 'petal_width', hue = 'species', palette = 'dark')
plot.show()

sns.boxplot(x = 'species', y = 'sepal_length', data = iris)
plot.show()

sns.barplot(x = 'species', y = 'sepal_length', data = iris)
plot.show()

