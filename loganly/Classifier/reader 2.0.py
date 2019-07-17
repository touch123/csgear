# -*- coding : utf-8
import ptn
import os

catalog = []


def mk_catalog(file_path):
    count = 0
    old_present = 0
    with open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        path = str("classified_" + log.name)
        mk_dir(path)
        lines = log.readlines()
        current_pid = 0
        file = None
        for line in lines:
            count += 1
            pid = ptn.ID(line)
            if pid:
                if pid not in catalog:  # 不在源目录里面的新pid
                    file = open(path + "\\" + pid, 'a+')  # 创建新文件
                    catalog.append(pid)

                if pid != current_pid:  # 当前的pid和连续的pid不一样
                    file.close()
                    file = open(path + "\\" + pid, 'a+')
                    file.write(line)
                else:  # 连续的pid
                    file.write(line)
                current_pid = pid  # 当前pid设置为和目录不一样的pid
            else:  # 数字开头的十六进制报文
                if file:
                    file.write(line)
                    if round(count / len(lines) * 100) != old_present:
                        print("Classifing: " + str(log.name) + "...... " + str(round(count / len(lines) * 100)) + "%")
                        old_present = round(count / len(lines) * 100)
                    else:
                        pass

        return catalog


def mk_dir(dir_path):
    is_exist = os.path.exists(dir_path)
    if not is_exist:
        os.mkdir(dir_path)
        print("📂 " + dir_path + " was created.")
        return True
    else:
        return False


if __name__ == '__main__':
    mk_catalog("qrcodetran.20190420")
    mk_catalog("postran.20190116")
    mk_catalog("mis_clt.20190116")
