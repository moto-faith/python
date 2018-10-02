from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz

iris = load_iris()
data = iris.data
target = iris.target
dtc = DTC(criterion='entropy')
dtc.fit(data,target)


with open('dtc.dot','w')as f:
    export_graphviz(dtc,feature_names=['sepal length', 'sepal width', 'petal length', 'petal width'],out_file=f)


















