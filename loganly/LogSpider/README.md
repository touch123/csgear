## Spider 日志采集器

日志按设定地规则（如进程号）拆分日志文件，根据抓取规则提取关键信息，并记录到采样数据库（或文件中）。每天定时运行作为预处理

- 输入：
  日期：如有参，执行指定日期的处理，原先处理过的，也先删除数据库中的记录，重新处理
  如无参, 从日志文件登记表中取未处理的日志，进行处理，并登记
  日志类型： 
  日志类型是日志文件名的主要部分， 如postran, mis_clt, qrcodetran， qr_clt 等
- 输出：
  拆分出的进程文件写入配置文件指定的目录， 写入配置文件中指定的数据库文件。
  运行时间比较长，则同时也要输出执行过程、执行结果

### 流程

1.Dealer根据设定的规则遍历Log文件夹下的文件，并根据PID对文件进行拆分

3.Unpacking遍历classified文件夹下的拆分出来的文件，并通过配置文件中的正则提取关键词，或者做特殊处理

4.将提取Unpacking出来的数据通过DBMS入库

![流程图](https://raw.githubusercontent.com/0xC000005/image-hosting/master/20190802091845.png)

### 用法

python Spider.py [fileDate] [logType]

### 依赖环境

Python 2.7，需要PYymal库，docker环境下启