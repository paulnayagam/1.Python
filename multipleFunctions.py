class multipleFunctions():
    
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is even number")
            mes=num,"is even number"
        else:
            print(num,"is odd number")
            mes=num,"is odd number"
        return mes
    
    def Subfields():
        list = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for val in list:
            print(val)

    def eligiblity():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if((gender == "male") & (age>=21)):
            print("Eligible")
        elif((gender == "female") & (age>=18)):
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        sub1=int(input("Subject1 ="))
        sub2=int(input("Subject2 ="))
        sub3=int(input("Subject3 ="))
        sub4=int(input("Subject4 ="))
        sub5=int(input("Subject5 ="))
        total=sub1+sub2+sub3+sub4+sub5
        print("total= ",total)
        print("percentage= ",total/5)

    def triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(height*breadth)/2)
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        breadth=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",height1+height2+breadth)


