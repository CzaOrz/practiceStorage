__file__ = 'Note'

"""
字符集：就是用来定义字符在数据库中的编码的集合
常见的字符集：utf-8、unicode、gbk、、gb2312、ascii...

排序规则：就是指字符比较时是否区分大小写，以及是按照字符编码进行比较直接用二进制数据比较

"""


"""
SQL注入攻击，通过把sql指令插入到web表单递交或输入域名或页面请求的查询字符串，达到欺骗服务器执行恶意的SQL命令 -- 攻击后台服务器


XSS：跨站脚本攻击，为了与css区分开来，缩写为XSS，两种形式：
1、XSS反射型攻击。通过恶意连接，诱导用户点击然后或发送用户的私密信息。比如陌生人发送一张图片给你，你点击后就会执行他所定义的恶意代码。这种属于反射型。
2、XSS存储型攻击，恶意代码保存到目标服务器中。比如发表评论<script>....</script>，将恶意代码存储到服务器中，每当有点点击时改代码就会执行。
xss是利用站点内的信任用户。与csrf不同，csrf是通过伪装成受信任用户的请求来利用获取资源，


CSRF：跨站请求伪造，劫持受信任用户向服务器发送恶意请求的攻击方式。
"""