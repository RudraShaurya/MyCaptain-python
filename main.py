r= float(input("enter the float radius of the circle"))
A = 3.141592653589793238*(r**2)
print("area of the circle of radius", r, "is=", A)

f=str(input("Input the Filename"))
Newf=f.split(".")
if Newf[-1 =="py"]:
    print("The extension of the file is:'python'")
else:
    print("The extension of the file is:", Newf[-1])