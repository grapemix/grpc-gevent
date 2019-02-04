# -*- coding: utf-8 -*-
#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()
#monkey.patch_all(thread=False)

import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()

import gevent
import grpc

import concurrent.futures
from gevent.threadpool import ThreadPoolExecutor
concurrent.futures.ThreadPoolExecutor = ThreadPoolExecutor

import pb.echoserver_pb2 as echoserver
import pb.echoserver_pb2_grpc as echoserver_grpc

import sys

class Echoer(object):
    count = 10
    def Echo(self, req, context):
        print("Received {} message {}: {}".format(self.count, req.id, req.message))
        gevent.sleep(req.sleep_seconds)
        print("Finished {} message {}: {}".format(self.count, req.id, req.message))
        self.count -= 1
        return echoserver.Response(id=req.id, message=req.message)

def main():
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24

    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    echoserver_grpc.add_EchoerServicer_to_server(Echoer(), server)
    server.add_insecure_port('[::]:12345')
    server.start()
    try:
        while True:
            gevent.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
      server.stop(0)

if __name__ == '__main__':
    main()

