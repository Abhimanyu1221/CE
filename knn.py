import math
from collections import Counter

# Step 1 - distance function
def euclidean_distance(point1, point2):
    total = 0
    for i in range(len(point1)):
        diff = point1[i] - point2[i]
        total += diff ** 2
    return math.sqrt(total)

# Step 2 - K nearest dhundho
def find_k_nearest(X_train, y_train, new_point, k):
    distances = []
    for i in range(len(X_train)):
        d = euclidean_distance(X_train[i], new_point)
        distances.append((d, y_train[i]))
    distances.sort(key=lambda x: x[0])
    return distances[:k]

# Step 3 - vote karo
def knn_predict(X_train, y_train, new_point, k):
    k_nearest = find_k_nearest(X_train, y_train, new_point, k)
    labels = [label for (distance, label) in k_nearest]
    vote = Counter(labels)
    return vote.most_common(1)[0][0]

# TEST
X_train = [[1,2], [2,3], [3,1], [6,5], [7,7], [8,6]]
y_train = ['A', 'A', 'A', 'A', 'B', 'B']
new_point = [5, 5]
k = 3

print("Predicted:", knn_predict(X_train, y_train, new_point, k))