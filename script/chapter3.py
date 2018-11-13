#3.2.2 ステップ関数の実装
def step_function_proto(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function(x):
    y = x > 0
    return y.astype(np.int)

import numpy as np
x = np.array([-1.0, 1.0, 2.0])
x
y = x > 0
y
y = y.astype(np.int)
y

#3.2.3 ステップ関数のグラフ
import matplotlib.pylab as plt

def step_function(x):
   return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)

#3.2.4 シグモイド関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
sigmoid(x)

t = np.array([1.0, 2.0, 3.0])
1.0 + t
1.0 / t

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)

#3.2.7 ReLU関数
def relu(x):
    return np.maximum(0, x)

#3.3.1 多次元配列
A = np.array([1, 2, 3, 4])
print(A)
np.ndim(A)
A.shape
A.shape[0]

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
np.ndim(B)
B.shape

#行列の積
A = np.array([[1, 2], [3, 4]])
A.shape
B = np.array([[5, 6], [7, 8]])
B.shape
np.dot(A,B)
A = np.array([[1, 2, 3], [4, 5, 6]])
A.shape
B = np.array([[1, 2], [3, 4], [5, 6]])
B.shape
np.dot(A, B)

C = np.array([[1, 2], [3, 4]])
C.shape
A.shape
np.dot(A, C)
A = np.array([[1, 2], [3, 4], [5, 6]])
A.shape
B = np.array([7, 8])
B.shape
np.dot(A, B)

#3.3.3 ニューラルネットワークの行列の積
X = np.array([1, 2])
X.shape
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W)
W.shape
Y = np.dot(X, W)
print(Y)

#3.4.2 各層における信号伝達の実装
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1

Z1 = sigmoid(A1)

print(A1)
print(Z1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

#3.4.3 3層ニューラルネットワークの実装まとめ
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)

#3.5.1 恒等関数とソフトマックス関数
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a)
print(exp_a)

sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

def sotmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

#3.5.2 ソフトマックス関数の実装上の注意
a = np.array([1010, 1000, 990])
np.exp(a) / np.sum(np.exp(a))
c = np.max(a)
a - c

np.exp(a - c) / np.sum(np.exp(a - c))


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

#3.5.3 ソフトマックス関数の特徴
a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
np.sum(y)

#3.5.4 出力層のニューロンの数
import sys, os
os.getcwd()
os.chdir('script')
sys.path.append(os.pardir)
from others.mnist import load_mnist

#3.6.1 MNISTデータセット
(x_train, t_train), (x_test, t_test) = \
    load_mnist(flatten = True, normalize = False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    plt.imshow(pil_img)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)
img_show(img)

#3.6.2 ニューラルネットワークの推論処理
import pickle
def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize = True, flatten = True, one_hot_label = False)
    return x_test, t_test

def init_network():
    with open("../others/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p = np.argmax(y)
    if p == t[i]:
        accuracy_cnt += 1

print(f"Accuracy : {str(float(accuracy_cnt) / len(x))}")

#3.6.3 バッチ処理
x, _ = get_data()
network = init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']

x.shape
x[0].shape
W1.shape
W2.shape
W3.shape

#バッチ処理実装
x, t = get_data()
network = init_network()

batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis = 1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print(f"Accuracy : {str(float(accuracy_cnt) / len(x))}")


x = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.8, 0.1, 0.1]])
y = np.argmax(x, axis = 1)
print(y)

y = np.array([1, 2, 1, 0])
t = np.array([1, 2, 0, 0])
print(y == t)
np.sum(y == t)
