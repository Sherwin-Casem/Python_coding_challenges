import string
def print_rangoli(size):
       alpha = string.ascii_lowercase
    
       width = 4 * size - 3
    
    # Top half
       for i in range(size-1, 0, -1):
            s = "-".join(alpha[i:size])
            line = (s[::-1] + s[1:]).center(width, "-")
            print(line)
        
        # Bottom half
       for i in range(size):
            s = "-".join(alpha[i:size])
            line = (s[::-1] + s[1:]).center(width, "-")
            print(line)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)