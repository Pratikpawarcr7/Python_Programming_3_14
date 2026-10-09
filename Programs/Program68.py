
class Array:
    def __init__(self,B):

        self.iSize = B
        self.Arr = [0] * self.iSize

    def Accept(self):

        print("Enter the Elemnets : ")

        for iCnt in range(0,self.iSize):
            self.Arr[iCnt] = int(input())

    def Display_Reverse_Number(self):
         
         print("Reverse Number Are : ")
         for iCnt in range(self.iSize-1,-1,-1):
            print(self.Arr[iCnt])

         

def main():

    print("How Many Elemnets You Want : ")
    iValue1 = int(input())

    aobj = Array(iValue1)

    aobj.Accept()
    aobj.Display_Reverse_Number()

    

if __name__ == "__main__":
    main()