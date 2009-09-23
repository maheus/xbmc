#!/usr/bin/python

import sys
import getopt
from socket import *
try:
    from xbmc.xbmcclient import *
except:
    sys.path.append('../../lib/python')
    from xbmcclient import *

def usage():
    print "xbmc-send [OPTION] --action=ACTION"
    print 'Example'
    print '\txbmc-send --host=192.168.0.1 --port=9777 --action="XBMC.Quit"'
    print "Options"
    print "\t-?, --help\t\t\tWill bring up this message"
    print "\t--host=HOST\t\t\tChoose what HOST to connect to (default=localhost)"
    print "\t--port=PORT\t\t\tChoose what PORT to connect to (default=9777)"
    print '\t--action=ACTION\t\t\tSends an action to XBMC, this option can be added multiple times to create a macro'
    pass

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "?pa:v", ["help", "host=", "port=", "action="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    ip = "localhost"
    port = 9777
    actions = []
    verbose = False
    for o, a in opts:
        if o in ("-?", "--help"):
            usage()
            sys.exit()
        elif o == "--host":
            ip = a
        elif o == "--port":
            port = int(a)
        elif o in ("-a", "--action"):
            actions.append(a)
        else:
            assert False, "unhandled option"
    
    addr = (ip, port)
    sock = socket(AF_INET,SOCK_DGRAM)
    
    if len(actions) is 0:
        usage()
        sys.exit(0)
    
    for action in actions:
        print 'Sending action:', action
        packet = PacketACTION(actionmessage=action, actiontype=ACTION_BUTTON)
        packet.send(sock, addr)

if __name__=="__main__":
    main()
