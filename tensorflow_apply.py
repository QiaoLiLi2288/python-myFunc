import tensorflow as tf
tf.cast(x, dtype) #转换张量数据类型
tf.argmax(x, 0) #axis=0下返回最大值的坐标
tf.equal(x,y) #比较张量x,y的是否相等 -- bool
tf.reduce_mean(), tf.square() #求均值、求平方
# 初始化变量
sess = tf.Session()
sess.run(tf.global_variables_initializer())
tf.matmul() # 矩阵乘积
tf.nn.relu() #relu
tf.nn.softmax_cross_entropy_with_logits(labels=, logits=) # 交叉熵
opt = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(loss) #SGD
# 定义权重和偏置
W_conv = tf.Variable(tf.truncated_normal([5,5,1,32], stddev=0.1)) # 5*5表示卷积核的大小，1表示图像的通道数，32表示卷积的个数
B_conv = tf.Variable(tf.constant(0.1, shape = [32])) 
# 定义卷积层和2*2池化层
def conv2d(x, W):
    return tf.nn.conv2d(input=x, filter=W, strides=[1,1,1,1], padding="SAME")
def max_pool_2X2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")
