def square(squ):
     a=squ
     for i in range(a):
	     print("*" * a)

def diamond(dia):
     a=dia
     for i in range(a):
        if i <= 5:
            for j in range(5-i):
                print(" ",end="")
            for j in range(2*i-1):
                print("*",end="")
            print()
        else:
            for j in range(i-5):
                print(" ",end="")
            for j in range((10-i)*2-1):
                print("*",end="")
            print()

while(True):
    shape = str(input("도형선택:"))
    if shape == "정사각형":
        squ=int(input("square:"))
        square(squ)
    elif shape == "마름모":
        dia=int(input("diamond:"))
        diamond(dia)
    else:
        shape = str(input("도형선택:"))