def NOT():
    a = int(input("请输入NOT门的一位输入:"))
    if (a == 1):
        a = 0
    elif (a == 0):
        a = 1
    print("经过NOT门的转换，输出为：" + str(a))
    choose()

def CNOT():
    control = int(input("请输入CNOT门的控制位:"))
    target = int(input("请输入CNOT门的目标位:"))
    if (control == 0):
        target = target
    elif (control == 1):
        if (target == 1):
            target = 0
        elif (target == 0):
            target = 1
    print("经过CNOT门的转换,控制位：" + str(control))
    print("经过CNOT门的转换,目标位：" + str(target))
    choose()

def Toffoli():
    control_1 = int(input("请输入Toffoli门的第一位控制位:"))
    control_2 = int(input("请输入Toffoli门的第二位控制位:"))
    target = int(input("请输入Toffoli门的目标位:"))
    if (control_1 == 1 and control_2 == 1):
        if (target == 1):
            target = 0
        elif (target == 0):
            target = 1
    print("经过Toffoli门的转换，第一位控制位：" + str(control_1))
    print("经过Toffoli门的转换，第二位控制位：" + str(control_2))
    print("经过Toffoli门的转换，目标位：" + str(target))
    choose()

def Swap():
    control = int(input("请输入Swap门的控制位:"))
    target_1 = int(input("请输入Swap门的第一目标位:"))
    target_2 = int(input("请输入Swap门的第二目标位:"))
    if (control == 1):
        temp = target_1
        target_1 = target_2
        target_2 = temp
    print("经过Swap门的转换,控制位:" + str(control))
    print("经过Swap门的转换,第一目标位:" + str(target_1))
    print("经过Swap门的转换,第二目标位:" + str(target_2))

def choose():
    print("1---NOT门\n" +
          "2---CNOT门\n" +
          "3---Toffoli门\n"
          "4---Swap门\n"
          "-1--退出")
    _NO = int(input("请输入你要选择的量子逻辑门："))
    if (_NO == 1):
        NOT()
    elif (_NO == 2):
        CNOT()
    elif (_NO == 3):
        Toffoli()
    elif (_NO==4):
        Swap()
    elif (_NO == -1):
        return 0


if __name__ == '__main__':
    choose()
