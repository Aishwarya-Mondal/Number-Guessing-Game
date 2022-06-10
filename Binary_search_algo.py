import random
num_list = []
for i in range(1,11):
    num_list.append(random.randint(1,20))
num_list.sort()
print(num_list)


def binary_search(num):
    global num_list
    lower = 0
    upper = len(num_list)-1
    flag = 0
    while lower < upper:
        mid = int((lower+upper)/2)
        if num_list[mid] == num:
            print("Your number is found in the list!")
            flag += 1
            break
        elif num_list[mid] > num:
            upper = mid-1
        elif num_list[mid] < num:
            lower = mid+1
    if flag == 0:
        print("Sorry number not found!")

def start_searching():
    global num_list
    try:
        num = int(input("Enter a number to be searched in range 1-20:"))

        if num<1 or num>20:
            raise ValueError

        binary_search(num)
    except ValueError as ve:
        print("Please enter a number in 1-20 range!")
if __name__=='__main__':
    start_searching()