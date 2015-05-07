import sys


def gen_heapdump(server, node):
    instance = AdminControl.queryNames("type=JVM,process="+server+",node="+node+",*")
    AdminControl.invoke(instance, 'generateHeapDump')


if len(sys.argv) > 0 and sys.executable is None:
    gen_heapdump(sys.argv[0], sys.argv[1])
elif sys.executable is None:
    cells = AdminConfig.list('Cell').split()
    nodelist = []
    for cell in cells:
        nodes = AdminConfig.list('Node', cell).split()
        for node in nodes:
            cn = AdminConfig.showAttribute(cell, 'name')
            nn = AdminConfig.showAttribute(node, 'name')
            nodelist.append([nn, cn])
        selection = ''
        while isinstance(selection, (int, long)):
            print "Select an option:"
            for item in nodelist:
                name = item[0]
                print (nodelist.index(name)+1)+". "+name
            selection = raw_input("Enter selection: ")
            if int(selection) > len(nodelist):
                selection = ''
        nn = [int(selection)-1][0]
        cn = [int(selection)-1][1]
        servers = AdminControl.queryNames('type=Server,cell='+cn+',node='+nn+',*').split()
        serverlist = []
        for server in servers:
            sn = AdminConfig.showAttribute(server, 'serverName')
            serverlist.append(sn)
        selection = ''
        while isinstance(selection, (int, long)):
            print "Select an option:"
            for item in serverlist:
                print (serverlist.index(item)+1)+". "+item
            selection = raw_input("Enter selection: ")
            if int(selection) > len(serverlist):
                selection = ''
        sn = serverlist(int(selection)-1)
    gen_heapdump(sn, nn)
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
