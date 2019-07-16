# !-*-coding:utf-8-*-
import ptn
import delete_str


def unpacking(file_path):
    with open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        # 在读取完read和write之后用jion()方法合并字符串，然后去空格
        reads = []  # 空read报文容器
        write = 0
        read = 0
        writes = []  # 空write报文容器
        for line in log.readlines():
            pid = ptn.ID(line)
            message_head = ptn.message_head(line)
            if pid:
                # 如果开头是pid文
                # 1.报文头
                # 2.连续的报文尾

                # 检测到新的头之后重置开关
                # write = False
                # read = False

                # 如果检测到报文类型关键词且是第一次出现
                if 'write2 .....' in line and write == 0:
                    write = 1
                    if read == 1:
                        read = 0  # 释放read开关节省时间
                elif 'read .....' in line and read == 0:
                    read = 1
                    if write == 1:
                        write = 0
                elif 'read from MISP len' in line and read != 0:
                    str_write = "".join(writes).replace("\n","")
                    str_reads = "".join(reads).replace("\n","")
                    return str_write,str_reads
                    break

            else:
                # 如果不是pid头
                if message_head:  # 只有可能是报文的头部被检测到了
                    if write:
                        # print("W:" + line)
                        writes += str(delete_str.get_pure_8583(ptn.message_head(line) + ": ", ptn.message_tail(line),
                                                              line)).split(" ")
                    if read:
                        # print("R:" + line)
                        reads += str(delete_str.get_pure_8583(ptn.message_head(line) + ": ", ptn.message_tail(line),
                                                             line)).split(" ")


if __name__ == '__main__':
    print(unpacking("5897"))
