import sys


def main():
    # 判断系统版本

    if sys.platform.startswith('linux'):
        print("当前系统是Linux")
    elif sys.platform.startswith('win32'):
        print("当前系统是Windows")
    elif sys.platform.startswith('darwin'):
        print("当前系统是macOS")
    else:
        print("当前系统是其他操作系统")


if __name__ == '__main__':
    main()
