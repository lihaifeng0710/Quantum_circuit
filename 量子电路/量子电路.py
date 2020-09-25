import numpy as np
Result=np.array([0,0,0])

def NOT(place):
    """
    :param place: Result[place] 取反
    :return:
    """
    a = Result[place]
    _not = np.array([[0, 1],
                     [1, 0]])
    if a == 1:
        begin = np.array([[0], [1]])
        result = np.dot(_not, begin)
    elif a == 0:
        begin = np.array([[1], [0]])
        result = np.dot(_not, begin)
    if ((result == [[1], [0]]).all()):
        Result[place]=0
    elif ((result == [[0], [1]]).all()):
        Result[place] = 1
    print(Result)

def CNOT(place1,place2):
    """
    :param place1: Result[place1]为控制位
    :param place2: Result[place2]为目标位，当控制为1，目标为取反
    :return:
    """
    control = Result[place1]
    target = Result[place2]
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
        Result[place1]=0
        Result[place2]=0
    elif ((result == [[0], [1], [0], [0]]).all()):
        Result[place1] = 0
        Result[place2] = 1
    elif ((result == [[0], [0], [0], [1]]).all()):
        Result[place1] = 1
        Result[place2] = 1
    elif ((result == [[0], [0], [1], [0]]).all()):
        Result[place1] = 1
        Result[place2] = 0
    print(Result)

def Swap(place1,place2):
    """
    Result[place1]与Result[place2]交换
    :param place1:
    :param place2:
    :return:
    """
    target_1 = Result[place1]
    target_2=Result[place2]
    temp = target_1
    target_1 = target_2
    target_2 = temp
    Result[place1]=target_1
    Result[place2]=target_2

def Toffoli(place1,place2,place3):
    """
    :param place1: Result[place1]为控制位
    :param place2: Result[place2]为控制位
    :param place3: 当Result[place1]和Result[place2]都为1时，Result[place3]取反
    :return:
    """
    control_1 = Result[place1]
    control_2 = Result[place2]
    target = Result[place3]
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
        Result[place1]=0
        Result[place2]=0
        Result[place3]=0
    elif ((result == [[0], [1], [0], [0], [0], [0], [0], [0]]).all()):
        Result[place1] = 0
        Result[place2] = 0
        Result[place3] = 1
    elif ((result == [[0], [0], [1], [0], [0], [0], [0], [0]]).all()):
        Result[place1] = 0
        Result[place2] = 1
        Result[place3] = 0
    elif ((result == [[0], [0], [0], [1], [0], [0], [0], [0]]).all()):
        Result[place1] = 0
        Result[place2] = 1
        Result[place3] = 1
    elif ((result == [[0], [0], [0], [0], [1], [0], [0], [0]]).all()):
        Result[place1] = 1
        Result[place2] = 0
        Result[place3] = 0
    elif ((result == [[0], [0], [0], [0], [0], [1], [0], [0]]).all()):
        Result[place1] = 1
        Result[place2] = 0
        Result[place3] = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [0], [1]]).all()):
        Result[place1] = 1
        Result[place2] = 1
        Result[place3] = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [1], [0]]).all()):
        Result[place1] = 1
        Result[place2] = 1
        Result[place3] = 0
    print(Result)

def CSWAP(place1,place2,place3):
    """
    Result[place1]为控制位
    Result[place2]，Result[place3]为目标位
    当Result[place1]为1时，交换Result[place2]，Result[place3]
    :param place1:
    :param place2:
    :param place3:
    :return:
    """
    control = Result[place1]
    target_1 = Result[place2]
    target_2 = Result[place3]
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
        Result[place1] = 0
        Result[place2] = 0
        Result[place3] = 0
    elif ((result == [[0], [1], [0], [0], [0], [0], [0], [0]]).all()):  # 001
        Result[place1] = 0
        Result[place2] = 0
        Result[place3] = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [0], [0]]).all()):  # 010
        Result[place1] = 0
        Result[place2] = 1
        Result[place3] = 0
    elif ((result == [[0], [0], [1], [0], [0], [0], [0], [0]]).all()):  # 011
        Result[place1] = 0
        Result[place2] = 1
        Result[place3] = 1
    elif ((result == [[0], [0], [0], [1], [0], [0], [0], [0]]).all()):  # 100
        Result[place1] = 1
        Result[place2] = 0
        Result[place3] = 0
    elif ((result == [[0], [0], [0], [0], [1], [0], [0], [0]]).all()):  # 101
        Result[place1] = 1
        Result[place2] = 1
        Result[place3] = 0
    elif ((result == [[0], [0], [0], [0], [0], [1], [0], [1]]).all()):  # 110
        Result[place1] = 1
        Result[place2] = 0
        Result[place3] = 1
    elif ((result == [[0], [0], [0], [0], [0], [0], [1], [0]]).all()):  # 111
        Result[place1] = 1
        Result[place2] = 1
        Result[place3] = 1


if __name__ == '__main__':
    NOT(1)
    CNOT(1, 2)
    Toffoli(2,1,0)