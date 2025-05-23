if __name__ == '__main__':
    n = int(input())
    
    ls = map(int, input().split())
    arr=list(ls)
    new_list=sorted(arr,reverse=True)
    for x in range(len(new_list)):
        if new_list[x]<new_list[0]:
            print(new_list[x])
            break
