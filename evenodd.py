def evenorodd(num):
    if num % 2 == 0:
        print("the given number is even")
        return "even"
    else:
        print("the given number is odd")
        return "odd"
    
if __name__ == "__main__": 
    print(evenorodd(5))