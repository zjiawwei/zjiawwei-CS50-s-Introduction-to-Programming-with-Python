def convert():
    str = input("请输入英文内容：")
    str = str.replace(':)','🙂')
    str = str.replace(':(','🙁')
    print (str)

def main():
    return convert()
main()