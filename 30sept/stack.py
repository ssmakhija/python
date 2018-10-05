def push(l, data):
    l.append(data)

def pop(l):
    return l.pop()

def peep(l):
    return l[-1]

def is_empty(l):
    return l == []

def is_full(l):
    return len(l) == 10

def menu():
    ch = -1
    while ch < 1 or ch > 5:
        print("Welcome To Stack Menu !!!")
        print("1.push\n2.pop\n3.peep\n4.show\n5.exit")
        ch = eval(input("Enter Choice"))
    return ch
def stack_operations():
    l = []
    ch = menu()
    while(ch != 5):
        if ch == 1:
            if not is_full(l):
                push(l, eval(input("Enter data to push:")))
            else:
                print("Please pop something first, stack is full.")
        elif ch == 2:
            if not is_empty(l):
                print(pop(l))
            else:
                print("Stack is empty.")
        elif ch == 3:
            if not is_empty(l):
                print(peep(l))
            else:
                print("Stack is empty.")
        elif ch==4:
            if not is_empty(l):
                print(*l, sep=', ')
        else:
            break
        ch = menu()

def main():
    stack_operations()

if __name__ == "__main__":
    main()