# csgear
## loganly 日志分析插件

## 模块
1. 配置文件
  配置文件应有：日志文件目录、日志文件类型、日志关键信息提取规则、处理中间文件的存放目录、数据库的目录、处理结果文件的目录、日志过滤规则、以及其他程序功能配置。

1. 日志文件检测器
功能：
   根据配置文件中的日志目录，检测系统中存在的日志文件，登记到数据库中，状态设为未处理

1. 日志采集器
功能:
  按进程号拆分日志文件，提取关键信息
参数：
  日期：如有参，执行指定日期的处理，原先处理过的，也先删除数据库中的记录，重新处理
        如无参, 从日志文件登记表中取未处理的日志，进行处理，并登记
  日志类型： 
       postran, mis_clt, qrcodetran， qr_clt  等

1. 日志查询器       
 功能：
   1. 根据数据库有的关键字段，到数据库检索指定数据，返回json格式的结果信息，包含结果文件路径，关键信息
   关键信息：RRN, date, amount, termid, countno, orderid
   2. 根据输入数据，到拆分出得文件中查找包含该数据的文件名称，要求：并发或多线程同时处理多个文件。
   
1. 过滤器
功能： 
   根据设定的规则，过滤掉无用杂乱的信息，
   也可根据设定的规则替换原有的信息，达到转译日志文件为可读性好的文本
   
1. 作为csgear的插件运行。   

## TODO

~~1. 拆分 ~~
1. 采集
1. 入库
1. docker 运行环境
1. django 前端

## 事件/计划
* 2019/07/18 部署docker 运行
* 2019/07/17 采集内容入sqlite, 插件并入csgear平台
* 2019/07/16  yaml配置文件，iso8583解包
* 2019/07/15  拆分文件，优化，提交代码库
