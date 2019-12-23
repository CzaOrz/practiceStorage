### [Web](#Web)
* [TCP����Э��](#TCP����Э��)
* [HTTP](#HTTP)
* [WSGI](#WSGI)
* [MVC](#MVC)
* [Flask](#Flask)
* [Django](#Django)

----------

## web
webӦ�õı��ʡ��ͻ��˷���HTTP���󣬷���˽�������������Ӧ����������һ��Html�ļ���
Ȼ��������Ѵ�Html�ļ���ΪHTTP��Ӧ��Body���͸��ͻ��ˣ��ɿͻ��˽��к�������ʾ����


#### TCP����Э��


#### HTTP
HTTP��һ���ı�Э�飬Ҳ�ǳ��õ�����ͨ��Э�顣

һ��HTTP�¼�������Header��Body���¼�ͨ����Ϊ�����¼�����Ӧ�¼���

�����¼�Header�У���Ҫ��ͷ�ͱ��ġ�Body�Ǹ�������ʽ�Ŀ�ѡ�¼�
* **GET / HTTP/1.1** ��ͷ��������ʽ������·����Э��汾
* **Host: www.google.com** ��������Key:Value�Ľṹ���

��Ӧ�¼�Header�У�Ҳ������ͷ�ͱ��ģ�Body������������������ܿ���������
* **HTTP/1.1 200 OK** ��Ӧ��ͷ�а���Э��汾����Ӧ״̬�롢��Ϣ˵��
* **X-Powered-By: Express** ������һ������Key:Value�Ľṹ���

Header֮����\r\n���л��֣���������\r\n\r\n������������ȫΪbody��

200�ɹ���3xx�ض���4xx�ͻ����쳣��5xx������쳣


#### WSGI
**Web-Server-Gateway-Interface** web���������ؽӿ�

��򵥵�webӦ�þ����Ȱ�html�ļ�����ã������е�HTTP�����������û�����Ȼ��ֱ�ӷ������е�html�ļ���
��������ǳ�˵�ľ�̬����������Nginx�ȡ�

��ʵ����һ��webӦ�ÿ��ܸ��ӵĶ࣬��Ҫ���ǻ�ȡHTTP������Ϣ��������Ȼ��������Ӧ�Ĵ����ٴ�����ء�
��Ϊ�˼򻯿�����WSGI�ӿڳ����ˡ���ʵ���˶�HTTP����ĳ�����װ���Ա�webӦ�ý��к����Ĵ���

һ��WSGI�ӿڣ���װHTTP����󣬻�ΪwebӦ���ṩ�����������ֱ�Ϊenviron��start_response��
* **environ** �˲�����һ��dict���󣬰�����������HTTP������Ϣ
* **start_response** �˲�����һ���������������ڷ���HTTP��Ӧ���ĵĺ���

webӦ�ã���WSGI�ӿ��л�ȡ���������������к����Ĵ���ҵ���߼���ɺ�
�����ҽ��ܵ���һ��start_response���������ڷ�����Ӧ����
```start_response("200 fucking", [("Content-Type", "this/is/a/joking")])```��
�˺�������������������һ������Ӧ��ͷ���������״̬�����Ϣ˵�����ڶ�������Ӧ���ģ���һ��list��
��Ԫ����tuple��tuple�ڲ�Ϊ����string���ֱ��Ӧ�ű����е�Key:Value
```
from wsgiref.simple_server import make_server
def test_app(environ, start_response):
    start_response("200 fucking-man", [("Content-Type", "text/html")])
    return [b"hello, funking man"]
web = make_server("", 8888, test_app)
web.serve_forever()
```


#### MVC
Model-View-Controller ���� ģ��-��ͼ-������

python��˴����У�������·�ɵĺ��������࣬���ǿ���������Ҫ����ҵ���߼�

����jinjia2��Django�Դ�ģ���ܣ�����һЩ����{{}}����������ļ���������ͼ����Ҫ������ʾ�߼���
Ҳ����ͨ��һЩ�򵥵��滻���������յ���ʾҳ�档

��ҵ���߼� ���ݸ� ��ʾ�߼� �Ĳ��֣�����Modelģ�塣��������һ���ֵ䣬Ҳ��һ��ӳ���
���û���Ϊ����Ⱦ��ͼ������Ŀ��ģ��

MVC�ܹ�������������ҵ���߼�����ʾ�߼���


#### Flask


#### Django