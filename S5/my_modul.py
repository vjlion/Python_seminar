def rect(n,m):
    s= n*m
    return s

def tri(h,m):
    s = 0.5*h*m
    return s

def circ(r):
    return 3.14*r**2

def main():
    print(rect(2,3))
    print(tri(2,3))
    print(circ(2))

if __name__ == "__main__":
    main()