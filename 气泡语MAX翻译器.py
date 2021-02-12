
from os import system
from typing import Text


def init() -> None:

    global choose
    global history

    choose = ""
    history = []


def welcome() -> None:

    print("\n-----欢迎使用气泡语MAX翻译器-----")
    print("版本：v1.0_py")
    print("语言：Python")
    print("Kitten4.0版链接：https://shequ.codemao.cn/work/74451508")


def chooseer() -> str:

    print("\n---选择功能---")
    print("0.清屏")
    print("1.人语->气泡语MAX")
    print("2.气泡语MAX->人语")
    print("3.查看翻译历史")
    print("4.清空翻译历史")
    print("输入序号以选择功能：", end="")

    return input()


def baseConversion(mode: bool, num: str) -> str:
    """
    True:十进制转四进制\n
    False:四进制转十进制\n
    这里用了一些投机取巧的方式，主要是懒得思考\n
    """

    newNum = ""
    if (mode):
        num = str(bin(int(num)))[2:]
        if (len(num) % 2 == 1):
            num = "0" + num
        i = 0
        while (i < len(num)):
            if (num[i:i + 2] == "00"):
                newNum += "0"
            elif (num[i:i + 2] == "01"):
                newNum += "1"
            elif (num[i:i + 2] == "10"):
                newNum += "2"
            elif (num[i:i + 2] == "11"):
                newNum += "3"
            i += 2
    else:
        newNum = str(int(num, 4))

    return newNum


def toQPYMAX(inputText: str) -> str:

    global history

    print("\n-输出-")
    temp = ""
    for text in inputText:
        temp += baseConversion(True, str(ord(text))).rjust(8, "0").replace(
            "0", ".").replace("1", "o").replace("2", "0").replace("3", "O")
    print(temp)
    history.append((inputText, temp, True))


def toRY(inputText: str) -> str:

    global history

    print("\n-输出-")
    temp = ""
    for i in range(len(inputText)//8):
        text = inputText[i * 8:i * 8 + 8]
        temp += chr(int(baseConversion(False, text.replace("O", "3").replace(
            "0", "2").replace("o", "1").replace(".", "0"))))
    print(temp)
    history.append((inputText, temp, False))


init()
welcome()

while True:

    choose = chooseer()
    if (choose == "0"):
        system("cls")
    elif (choose == "1"):
        print("\n-输入-")
        toQPYMAX(input("输入人语："))
    elif (choose == "2"):
        print("\n-输入-")
        toRY(input("输入气泡语MAX："))
    elif (choose == "3"):
        for i, history_ in enumerate(history):
            from_ = history_[0]
            to = history_[1]
            mode = history_[2]
            print(f"{i}.\t{from_}\tto{'气泡语MAX' if mode else '人语'}\t{to}")
    elif (choose == "4"):
        history = []
    else:
        print("\n-输出-")
        print("此功能不存在")
