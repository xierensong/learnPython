from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)  # 获取数据集

print(mnist.train.images.shape, mnist.train.labels.shape)   # 训练集大小 训练模型
print(mnist.test.images.shape, mnist.test.labels.shape)    # 测试集大小 评测模型的效果
print(mnist.validation.images.shape, mnist.validation.labels.shape) # 验证集大小 没用到

import tensorflow as tf

sess = tf.InteractiveSession()  # 当前session注册为默认session，运算默认跑在这个session中，不同session的数据和运算是独立的

x = tf.placeholder(tf.float32, [None, 784]) # 输入数据，32位浮点数，n*784,n表示无限制
W = tf.Variable(tf.zeros([784, 10]))    # 存储模型参数，784×10，长期存在并在每轮迭代中被更新，初始化为0
b = tf.Variable(tf.zeros([10])) # 存储模型参数，1×10，初始化为0

# 定义算法公式，神经网路forward时的计算
# y = tf.nn.softmax(tf.matmul(x, W) + b)
y = tf.matmul(x, W) + b  # matmul表示矩阵乘法

y_ = tf.placeholder(tf.float32, [None, 10]) # 输入真实的label

# 第二步 定义loss， 选定优化器，并指定优化器优化loss
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y),reduction_indices[1])) # unstable
cross_entropy = tf.reduce_mean( # 计算交叉熵，先计算softmax，再用交叉熵公式y_ * log(y) 求和，取平均
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy) # 定义优化函数（随机梯度下降SGD），设置学习速率0.5，优化目标设置为cross-entropy,这一步骤就是训练，（计算图）

# 第三步，迭代地对数据进行训练
tf.global_variables_initializer().run()  # 全局参数初始化器，执行run方法

for _ in range(1000):   # 迭代执行训练操作train_step  使用一小部分样本进行训练称为随机梯度下降，比全样本训练的收敛速度快很多。不用的数字可以用_处理
    batch_xs, batch_ys = mnist.train.next_batch(100)    # 随机从训练集中抽取100条样本
    train_step.run({x: batch_xs, y_: batch_ys}) # feed给placeholder x, y_，进行训练

# 第四步 在测试集或验证集上对准确率进行评测
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))    # 从一个tensor中寻找最大值的序号，判断预测的数字类别是否就是正确的类别
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))  # cast bool类型转化为float32，再求平均

print(accuracy.eval({x:mnist.test.images, y_:mnist.test.labels})) # 评测流程 将测试数据的特征和label feed评测流程