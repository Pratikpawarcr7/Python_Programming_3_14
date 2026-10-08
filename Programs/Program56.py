
class Array:
    def __init__(self,B):

        self.iSize = B
        self.Arr = [0] * self.iSize

    def Accept(self):

        print("Enter the Elemnets : ")

        for iCnt in range(0,self.iSize):
            self.Arr[iCnt] = int(input())

    def Display_Numbrs(self):

         print("Elemens Are : ")
        
         for iCnt in range(0,self.iSize):
            print(self.Arr[iCnt])


def main():

    print("How Many Elemnets You Want : ")
    iValue1 = int(input())

    aobj = Array(iValue1)

    aobj.Accept()
    aobj.Display_Numbrs()


if __name__ == "__main__":
    main()