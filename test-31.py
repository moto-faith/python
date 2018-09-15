#岭回归让MSE和theta同时变小，避免过拟合,Lasso回归可筛去一部分特征值
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
x = np.random.uniform(-3.0,3.0,size=100)
X = x.reshape(-1,1)
y = 0.5 *x +3 +np.random.normal(0,1,100)
# plt.scatter(X,y)
# plt.show()

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from  sklearn.linear_model import LinearRegression
def PolynomialRegression(degree):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree)),
        ("std_scaler", StandardScaler()),
        ("lin_reg", LinearRegression())
    ])
from sklearn.model_selection import train_test_split
np.random.seed(666)
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.metrics import mean_squared_error
poly_reg = PolynomialRegression(degree=20)
poly_reg.fit(X_train,y_train)
y_predict = poly_reg.predict(X_test)
print(mean_squared_error(y_test,y_predict))#167.9401087009438过拟合导致MSE过大


def plot_model(model):#调用不同算法的画图模块
    X_plot = np.linspace(-3, 3, 100).reshape(100, 1)
    y_plot = model.predict(X_plot)

    plt.scatter(x, y)
    plt.plot(X_plot[:,0], y_plot, color='r')
    plt.axis([-3, 3, 0, 6])
    plt.show()
plot_model(poly_reg)

#使用Lasso回归
from sklearn.linear_model import Lasso
def LassoRegression(degree, alpha):
    return Pipeline([
        ("poly", PolynomialFeatures(degree=degree)),
        ("std_scaler", StandardScaler()),
        ("ridge_reg", Lasso(alpha=alpha))
    ])
ridge1 = LassoRegression(20,0.01)
ridge1.fit(X_train,y_train)
y1_predict = ridge1.predict(X_test)
print(mean_squared_error(y_test,y1_predict))#1.1496080843259961
plot_model(ridge1)


ridge2_reg = LassoRegression(20, 0.1)
ridge2_reg.fit(X_train, y_train)
y2_predict = ridge2_reg.predict(X_test)
print(mean_squared_error(y_test, y2_predict))#1.1213911351818648
plot_model(ridge2_reg)
