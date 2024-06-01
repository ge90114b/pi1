import zmq
import json

# 创建一个ZeroMQ上下文
context = zmq.Context()

# 创建一个PULL套接字
receiver = context.socket(zmq.PULL)

# 连接到Sender的地址
receiver.connect("tcp://192.168.1.224:6666")

# 等待并接收消息
print("Waiting for message...")
message = receiver.recv_string()

# 解析接收到的JSON数据
received_data = json.loads(message)

# 打印接收到的数据
print(received_data)

# 关闭套接字
receiver.close()
context.term()