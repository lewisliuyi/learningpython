import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST 数据集相关的常数
INPUT_NODE = 784
OUTPUT_NODE =10

#配置神经网络的参数
LAYER1_NODE=500
BETCH_SIZE=100
LEARNING_RATE_BASE=0.8
LEARNING_RATE_DECAY=0.99
REGULARIZATION_RATE=0.0001
TRAINING_STEPS=30000
MOVING_AVERAGE_DECAY=0.99

#一个辅助函数，给定神经网络的输入和所有参数，计算神经网络的前向传播过程
def inference(input_tensor,avg_class,weights1,biases1,weights2,biases2):
    #当没有提供滑动平均类时，直接使用参数当前的取值。
    if avg_class == None:
        #计算隐藏层的前向传播结果，这里使用了ReLU激活函数。
        layer1=tf.nn.relu(tf.matmul(input_tensor,weights1)+biases1)

        #计算输出层的前向传播结果
        return tf.matmul(layer1,weights2)+biases2
    else:
        #首先使用avg_class.average函数来计算得出变量的滑动平均值,然后再计算相应的神经网络前向传播结果
        layer1=tf.nn.relu(tf.matmul(input_tensor,avg_class.average(weights1))+avg_class.average(biases2))

#训练模型的过程
def train(mnist):
    x=tf.placeholder(tf.float32,[None,INPIT_NODE],name='x-input')
    y_ = tf.placeholder(tf.float32,[None,OUTPUT_NODE],name='y-input')

    #生成隐藏层的参数
    weights1=tf.Variable(tf.truncated_normal([INPUT_NODE,LAYER1_NODE],stddev=0.1))
    biases1=tf.Variable(tf.constant(0.1,shape=[LAYER1_NODE]))

    #生成输出层的参数
    weights2=tf.Variable(tf.truncated_normal([LAYER1_NODE.OUTPUT_NODE],stddev=0.1))
    biases2=tf.Variable(tf.constant(0.1,shape=[OUTPUT_NODE]))