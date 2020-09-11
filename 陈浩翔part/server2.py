from socket import *

HOST = ''
PORT = 8266     # 设置端口号
BUFSIZ = 1024
ADDRESS = (HOST, PORT)
demo = b"0"
# 创建监听socket
tcpServerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定IP地址和固定端口
tcpServerSocket.bind(ADDRESS)
print("服务器启动，监听端口{}...".format(ADDRESS[1]))

tcpServerSocket.listen(5)
print('服务器正在运行，等待客户端连接...')

try:
    while True:
        client_socket, client_address = tcpServerSocket.accept()

        try:
            while True:
                
                print("请输入指令")
                gauge = input()
                # 异常指令处理，若输入不合法则重新进入循环
                if(gauge != '0') :
                    print("您输入的指令有误，请重新尝试")
                    continue
                gauge = ord(gauge)  # 转ASCII
                if (gauge == 48) :
                    client_socket.send(demo)    # 发送请求，arduino端接收到后会发送温度json
                else :
                    continue
                dataTemp = client_socket.recv(2048)
                # 这里使用if判断，让dataTemp不为空时才执行后续内容，避免后面eval()出现EOF错误
                if dataTemp:
                    data = eval(dataTemp.decode('utf-8'))   # 解析收到json，通过decode和eval得到python字典格式，再处理数据
                    # print('接收到消息 {}({} bytes) 来自 {}'.format(data.decode('utf-8'), len(data), client_address))
                    objTemp = data["Temp1"]
                    ambTemp = data["Temp2"]
                    print(objTemp,ambTemp)
                else:
                   print('客户端 {} 已断开！'.format(client_address))
                   break
            
        finally:
            # 从else处break后跳出循环来到这里，关闭为这个客户端服务的socket
            client_socket.close()
finally:
    # 关闭监听socket，不再响应其它客户端连接
    tcpServerSocket.close()