class Display:

    def Count_Numbers(iNo):

        iCnt = 0

        print("Evan Numbers Are : ")
        for i in range(1,iNo):
            if i%2 == 0:
                print(i)

def main():

    print("Enter the Number : ")
    iValue1 = int(input())

    dobj = Display
    dobj.Count_Numbers(iValue1)

    

if __name__ == "__main__":
    main()