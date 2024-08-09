import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # รับข้อมูลจาก client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # ออกจากลูปถ้าข้อมูลที่รับมาว่าง
                break
            print(f"Received from client: {message}")

            # ส่งข้อความตอบกลับ
            response = "Message received"
            client_socket.send(response.encode('utf-8'))
        except ConnectionResetError:
            # จัดการกับกรณีที่ client เชื่อมต่อหลุด
            break

    # ปิดการเชื่อมต่อเมื่อเสร็จสิ้น
    client_socket.close()

# สร้าง socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# กำหนด host และ port
host = '0.0.0.0'  # ฟังที่ทุก IP บนเครื่อง
port = 12345

# ผูก socket กับ address และ port
server_socket.bind((host, port))

# เริ่มรอรับการเชื่อมต่อ
server_socket.listen(5)  # รองรับการเชื่อมต่อได้สูงสุด 5 รายการ
print(f"Server listening on {host}:{port}")

while True:
    # รับการเชื่อมต่อจาก client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # เริ่ม thread ใหม่เพื่อจัดการกับ client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
