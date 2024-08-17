def midwel(N):
    for i in range(1, N, 2):
        pattern = (".|."*i).center(M, "_")
        print(pattern)
    print("Welcome".center(M, "_"))
    for i in range(N-2, 0, -2):
        pattern = (".|."*i).center(M, "_")
        print(pattern)

L1 = list(map(int, input("Enter an odd number: ").strip().split()))
N = L1[0]
M = L1[1]
midwel(N)
