# csgear
## logspider 日志爬虫插件
  根据配置文件抓取系统中指定的日志文件，并根据规则拆分，并提取关键信息。提供查询工具根据输入信息查找定位目标文件，并友好地显示。
  
## 使用范例
python logspider.py [ filedate ]  [ logtype ] 
参数：

例子：

## 依赖
pip install PyYAML

## 配置
配置文件应有：日志文件目录、日志文件类型、日志关键信息提取规则、处理中间文件的存放目录、数据库的目录、处理结果文件的目录、日志过滤规则、以及其他程序功能配置。

## 功能模块

1. 日志文件检测器 sensor

   根据配置文件中的日志目录，检测系统中存在的日志文件，登记到数据库中，并将状态设为未处理，如数据库中文件记录已经存在，则不覆盖。

输入：
  日志目录

输出：
  数据库

1. 日志采集器 spider

  日志按设定地规则（如进程号）拆分日志文件，根据抓取规则提取关键信息，并记录到采样数据库（或文件中）。

输入：
 
  日期：如有参，执行指定日期的处理，原先处理过的，也先删除数据库中的记录，重新处理
        如无参, 从日志文件登记表中取未处理的日志，进行处理，并登记

  日志类型： 
       日志类型是日志文件名的主要部分， 如postran, mis_clt, qrcodetran， qr_clt  等

输出：
  拆分出的进程文件写入配置文件指定的目录， 写入配置文件中指定的数据库文件。
  运行时间比较长，则同时也要输出执行过程、执行结果


1. 日志查询器 finder      
 
   1. 根据输入的信息，到采样数据库检索并返回json格式的结果信息。返回信息应包含有结果文件路径、关键信息等
   关键信息如：RRN, date, amount, termid, countno, orderid
   
   2. 根据输入数据，到拆分的文件中查找包含该数据的文件名称，可一次同时处理多个文件。

输入：
  查询字符串， 以空格分隔多个条件参数。可以根据文本自动识别每个条件参数，
  如 123.10 识别为 金额， 12位数字字符串识别为 参考号， 6位数字字符串识别为 流水号 等等。
  识别后转为json 格式的参数字符串
 
输出：
 josn格式的文件名列表

   
1. 过滤器  filter
 
   根据设定的排除和包含的过滤规则，过滤掉无用杂乱的信息，
   同时也可根据设定的规则替换原有的信息，达到将日志文本转译为可读性更好的文本。   
   
输入：
   日期、日志类型、进程号、（配置文件中的规则）

输出：
   例：XX卡在XX终端 消费 XX 元，参考号为XX，订单号为XXX
   
1. 本模块可由其他python程序导入，作为csgear的一个插件运行，csgear 可以运行并显示结果。   

## TODO


## 事件/计划
* 2019/07/26 实现过滤器
* 2019/07/26 实现查询器
* 2019/07/18 部署docker 运行
* 2019/07/17 采集内容入sqlite, 插件并入csgear平台
* 2019/07/16  yaml配置文件，iso8583解包
* 2019/07/15  拆分文件，优化，提交代码库
