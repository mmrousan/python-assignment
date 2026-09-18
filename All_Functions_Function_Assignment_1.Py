class AllFunctionsOfAssignment:
    
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        

    def OddEven():
        num=int(input("Enter a number: "))
        if((num%2)==1):
            print(num,"is odd number")
            output=f"{num} is odd number"
        else:
            print(num,"is Even number")
            output=f"{num} is Even number"
        
        return output
    
    
    def Elegible():
        
        gen=input("Enter Your Gender: ")
        age=int(input("Enter Your Age: "))
        
        if(gen=="Male" and age>=21):
            print("Eligible")
            result="Eligible"
            
        elif(gen=="Femala" and age>=18):
            print("Eligible")
            result="Eligible"
            
        else:
            print("Not Eligible")
            result="Not Eligible"
            
        return result


    def percentage():
    
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93
        
        subjects=[Subject1,Subject2,Subject3,Subject4,Subject5]
        total=sum(subjects)
        average=total/len(subjects)
        
        print(f"""
        Subject1= {Subject1}
        Subject2= {Subject2}
        Subject3= {Subject3}
        Subject4= {Subject4}
        Subject5= {Subject5}
        """)
        print("Total: ",total)
        print("Percentage: "f"{average:.10f}")
        
        return total, average

    
    def triangle():
        height=float(input("Enter the Height: "))
        breadth=float(input("Enter the Breadth: "))
        height1=float(input("Enter the Height1: "))
        height2=float(input("Enter the Height2: "))
        
        area=(height*breadth)/2
        perimeter=height1+height2+breadth
        
        print("Area of the Triangle: ",area)
        print("Perimeter of the Triangle: " ,perimeter)
        
        return area,perimeter

 
      