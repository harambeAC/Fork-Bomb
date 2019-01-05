from multiprocessing import Process
import os

def run():
    os.fork()
    exec(open(__file__).read())

while(True):
    print("fork")
    p = Process(target=run)
    p.start()
