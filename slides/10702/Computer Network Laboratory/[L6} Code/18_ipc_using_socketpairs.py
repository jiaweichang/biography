import socket
import os

BUFSIZE = 1024

def test_socketpair():
    """ Test Unix socketpair"""
    parent, child = socket.socketpair()
    
    pid = os.fork()
    try:
        if pid:
            print ("@Parent, sending message...")
            child.close()

            parent.sendall(bytes("Hello from parent!"))
            # Comment out the above line and uncomment the below line for Python 2.7.
            # parent.sendall("Hello from parent!")

            response = parent.recv(BUFSIZE)
            print ("Response from child:", response)
            parent.close()
        
        else:
            print ("@Child, waiting for message from parent")
            parent.close()
            message = child.recv(BUFSIZE)
            print ("Message from parent:", message)

            child.sendall(bytes("Hello from child!!"))
            # Comment out the above line and uncomment the below line for Python 2.7.
            # child.sendall("Hello from child!!")

            child.close()
    except Exception as err:
        print ("Error: %s" %err)


if __name__ == '__main__':
    test_socketpair()
