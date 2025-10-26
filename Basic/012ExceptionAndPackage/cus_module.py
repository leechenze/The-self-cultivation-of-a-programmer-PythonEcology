


name = 'cus_module'

def funcA():
    print('funcA for cus_module')

def funcB():
    print('funcB for cus_module')

print("cus_module模块会显示出来的内容")

print(__name__)
if __name__ == "__main__":
    print("cus_module模块不会显示出来的内容")

