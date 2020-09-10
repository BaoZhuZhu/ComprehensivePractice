from socket import *

HOST = ''
PORT = 8266
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
        # print('客户端{}已连接！'.format(client_address))

        try:
            while True:
                
                print("请输入指令")
                gauge = input()
                gauge = ord(gauge)
                if (gauge == 48) :
                    client_socket.send(demo)
                else :
                    continue
                dataTemp = client_socket.recv(2048)
                #print(dataTemp)
                # 这里使用if判断，让dataTemp不为空时才执行后续内容，避免后面eval()出现EOF错误
                if dataTemp:
                    data = eval(dataTemp.decode('utf-8'))
                    # print('接收到消息 {}({} bytes) 来自 {}'.format(data.decode('utf-8'), len(data), client_address))
                    # print(data["Temp1"],data["Temp2"])
                    objTemp = data["Temp1"]
                    ambTemp = data["Temp2"]
                    print(objTemp,ambTemp)
                    # print(type(data))

                    # client_socket.send(data)
                    # print('发送消息 {} 至 {}'.format(data.decode('utf-8'), client_address))
                
                else:
                   print('客户端 {} 已断开！'.format(client_address))
                   break
                
        finally:
            # 关闭为这个客户端服务的socket
            # print('客户端 {} 已断开！'.format(client_address))
            client_socket.close()
finally:
    # 关闭监听socket，不再响应其它客户端连接
    tcpServerSocket.close()