def tower(n,dau,giua,duoi):
    if n == 1:
        print("chuyen dia thu 1 tu cot", dau,"qua cot",duoi)
        return
    tower(n-1,dau,duoi,giua)
    print("chuyen dia ",n, " tu cot ",dau,"qua cot", duoi)
    tower(n-1,giua,dau,duoi)
tower(4,"A","B","C")