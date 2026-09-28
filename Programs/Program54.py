class Display:

    def Count_Numbers(iNo):

        i = 0
        iSum = 0

        for i in range(1,iNo):
            if i%2 == 0:
                iSum = iSum + i
        return iSum

def main():

    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display
    iRet = dobj.Count_Numbers(iValue1)

    print(f"Addition is : {iRet}")

    

if __name__ == "__main__":
    main()