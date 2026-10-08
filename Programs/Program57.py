
class Array:
    def __init__(self,B):

        self.iSize = B
        self.Arr = [0] * self.iSize

    def Accept(self):

        print("Enter the Elemnets : ")

        for iCnt in range(0,self.iSize):
            self.Arr[iCnt] = int(input())

    def Display_Addition(self):
         iSum = 0
        
         for iCnt in range(0,self.iSize):
            iSum = iSum + self.Arr[iCnt]

         return iSum

def main():

    print("How Many Elemnets You Want : ")
    iValue1 = int(input())

    aobj = Array(iValue1)

    aobj.Accept()
    iRet = aobj.Display_Addition()

    print(f"Addition is : {iRet}")

if __name__ == "__main__":
    main()