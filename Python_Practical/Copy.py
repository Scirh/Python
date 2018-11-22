#Author Scon
# -*- coding utf-8 -*-
# help()


# 模拟cp操作

def copy(src_file,dst_file):

        with open(src_file,'rb') as src_boj:
            src_data = src_boj.read()
        with open(dst_file,'wb') as dst_obj:
            if not src_data:        # 如果数据为空的话就结束程序
                exit()
            dst_obj.write(src_data)

if __name__ == '__main__':
    while True:
        try:
            file = input("Please enter the file that you want to copy:").strip()
            file_name = input("\nPlease enter the location you want to copy to:").strip()
            copy(file,file_name)
            print("\nSuccessful!")
        except FileNotFoundError:
            print("\n\033[31;1mPlease enter the file path.Try again.\033[0m")
        except KeyboardInterrupt:
            print("\nGoodBye!")
            break
        else:
            break
