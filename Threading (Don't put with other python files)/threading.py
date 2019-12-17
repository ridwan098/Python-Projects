# threading

# this allows you to do multiple things at the same time
# instead of going to step to the other

# most of the time, this is not a good idea beacaue you want to go
# one step at a time
# for example a calaculation, where you have BODMAS

# this is useful if you are building something like a messenger program
# and you want it to be able to receive whilst also sending
# so you dont have to wait for them to respond before you send


import time
import threading

class RidwansMessenger(threading.Thread): # threading.Thread is the built in parent class

    def run(self): # 'run' is an inbuilt name that means something special to thread

        for _ in range(10): # you can use _ instead of numbers
                               # to represent numbers
                               # just for it to loop ten time

            print(threading.currentThread().getName())
            

x = RidwansMessenger(name = 'Send out messages\n')
y = RidwansMessenger(name = 'Receiving messages')

x.start() # to call it, you use. start
y.start()

