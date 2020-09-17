from socket import *
import logging

HOST = ''
PORT = 8266  # 设置端口号
BUFSIZ = 1024
ADDRESS = (HOST, PORT)
demo = b"0"



class A:
    def __init__(self, address):
        # 创建监听socket
        self.tcpServerSocket = socket(AF_INET, SOCK_STREAM)

        # 绑定IP地址和固定端口
        self.tcpServerSocket.bind(address)
        print("服务器启动，监听端口{}...".format(address[1]))

        self.tcpServerSocket.listen(5)
        print('服务器正在运行，等待客户端连接...')

        self.client_socket, self.client_address = self.tcpServerSocket.accept()

    def run(self, gauge):

        #while True:
        print("请输入指令")
        #gauge = input()

        # 异常指令处理，若输入不合法则重新进入循环
        if (gauge != '0'):
            print("您输入的指令有误，请重新尝试")
            #break;
            return
        gauge = ord(gauge)  # 转ASCII
        if (gauge == 48):
            self.client_socket.send(demo)  # 发送请求，arduino端接收到后会发送温度json
        else:
            #continue
            return
        #logging.warning("abcde")
        dataTemp = self.client_socket.recv(2048)
        #logging.warning("abcde")
        # 这里使用if判断，让dataTemp不为空时才执行后续内容，避免后面eval()出现EOF错误
        if dataTemp:
            data = eval(dataTemp.decode('utf-8'))  # 解析收到json，通过decode和eval得到python字典格式，再处理数据
            # print('接收到消息 {}({} bytes) 来自 {}'.format(data.decode('utf-8'), len(data), client_address))
            objTemp = data["Temp1"]
            ambTemp = data["Temp2"]
            #print(objTemp, ambTemp)
            return objTemp
        else:
            print('客户端 {} 已断开！'.format(self.client_address))
            #break
            #self.client_socket.close()
            return

    def close(self):
        self.client_socket.close()
        self.tcpServerSocket.close()




