if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lg_list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                t = (i,j,k)
                if i+j+k != n:
                    sm_list = list(t)
                    lg_list.append(sm_list)
    print(lg_list)
