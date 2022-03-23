# userRequest.py 
##Imports hostQueue and is the main driver that references begin connection in another class
from hostQueue import hostQueue


BEGIN_HOST = hostQueue();

def main():
    BEGIN_HOST.beginConnection();
    return

if __name__ == "__main__":
    main()