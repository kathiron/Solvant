import threading
import time

class mythreadapp:
    def __init__(self):
        # TODO document why this method is empty
        pass
    
    def worker(self, num):
        print('------------')
        for i in range(5):
            print(f"Worker {num}: {i}")
            time.sleep(1)

    def callthread(self):
        threads = []
        for i in range(3):
            t = threading.Thread(target=self.worker, args=(i,)) # type: ignore
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("All threads finished")