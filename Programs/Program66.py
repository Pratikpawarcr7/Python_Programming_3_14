class Array:
    def __init__(self,B):

        self.iSize = B
        self.Arr = [0] * self.iSize

    def Accept(self):

        print("Enter the Elemnets : ")

        for iCnt in range(0,self.iSize):
            self.Arr[iCnt] = int(input())

    def Display_Maximum(self):

         iMax = 0
         iMax = self.Arr[0]
         for iCnt in range(0,self.iSize):
            if ((self.Arr[iCnt]) > iMax):
                iMax = self.Arr[iCnt]

         return iMax

         

def main():

    print("How Many Elemnets You Want : ")
    iValue1 = int(input())

    aobj = Array(iValue1)

    aobj.Accept()
    iRet = aobj.Display_Maximum()

    print(f"Maximum Elements is : {iRet}")

if __name__ == "__main__":
    main()