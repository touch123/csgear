import ptn
import os

file_path = "qrcodetran.20190420"
catalog = []


def mk_catalog():
    with open(file_path, 'r', encoding='gb2312', errors='ignore') as file:
        line = file.readline()
        while line is not None and line != '':
            n = ptn.ID(line)
            if n:
                # mk_file(n, line)
                if n not in catalog:
                    # print("GET : " + line)
                    # print("POST : " + n)
                    catalog.append(n)
            else:
                if len(catalog):
                    pass
                    # mk_file(catalog[-1], line)
                    # print("写" + catalog[-1] + "的报文:" + line)
            line = file.readline()

        return catalog


def mk_dir(dir_path):
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        os.mkdir(dir_path)
        print("📂 " + dir_path + " was created.")
        return True
    else:
        return False


def mk_file(num, content):
    with open(num, 'a+') as file:
        file.write(content)


if __name__ == '__main__':
    mk_catalog()
    print(catalog)
# mk_file("12345", "[03:10:01 - 3546] : begin pack DE 4")
