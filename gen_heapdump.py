import sys

def gen_heapdump(server, node):
   instance=AdminControl.queryNames("type=JVM,process="+server+",node="+node+",*")
   AdminControl.invoke(instance, 'generateHeapDump')


if len(sys.argv) > 0 and sys.executable is None:
    gen_heapdump(sys.argv[0], sys.argv[1])
elif sys.executable is None:
    server=raw_input("Server name: ")
    node=raw_input("Node name: ")
    gen_heapdump(server, node)
else:
    #Get list of servers and print list for selection.
    print """
    This script will pause one or more generated a heapdump for an application server
    Usage:

       wsadmin.sh -lang jython -f genheapdump.py

    or

       wsadmin.sh -lang jython -f genheapdump.py <servername> <nodename>

    Note: This script should only be used with wsadmin, not python.
    """
