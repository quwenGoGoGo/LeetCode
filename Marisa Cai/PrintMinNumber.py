'''
题目描述：
    输入一个正数数组，把数组里所有的数拼接起来排成一个数字，打印出能拼接出数字中最小的一个。
    例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字位321323
'''

'''
思考：
    将数组中的第一个数字和第二个数字正反连接，比较大小，正连接大的话就将第一个数字往后移一位；
    正连接小的话，开始比较第二个数字和第三个数字正反连接...
    也就是冒泡排序
'''

def theMax(str1, str2):
    '''定义字符串比较函数'''
    return str1 if str1+str2 > str2+str1 else str2


def PrintMinNumber(numbers):
    '''使用冒泡进行排序，把最大的放最后'''
    string = [str(num) for num in numbers]
    res = []
    flag = True
    count = len(string) - 1
    while flag and count > 0:
        flag = False
        for i in range(len(string)-1):
            if theMax(string[i], string[i+1]) == string[i]:
                temp = string[i]
                del string[i]
                string.insert(i+1, temp)
                flag = True
        count -= 1
    string = ''.join(string)
    return string

s = [int(i) for i in input('输入正数数组:').split()]
print(PrintMinNumber(s))
