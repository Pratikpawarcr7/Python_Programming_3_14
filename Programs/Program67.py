class Array:
    def __init__(self,B):

        self.iSize = B
        self.Arr = [0] * self.iSize

    def Accept(self):

        print("Enter the Elemnets : ")

        for iCnt in range(0,self.iSize):
            self.Arr[iCnt] = int(input())

    def Display_Minimum(self):

         iMin = 0
         iMin = self.Arr[0]
         for iCnt in range(0,self.iSize):
            if ((self.Arr[iCnt]) < iMin):
                iMin = self.Arr[iCnt]

         return iMin

def main():

    print("How Many Elemnets You Want : ")
    iValue1 = int(input())

    aobj = Array(iValue1)

    aobj.Accept()
    iRet = aobj.Display_Minimum()

    print(f"Smallest Elements is : {iRet}")

if __name__ == "__main__":
    main()