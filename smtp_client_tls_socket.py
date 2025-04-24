import socket
import ssl
import base64

# SMTP2GO server and port (587 supports STARTTLS)
mailserver = "mail.smtp2go.com"
port = 587

# Credentials
username = "EsmeW"
password = "Xx123456"
sender_email = "oogwayrosiejade@hotmail.com"
receiver_email = "wangxueqi08@gmail.com"

# Message
msg = "Subject: SMTP Lab Test\r\n\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Connect socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, port))

# Server response (220)
recv = clientSocket.recv(1024).decode()
print(recv)

# Send EHLO
clientSocket.send(b"EHLO Alice\r\n")
recv = clientSocket.recv(1024).decode()
print(recv)

# Send STARTTLS
clientSocket.send(b"STARTTLS\r\n")
recv = clientSocket.recv(1024).decode()
print(recv)

# Wrap in SSL
context = ssl.create_default_context()
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
secureSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

# Send EHLO again after TLS
secureSocket.send(b"EHLO Alice\r\n")
recv = secureSocket.recv(1024).decode()
print(recv)

# AUTH LOGIN
secureSocket.send(b"AUTH LOGIN\r\n")
recv = secureSocket.recv(1024).decode()
print(recv)

# Send base64 encoded username
secureSocket.send(base64.b64encode(username.encode()) + b"\r\n")
recv = secureSocket.recv(1024).decode()
print(recv)

# Send base64 encoded password
secureSocket.send(base64.b64encode(password.encode()) + b"\r\n")
recv = secureSocket.recv(1024).decode()
print(recv)

# MAIL FROM
mail_from = f"MAIL FROM:<{sender_email}>\r\n"
secureSocket.send(mail_from.encode())
recv = secureSocket.recv(1024).decode()
print(recv)

# RCPT TO
rcpt_to = f"RCPT TO:<{receiver_email}>\r\n"
secureSocket.send(rcpt_to.encode())
recv = secureSocket.recv(1024).decode()
print(recv)

# DATA
secureSocket.send(b"DATA\r\n")
recv = secureSocket.recv(1024).decode()
print(recv)

# Send message content
secureSocket.send(msg.encode())
secureSocket.send(endmsg.encode())
recv = secureSocket.recv(1024).decode()
print(recv)

# QUIT
secureSocket.send(b"QUIT\r\n")
recv = secureSocket.recv(1024).decode()
print(recv)

# Close socket
secureSocket.close()