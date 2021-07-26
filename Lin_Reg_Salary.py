import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/Users/19luc/OneDrive/Desktop/Test_01/Salary_Data.csv")

# print(df)
# plt.plot(df["YearsExperience"], df["Salary"])
# plt.show()

x = df.iloc[:, 0].values.reshape(-1, 1)
y = df.iloc[:, 1].values


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)
print(x_test)


Lin = LinearRegression()
Lin.fit(x_train, y_train)
y_pred = Lin.predict(x_test)
print(y_pred)

print(y_test)


acq = np.abs(y_pred - y_test).mean()
print(acq)
