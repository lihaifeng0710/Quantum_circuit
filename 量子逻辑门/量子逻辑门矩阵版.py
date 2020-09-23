import numpy as np


def NOT():
    print("用矩阵表示0和1两个状态位")
    print("1---[[0],\n\t[1]]")
    print("0---[[1],\n\t[0]]")
    a = int(input("请输入NOT门的一位输入:"))
    _not = np.array([[0, 1],
                     [1, 0]])
    if a == 1:
        begin = np.array([[0], [1]])
        print("您的输入是：")
        print("[[0],\n[1]]")
        result = np.dot(_not, begin)
    elif a == 0:
        begin = np.array([[1], [0]])
        print("您的输入是：")
        print("[[1],\n[0]]")
        result = np.dot(_not, begin)
    if ((result == [[1], [0]]).all()):
        begin = 0
    elif ((result == [[0], [1]]).all()):
        begin = 1
    print("经过NOT门的转换，输出为：" + str(begin))
    choose()


def CNOT():
    print("用矩阵表示0和1两个状态位")
    print("1---[[0],\n\t[1]]")
    print("0---[[1],\n\t[0]]")
    print("因为CONT门有两位，一个控制位，一个目标位，所以需要进行张量积运算")
    control = int(input("请输入CNOT门的控制位:"))
    target = int(input("请输入CNOT门的目标位:"))
    if control == 0:
        control = np.array([[1], [0]])
    elif control == 1:
        control = np.array([[0], [1]])
    if target == 0:
        target = np.array([[1], [0]])
    elif target == 1:
        target = np.array([[0], [1]])
    cnot = np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]])
    product = np.kron(control, target)
    result = np.dot(cnot, product)
    if ((result == [[1], [0], [0], [0]]).all()):
        control = 0
        target = 0
    elif ((result == [[0], [1], [0], [0]]).all()):
        control = 0
        target = 1
    elif ((result == [[0], [0], [0], [1]]).all()):
        control = 1
        target = 1
    elif ((result == [[0], [0], [1], [0]]).all()):
        control = 1
        target = 0
    # print(result)
    print("经过CNOT门的转换,控制位：" + str(control))
    print("经过CNOT门的转换,目标位：" + str(target))
    choose()


def Toffoli():
    print("用矩阵表示0和1两个状态位")
    print("1---[[0],\n\t[1]]")
    print("0---[[1],\n\t[0]]")
    print("因为Toffoli门有三位，两个控制位，一个目标位，所以需要进行张量积运算")
    control_1 = int(input("请输入Toffoli门的第一位控制位:"))
    control_2 = int(input("请输入Toffoli门的第二位控制位:"))
    target = int(input("请输入Toffoli门的目标位:"))

    if control_1 == 0 and control_2 == 0:
        control_1 = np.array([[1], [0]])
        control_2 = np.array([[1], [0]])
    elif control_1 == 0 and control_2 == 1:
        control_1 = np.array([[1], [0]])
        control_2 = np.array([[0], [1]])
    elif control_1 == 1 and control_2 == 0:
        control_1 = np.array([[0], [1]])
        control_2 = np.array([[1], [0]])
    elif control_1 == 1 and control_2 == 1:
        control_1 = np.array([[0], [1]])
        control_2 = np.array([[0], [1]])

    if target == 0:
        target = np.array([[1], [0]])
    elif target == 1:
        target = np.array([[0], [1]])

    Toffoli = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0]])
    product = np.kron(control_1, control_2)
    product = np.kron(product, target)
    result = np.dot(Toffoli, product)
    if ((result == [[1], [0], [0], [0], [0], [0], [0], [0]]).all()):
        control_1 = 0
        control_2 = 0
        target = 0
    elif ((result == [[0], [1], [0], [0], [0], [0], [0], [0]]).all()):
        control_1 = 0
        control_2 = 0
        target = 0
    elif ((result == [[0], [0], [1], [0], [0], [0], [0], [0]]).all()):
        control_1 = 0
        control_2 = 1
        target = 0
    elif ((result == [[0], [0], [0], [1], [0], [0], [0], [0]]).all()):
        control_1 = 0
        control_2 = 1
        target = 1
    elif ((result == [[0], [0], [0], [0], [1], [0], [0], [0]]).all()):
        control_1 = 1
        control_2 = 0
        target = 0
    elif ((result == [[0], [0], [0], [0], [0], [1], [0], [0]]).all()):
        control_1 = 1
        control_2 = 0
        target = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [0], [1]]).all()):
        control_1 = 1
        control_2 = 1
        target = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [1], [0]]).all()):
        control_1 = 1
        control_2 = 1
        target = 0
    print("经过Toffoli门的转换,控制位：" + str(control_1))
    print("经过Toffoli门的转换,控制位：" + str(control_2))
    print("经过Toffoli门的转换,目标位：" + str(target))
    # print(result)
    choose()


def SWAP():
    print("用矩阵表示0和1两个状态位")
    print("1---[[0],\n\t[1]]")
    print("0---[[1],\n\t[0]]")
    print("因为SWAP门有三位，两个控制位，一个目标位，所以需要进行张量积运算")
    control = int(input("请输入SWAP门的第一位控制位:"))
    target_1 = int(input("请输入SWAP门的第一目标位:"))
    target_2 = int(input("请输入SWAP门的第二目标位:"))

    if control == 0:
        control = np.array([[1], [0]])
    elif control == 1:
        control = np.array([[0], [1]])

    if target_1 == 0:
        target_1 = np.array([[1], [0]])
    elif target_1 == 1:
        target_1 = np.array([[0], [1]])

    if target_2 == 0:
        target_2 = np.array([[1], [0]])
    elif target_2 == 1:
        target_2 = np.array([[0], [1]])

    swap = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 1, 0]])
    product = np.kron(target_1, target_2)
    product = np.kron(control, product)
    result = np.dot(swap, product)
    # print(result)
    if ((result == [[1], [0], [0], [0], [0], [0], [0], [0]]).all()):  # 000
        control = 0
        target_1 = 0
        target_2 = 0
    elif ((result == [[0], [1], [0], [0], [0], [0], [0], [0]]).all()):  # 001
        control = 0
        target_1 = 0
        target_2 = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [0], [0]]).all()):  # 010
        control = 0
        target_1 = 1
        target_2 = 0
    elif ((result == [[0], [0], [1], [0], [0], [0], [0], [0]]).all()):  # 011
        control = 0
        target_1 = 1
        target_2 = 1
    elif ((result == [[0], [0], [0], [1], [0], [0], [0], [0]]).all()):  # 100
        control = 1
        target_1 = 0
        target_2 = 0
    elif ((result == [[0], [0], [0], [0], [1], [0], [0], [0]]).all()):  # 101
        control = 1
        target_1 = 1
        target_2 = 0
    elif ((result == [[0], [0], [0], [0], [0], [1], [0], [1]]).all()):  # 110
        control = 1
        target_1 = 0
        target_2 = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [1], [0]]).all()):  # 111
        control = 1
        target_1 = 1
        target_2 = 1
    print("经过SWAP门的转换,控制位：" + str(control))
    print("经过SWAP门的转换,控制位：" + str(target_1))
    print("经过SWAP门的转换,目标位：" + str(target_2))
    choose()


def choose():
    print("-----------------------------------")
    print("1---NOT门\n" +
          "2---CNOT门\n" +
          "3---Toffoli门\n"
          "4---Swap门\n"
          "-1--退出")
    _NO = int(input("请输入你要选择的量子逻辑门："))
    print("-----------------------------------")
    if (_NO == 1):
        NOT()
    elif (_NO == 2):
        CNOT()
    elif (_NO == 3):
        Toffoli()
    elif (_NO == -1):
        return 0


if __name__ == '__main__':
    choose()
