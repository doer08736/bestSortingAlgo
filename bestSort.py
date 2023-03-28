from random import shuffle


def bestSort():
    print("\nSorting: ")
    while(list!=_list):
        print(list)
        shuffle(list)
    print("\nYour sorted list is: ", list)


n = int(input("enter no. of elements: "))
list = list(map(int, input().strip().split()))[:n]
_list = list.copy()
_list.sort()


if __name__ == "__main__":
    bestSort()