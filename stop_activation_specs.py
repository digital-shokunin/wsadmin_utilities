import sys


def stop_as(*act_specs):
    for as in act_specs:
        as_results = AdminControl.queryNames("type=J2CMessageEndpoint,ActivationSpec="+ as +"*,*")
        as_list = as_results.split('\n')  
   
        for as_mbean in as_list:    
            node = as_mbean.split('node=')[1].split(',')[0]
            print "Pausing " + node + " " + as
            AdminControl.invoke(as_mbean, 'pause')
            if AdminControl.invoke(as_mbean, 'getStatus') == "2":
                print node + " " + as + " has been paused(stopped)."
            else:
                print "FAILURE: " + node + " " + as + " is still running."


if len(sys.argv) > 0 and sys.executable is None:
    stop_as(sys.argv)
else:
    print """
    This script will pause one or more activation specifications

    Usage:
    
       wsadmin.sh -lang jython -f stop_activation_specs.py <act spec>
       
    Where <act spec> is the jndi name of one or more activation specs
    
    Note: This script should only be used with wsadmin, not python.
    """
