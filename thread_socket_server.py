#!/usr/bin/env python
# encoding: utf-8

import SocketServer
import commands

class MySockServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print 'Got a new conn from',self.client_address
        while True:
            cmd = self.request.recv(1024)
            if not cmd:
                print 'Lost connection with',self.client_address
                break
            #print 'recv:',data

            cmd_result = commands.getstatusoutput(cmd)
            self.request.send(cmd_result[1])

if __name__ == '__main__':
    h = '0.0.0.0'
    p = 9001
    s = SocketServer.ThreadingTCPServer((h,p),MySockServer)

    s.serve_forever()
