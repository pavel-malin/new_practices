# Running worker with ZeroMQ
import multiprocessing
import random
import zmq


def compute():
    return sum([random.randint(1, 100) for i in range(1000000)])


def worker():
    context = zmq.Context()
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect("tcp://0.0.0.0:5555")
    result_sender = context.socket(zmq.PUSH)
    result_sender.connect("tcp://0.0.0.0:5556")
    poller = zmq.Poller()
    poller.register(work_receiver, zmq.POLLIN)

    while True:
        socks = dict(poller.poll())
        if socks.get(work_receiver) == zmq.POLLIN:
            obj = work_receiver.recv_pyobj()
            result_sender.send_pyobj(obj())


context = zmq.Context()
# We create a channel for sending work
work_sender = context.socket(zmq.PUSH)
work_sender.bind("tcp://0.0.0.0:5555")
# We create a channel for receiving results
result_receiver = context.socket(zmq.PULL)
result_receiver.bind("tcp://0.0.0.0:5556")
# We start 4 works
processes = []
for x in range(4):
    p = multiprocessing.Process(target=worker)
    p.start()
    processes.append(p)

# We send 4 works
for x in range(4):
    work_sender.send_pyobj(compute)

# We get 4 works
results = []
for x in range(4):
    results.append(result_receiver.recv_pyobj())

# We complete the processes
for p in processes:
    p.teminate()

print("Results: %s" % results)
