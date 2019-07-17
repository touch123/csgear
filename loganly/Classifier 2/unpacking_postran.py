# !-*-coding:utf-8-*-
import ptn
import json
import reader
import codecs


def unpacking_postran(file_path):
    result = []  # 空结果列表，采集完了再把列表变成字典
    with codecs.open(file_path, 'r', encoding='gb2312', errors='ignore') as log:
        words = list(ptn.postran_key_words)
        rules = list(ptn.postran_key_words.values())
        for line in log.readlines():
            # 一次性匹配多个关键词
            for i in range(0, len(words)):
                if words[i] in line:
                    if rules[i]:
                        data = ptn.DIYSearch(rules[i], line)
                        if data:
                            result.append((words[i], data))
                            rules[i] = None

    return json.dumps(dict(result))


if __name__ == '__main__':
    #  print(unpacking_postran("5893"))
    for item in reader.file_name("log//classified_log//postran.20190116"):
        print(item + " : " + unpacking_postran("log//classified_log//postran.20190116//" + item))
