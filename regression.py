from sklearn.linear_model import LinearRegression
import numpy as np
import time

# Step 1: Data Input
n = int(input("Enter number of data points: "))

X = []
Y = []

for i in range(n):
    x = input("Enter x: ")
    y = input("Enter y: ")

    # Step 2: Data Cleaning
    if x == "" or y == "":
        print("Missing value removed")
        continue

    x = float(x)
    y = float(y)

    X.append([x])
    Y.append(y)

print("\nCleaned Data:")
for i in range(len(X)):
    print(X[i][0], Y[i])
    time.sleep(0.5)

# Step 3: Preprocessing
X = np.array(X)
Y = np.array(Y)
print("\nPreprocessing Done")
time.sleep(1)

# Step 4: Training
print("\nTraining Model...")
model = LinearRegression()
model.fit(X, Y)
time.sleep(1)

# Step 5: Model Info
b1 = model.coef_[0]
b0 = model.intercept_

print("\nEquation: Y =", b0, "+", b1, "X")
time.sleep(1)

# Step 6: Prediction
px = float(input("\nEnter X: "))
py = model.predict([[px]])

print("Predicted Y =", py[0])