from datetime import date


def main():
    length = convert(input('Date of Birth: '))
    print(sing(length))
    
    
def convert(birth):
    return (date.now() - date.fromisoformat(birth))
    
    
def sing(length):
    return length
    
    
if __name__ == "__main__":
    main()