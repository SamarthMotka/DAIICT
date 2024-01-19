
def printPascal(n): 
    pass
    for line in range(1, n + 1):
        C=1 
        print(" "*(n-line),end=" ")
        for i in range(1, line + 1): 
            
            print(C, end = " "); 
            C = int(C * (line - i) / i); 
        print(""); 

if __name__ == "__main__":
    rows = 5
    printPascal(rows)

   