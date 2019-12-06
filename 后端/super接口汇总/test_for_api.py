import requests

URL = "http://127.0.0.1:8888/"


def test4(): print(requests.post(f"{URL}04", data={'cz': 'cza', 'cza': 'cza'}).text)


def test5(): print(requests.post(f"{URL}05", json={'cz': 'cza'}).json())


def test6(): print(requests.get(f"{URL}06", cookies={'cza': 'hei', 'man': 'are you ok'}).json())


def test7(): print(requests.post(f"{URL}07", cookies={'cza': 'hei', 'man': 'are you ok'}).json())


def test8(): print(requests.get(f"{URL}08").status_code)


def test9():
    print(requests.get(f"{URL}09").text)
    print(requests.get(f"{URL}09").status_code)


def test10(): print(requests.post(f"{URL}10").text)


def test11(): print(requests.post(f"{URL}11").text)


def test14():
    files = {'file': open('cza.xls', 'rb')}
    files = {'file': ('cza.xls', open('cza.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
    files = {'file': ('fileName.txt', 'file content\nfile body')}
    print(requests.post(f"{URL}14", files=files).text)


def test15(): print(requests.get(f"{URL}15", cookies={'cza': 'cza-is-sg', 'orz': 'cza-is-sg'}).status_code)


def test16(): print(requests.get(f"{URL}16", cookies={'cza': 'cza-is-sg', 'orz': 'cza-is-sg'}).status_code)


def test17(): print(requests.options(f"{URL}17", cookies={'cza': 'cza-is-sg', 'orz': 'cza-is-sg'}).headers)


if __name__ == '__main__':
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    # test11()
    test14()
    # test15()
    # test16()
    # test17()
