#### 基础信息
* 个人信息
    * 工作年限：2年（2018.04~至今）
    * 最高学历：本科/学士
    * 籍贯：湖北咸宁
    * 现居地：武汉
    * 工作状态：在职
    * 当前薪资：56iO5ZCONWsK
    * Github: https://github.com/CzaOrz
* 求职意愿
    * 职位：python后端 / python相关
    * 城市：武汉 / 深圳
    * 薪资：5q2m5rGJOGsgLyDmt7HlnLMxMGsK
<hr>

#### 工作经历
* 2018.04-2019.03 / 武汉****有限公司 / 驱动开发工程师
    * 工作说明：
        * 业务性质为华为外包，虽职务为驱动开发，但甲方制度严格，基本没机会接触硬件。日常主要工作为:<br>
        1、荣耀系列产品性能测试，需求配置，beta问题处理<br>
        2、海外定制需求的配置<br>
        3、舆情数据分析与汇总
    * 其他说明：
        * 工作情况：四月进公司实习，七月领毕业证后正式进入试用期，八月因日常工作积极，总体表现优秀而提前转正。<br>
        * 辞职原因：5Y2O5Li65aSW5YyF5oC75L2T5p2l6K+05YGP5Lia5Yqh77yM6Zq+5bqm5LiN5aSn77yM5L2G5bel5L2c5by65bqm6auY77yM5a+56Ieq5bex5o+Q5Y2H5LiN5aSn44CCCg==
* 2019.03-至今 / 武汉****有限公司 / 爬虫开发工程师
    * 工作说明：<br>
        1、基于公司现有的爬虫框架，负责政府公开信息领域的爬虫开发<br> 
        2、特殊爬虫开发与维护（裁判文书网——JS加密、搜狗微信——验证码）<br>
        3、组内业务流程优化分析<br>
        4、组内数据消费（新闻分类、统计）
    * 其他说明：
        * 工作情况：整体工作表现优异，有责任心，由基础爬虫开发到承接特殊爬虫、pdf转码、数据分析等任务。
        * 辞职原因：MTnlubTlupXvvIznlLHkuo7kuJrliqHlj4rkurrlkZjlronmjpLljp/lm6DvvIzmnKzkurrlnKjlhazlj7jot5Hov4fnn63mnJ/kuJrliqHvvIzlkI7luIzmnJvmiJHplb/mnJ/otJ/otKPor6XkuJrliqHvvIzkuqTosIjml6DmnpzjgIIK
<hr>

#### 项目经验
* 分布式爬虫调度系统
    * 项目说明：
        * 基于Flask、Flask-Apscheduler、Scrapy、RabbitMQ、Redis、Mongodb等搭建的分布式爬虫调度系统。并提供一定数据分析服务<br>
        提供线上爬虫调度管理，服务端以RabbitMQ作为broker，发布调度任务，消费节点则订阅并执行调度任务。支持多节点并行处理任务。<br>
        整体上大致由server、salve、task三个模块组成。 
        server提供后端接口服务，调度任务仅需指定任务名。salve配置有具体的调度规则，是命令的执行者。
        task（爬虫）独立于系统外，单独有git维护，salve调度时自更新。
        在发布订阅基础上，建立 RPC 通道，提供Server管理与收录各节点状态的能力。<br>
        任务状态保存于redis中，日志和数据则存入mongodb。<br>
        针对某些异常情况（强制杀进程、task/salve crash）产生的脏数据，引入定时回查机制，确保redis中任务状态的一致性。<br> 
    * 项目架构图：http://www.czasg.xyz/static/img/spider_scheduler.jpg
    * demo：https://czaorz.github.io/ioco/open_source_project/spider_scheduler/scheduler.html
* 开源项目Pywss
    * 项目说明：
        * 基于socket编写，旨在快速搭建简易websocket服务端。详情见项目链接。
    * 项目链接： https://github.com/CzaOrz/Pywss
    * demo： https://czaorz.github.io/Pywss/client
<hr>

#### 技能专长
* 熟悉Python，了解HTML/CSS/JavaScript/Bootstrap/Vue等Web前端技术。
* 熟悉Scrapy框架，熟悉正则与xpath的使用，配套有自己的爬虫工具包。
* 熟悉Flask/Django等后端框架。
* 熟悉TCP/IP、HTTP协议和WebSocket通信，开源项目Pywss用于快速搭建WebSocket服务端。
* 了解基础机器学习算法。实现过自如房价图像识别，政府新闻分类，房价预测等。
* 了解MySQL、Redis、Mongodb等数据库的基本使用。
<hr>

#### 自我评价
* 有较强的学习能力和接受能力。钟爱python，愿意接受任何python相关知识。<br>
目前涉及领域包括爬虫、前端、后端、数据分析。希望将来能涉及全栈工程师和人工智能领域。<br>
暂时爬虫稍强，但也希望以此为引，深入python web方向。
