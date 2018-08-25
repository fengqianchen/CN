from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
																			
# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        #TODO: Create your Mininet Topology here!
	
	#Host and link configuration
	hostConfig = {'cpu': cpu}
	linkConfigEthernet = {'bw': 25, 'delay': '2ms', 'loss': 0, 'max_queue_size': max_queue_size}
	linkConfigWifi = {'bw': 10, 'delay': '6ms', 'loss': 3, 'max_queue_size': max_queue_size}
	linkConfig3G = {'bw': 3, 'delay': '10ms', 'loss': 8, 'max_queue_size': max_queue_size}

	# Hosts and switches
	s1 = self.addSwitch('s1')
	s2 = self.addSwitch('s2')
	s3 = self.addSwitch('s3')
	s4 = self.addSwitch('s4')
	h1 = self.addHost('h1', **hostConfig)
	h2 = self.addHost('h2', **hostConfig)
	h3 = self.addHost('h3', **hostConfig)

	#Wire between hosts and switches
	#Port numbers are arbitrary
	self.addLink(h1, s1, port1=0, port2=1, **linkConfigEthernet)
	self.addLink(s1, s2, port1=1, port2=2, **linkConfigEthernet)
	self.addLink(s2, s3, port1=2, port2=3, **linkConfigEthernet)
	self.addLink(s2, s4, port1=2, port2=4, **linkConfigEthernet)
	self.addLink(s3, h2, port1=3, port2=2, **linkConfigWifi)
	self.addLink(s4, h3, port1=4, port2=3, **linkConfig3G)
	
