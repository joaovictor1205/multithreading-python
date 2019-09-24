import threading
import time


class multithreading (threading.Thread):

    def __init__(self, threadID, nome):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = nome


    def run(self):
        print ("Initializing " + self.name)
        string = 'testetestetestetestetestetestetestetestetestetestetestetestetestetestetesteteste'

        for i in range(0, len(string)):
            if string[i].islower():
                aux_string = string[i].upper()
                string = string[:i] + aux_string + string[i+1:]
                print(string)

# Creating 30 threads
for i in range(30):
    thread = multithreading(i, "Thread")
    thread.start()

threads = []
threads.append(thread)

for t in threads:
    for i in range (0, 30):
        t.join()


print ("Finishing multithreading program")