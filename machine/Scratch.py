import socket
import sys
class Scratch:
    # 设置服务器 IP 和端口
    server_ip = "10.42.0.1"
    server_port = 8080

    # 打開文件以追加模式寫入，如果文件不存在則創建
    with open('received_messages.txt', 'a') as file:
        file.write("------------------New---------------------\n")

    # 建立套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定 IP 和端口
    server_socket.bind((server_ip, server_port))

    # 開始監聽
    server_socket.listen(1)
    print(f"等待連接在 {server_ip}:{server_port} 上的消息...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"已連接到 {client_address}")

            # 创建一个无限循环，等待指令
            while True:
                data = client_socket.recv(1024)  # 接收数据
                if not data:
                    break

                received_data = data.decode('utf-8').strip()  # 去除空白字符


                if received_data:
                    print( received_data)

                    # 将接收到的消息写入文本文件
                    with open('received_messages.txt', 'a') as file:
                        file.write(received_data + '\n')

            # 关闭客户端套接字
            client_socket.close()
            print("Connection closed")

    except KeyboardInterrupt:
        print("接收到 Ctrl + C，停止運行")

    finally:
        # 关闭服务器套接字
        server_socket.close()
        sys.exit(0)

    start_time = time.time()

    # data = client_socket.recv(4096)  # 接收数据
    # if not data:
    #     continue
    #
    # received_data = data.decode('utf-8').strip()  # 去除空白字符
    #
    # numbers = re.findall(r'\d+\.*\d*', received_data)
    #
    # # 將提取的數字轉換為浮點數，這里假設使用浮點數進行操作
    # numbers = [float(num) for num in numbers]
    #
    # # 假設進行除以 10 和減去 11.8 的操作
    # result = [(num / 10) - 11.8 for num in numbers]
    #
    # # 將結果轉換為絕對值
    # abs_result = [abs(num) for num in result]
    #
    # # 將結果四捨五入到小數點後第二位
    # rounded_result = [round(num, 2) for num in abs_result]
    #
    # # 將結果轉換為純數字字符串，小數點後只保留一位
    # result_str = ''.join(map(lambda x: f"{x:.1f}", rounded_result))
    # print(result_str)

    # if (3.5 <= result_str <= 4):
    #     end_time = time.time()
    #     current_time = end_time - start_time
    #     print(current_time)
    #     self.frequency_label.update_label.emit(str(current_time))

