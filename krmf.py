from sklearn.ensemble import RandomForestClassifier
import numpy as np
import time

# Step 1: Input
n = int(input("Enter number of data points: "))

X = []
Y = []

for i in range(n):
    x = input("Enter value: ")
    c = input("Enter class: ")

    # Step 2: Cleaning
    if x == "" or c == "":
        print("Invalid data removed")
        continue

    X.append([int(x)])
    Y.append(c)

print("\nCleaned Data:")
for i in range(len(X)):
    print(X[i], Y[i])
    time.sleep(0.5)

# Step 3: Preprocessing
X = np.array(X)
Y = np.array(Y)
print("\nPreprocessing Done")
time.sleep(1)

# Step 4: Training
print("\nTraining Random Forest...")
model = RandomForestClassifier(n_estimators=3)
model.fit(X, Y)
time.sleep(1)

# Step 5: Prediction
px = int(input("\nEnter new value: "))

print("\nPredicting...")
result = model.predict([[px]])

print("Final Class =", result[0])
time.sleep(1)

# Step 6: Tree-wise output
print("\nTree Votes:")
for i, tree in enumerate(model.estimators_):
    print("Tree", i+1, "→", tree.predict([[px]])[0])
    time.sleep(1)