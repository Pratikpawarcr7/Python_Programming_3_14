class Array:
    def __init__(self,B):

        self.iSize = B
        self.Arr = [0] * self.iSize

    def Accept(self):

        print("Enter the Elemnets : ")

        for iCnt in range(0,self.iSize):
            self.Arr[iCnt] = int(input())

    def Display_Count_Odd(self):

         iSum = 0
         for iCnt in range(0,self.iSize):
            if ((self.Arr[iCnt]%2) != 0):
                iSum = iSum + 1

         return iSum

         

def main():

    print("How Many Elemnets You Want : ")
    iValue1 = int(input())

    aobj = Array(iValue1)

    aobj.Accept()
    iRet = aobj.Display_Count_Odd()

    print(f"Total Number of Odd Elements is : {iRet}")

if __name__ == "__main__":
    main()