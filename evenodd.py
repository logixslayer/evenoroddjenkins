import sys 
def evenorodd(num):
    if num % 2 == 0:
        print("the given number is even")
        return 0
    else:
        print("the given number is odd")
        return 1
    
if __name__ == "__main__": 
    num = int(sys.argv[1])
    print(evenorodd(num))