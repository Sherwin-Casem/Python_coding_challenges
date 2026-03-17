if __name__ == '__main__':
    N = int(input())
    num_list = []
    
    for _ in range(N):
        command = input().split()
        
        match command[0]:
            case "insert":
                num_list.insert(int(command[1]), int(command[2]))
            case "print":
                print(num_list)
            case "remove":
                num_list.remove(int(command[1]))
            case "append":
                num_list.append(int(command[1]))
            case "sort":
                num_list.sort()
            case "pop":
                num_list.pop()
            case "reverse":
                num_list.reverse()
