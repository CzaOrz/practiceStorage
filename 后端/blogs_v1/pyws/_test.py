from queue import Queue
import time
import threading
q = Queue()
def test():
    while True:
        data = q.get()
        print(data)
        if data:
            while True:
                print('hello ' + data)
                time.sleep(5)
                break

if __name__ == '__main__':
    q.put('cza1')
    q.put('cza2')
    q.put('cza3')
    q.put('cza4')
    # print(q.qsize())
    time.sleep(2)
    thread = threading.Thread(target=test)
    thread.start()
    time.sleep(3)
    q.put('cza')
    time.sleep(13)
    q.put('hei')



