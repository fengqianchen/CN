from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
																			
# Topology to be instantiated in Mininet
class MNTopo(Topo):
    "Mininet test topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        # Host and link configuration
        hostConfig = {'cpu': cpu}
        linkConfig = {'bw': 50, 'delay': '10ms', 'loss': 0,
                   'max_queue_size': max_queue_size } #Ivy editted the 'bw' from 10 and 'delay' from '1ms'

        # Hosts and switches
        s1 = self.addSwitch('s1')
	# Ivy's Edit
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')
	# Ivy'S Edit Ended
        sender = self.addHost('sender', **hostConfig)
        receiver = self.addHost('receiver', **hostConfig)

        # Wire receiver
        self.addLink(receiver, s1, port1=0, port2=1, **linkConfig)

	# Ivy's Edit
	# Wire between Switches
	self.addLink(s1, s2, port1=2, port2=1, **linkConfig)
	self.addLink(s2, s3, port1=2, port2=1, **linkConfig)

        # Wire sender
        self.addLink(sender, s3, port1=0, port2=2, **linkConfig) #Ivy changed s1 to s3
	
