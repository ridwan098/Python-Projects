import threading

class RidwansMessenger(threading.Thread):

    def run(self):
        for i in range(10):
            print(threading.currentThread().getName())


x = RidwansMessenger(name='Send out messages')
y = RidwansMessenger(name='Receive messages')

x.start()
y.start()
