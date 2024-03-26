from os import system 
while True:
    
    
    a = input("""\033[1;36m1.Normal
2.Full
: """)
    if a == "1":
        print()
    
        import time 
        import socket 
        import sys
        import time
        from os import system 
        

        for number in range(8):
            print(f"\033[1;3{number}m PORT SCANNER",end="\r")
            time.sleep(0.1)
        print()    
        print("\033[1;31mScanning")    
        print("\033[1;32m___________________________________________")    
        a1 =  input("Enter the target: ")
        a2 = int(input("Enter the first port: "))
        a3 = int(input("Enter the second port: "))
        args =sys.argv
        
        for num in range(8):
         
            print(f"\033[1;3{num}m PORT SCANNER",end="\r")
            time.sleep(0.2)
        print()    
        print()
        print(f"\033[1;31mScanning \033[0;32m{a1}")
        print("\033[1;32m___________________________________________")

        if a1 == "--help":
            print("\033[1;31mpython3 PortScanner14.py [target] [port1] [port2]")
        for port in range(a2, a3):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((a1, port))
                print(f"\033[1;32m{port} [OPEN] {socket.getservbyport(port)}")
            except:
                pass
    elif a == "2":
        print()
        import time 
        import socket 
        import sys
        import time
        from os import system 
        

        for number in range(8):
            print(f"\033[1;3{number}m PORT SCANNER",end="\r")
            time.sleep(0.1)
        print()    
        print("\033[1;31mScanning")    
        print("\033[1;32m___________________________________________")    
        a1 =  input("Enter the target: ")
        a2 = int(input("Enter the first port: "))
        a3 = int(input("Enter the second port: "))
        args =sys.argv
        
        for num in range(8):
         
            print(f"\033[1;3{num}m PORT SCANNER",end="\r")
            time.sleep(0.2)
        print()    
        print()
        print(f"\033[1;31mScanning \033[0;32m{a1}")
        print("\033[1;32m___________________________________________")

        if a1 == "--help":
            print("\033[1;31mpython3 PortScanner14.py [target] [port1] [port2]")
        open_ports = []   
        for port in range(a2, a3):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((a1, port))
                open_ports.append(port)
                print(f"\033[1;32m{port} \033[1;32m[OPEN] {socket.getservbyport(port)}")
            except:
                print(f"\033[1;31m{port} \033[1;31m[CLOSE]") 
        print("\033[0;37m-------------------------------------------")     
        for open_port in open_ports:
            print(f"\033[1;31m{open_port}\033[1;32m [OPEN]")  
        print("\033[1;37m-------------------------------------------")                    