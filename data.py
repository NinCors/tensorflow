import sys
sys.path
print(sys.path)
sys.path.append('/Library/Python/2.7/site-packages/')
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
