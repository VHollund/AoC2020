# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def day_1_1():
    with open("Day1\input.txt", 'r') as file:
        list=file.readlines()
        for x in list:
            for z in list:
                if int(x)+int(z)==2020:
                    print(f"x: {int(x)}, z:{int(z)}, product:{int(x)*int(z)}")


def day_1_2():
    with open("Day1\input.txt", 'r') as file:
        list=file.readlines()
        for x in list:
            for z in list:
                for y in list:
                    if int(x)+int(z)+int(y)==2020:
                        print(f"x: {int(x)}, z:{int(z)}, y:{int(y)}, product:{int(x)*int(z)*int(y)}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day_1_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
