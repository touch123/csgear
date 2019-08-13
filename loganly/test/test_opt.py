# -*- coding: utf-8 -*-
# @Time : 2019/7/26 10:28
# @Author : Max
# @FileName: test.py
# @IDE: PyCharm

from optparse import OptionParser


def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-e", "--environment",
                      action="store_true",
                      dest="environment",
                      default="linux",
                      help=u"通过配置文件在Windows和Linux环境之间切换", )
    parser.add_option("-d", "--date",
                      action="store_true",
                      dest="FileDate",
                      default=False,
                      help=u"指定Spider处理的日志的日期范围")
    parser.add_option("-t", "--type",
                      action="store_true",  # optional because action defaults to "store"
                      dest="LogType",
                      default=False,
                      help=u"指定Spider处理的日志的类型", )
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options
    print args


if __name__ == '__main__':
    main()
