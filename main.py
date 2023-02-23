import chatserver
import getopt
import sys

if __name__=="__main__":
    options, _ = getopt.getopt(sys.argv[1:], "-p:-h:")
    port = 9123
    host = '172.17.0.5'
    for key, value in options:
        if key == "-p":
            port = int(value)
        elif key == "-h":
            host = value
    chatserver.run(port, host)

    