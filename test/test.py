import tensorflow as tf

def graph():
  # 创建一个常量运算操作,1*2矩阵
  matrix1 = tf.constant([[3., 3.]])
  # 创建另外一个常量运算操作，2*1矩阵
  matrix2 = tf.constant([[2.], [2.]])
  # 矩阵乘法
  product = tf.matmul(matrix1, matrix2)

  # 会话中运行
  with tf.Session() as sess:
    result = sess.run(product)
    print(result)

# 变量定义
def var_test():
  state = tf.Variable(0, name="counter")
  input1 = tf.constant(3.0)
  input1 = tf.placeholder(tf.float32)
  input2 = tf.placeholder(tf.float32)
  output = tf.matmul(input1, input2)
  with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1: [7.], input2: [2.]}))

# 激活函数
def jihuo():
  a = tf.constant([-1.0, 2.0])
  with tf.Session() as sess:
    print(sess.run(a))
    b = tf.nn.relu(a)
    print(sess.run(b))

if __name__ == '__main__':
    # graph()
  # var_test()
  jihuo()