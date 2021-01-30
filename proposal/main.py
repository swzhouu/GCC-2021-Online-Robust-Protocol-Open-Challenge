import sys
import utils
from myscu import NewSCU

# Taro's IP
# DEST_IP = "169.254.155.219"

# Hanako IP
DEST_IP = "169.254.229.153"

def main():
    if sys.argv[1] == "sender":
        myscu = NewSCU(mtu=1500)
        myscu.bind_as_sender(receiver_address=(DEST_IP, 8888))
        # myscu.bind_as_sender(receiver_address=("127.0.0.1", 50001))
        try:
            for id in range(0, 1000):
                myscu.send(f"./proposal/data/data{id}", id)
                print(f"file sent: {id}", end="\r")
        except Exception as e:
            print(e)
            myscu.drop() # just in case

    elif sys.argv[1] == "receiver":
        myscu = NewSCU(mtu = 1500)
        myscu.bind_as_receiver(receiver_address = (DEST_IP, 8888))       
        # myscu.bind_as_receiver(receiver_address = ("127.0.0.1", 50001))
        for i in range(0, 1000):
            filedata = myscu.recv()
            utils.write_file(f"./proposal/hanakoData/data{i}", filedata)
            del(myscu.received_files_data[i])
            print(f"file received: {i}")

if __name__ == '__main__':
    main()