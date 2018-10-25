#import zc.zk
from kazoo.client import KazooClient
import logging
import time
servicePath="/usNaukri/java"
try:
        zk1 = KazooClient(hosts='149.165.170.124:2182')
        zk1.start()
except:
        print("zookeeper not running")

logging.basicConfig()

if zk1.exists(servicePath):
	print("Node exists")
	pass
else:
	zk1.ensure_path(servicePath)

#give a 2 sec delay
time.sleep(2)

zk1.set(servicePath, b"149.165.170.240:9090")
children = zk1.get_children("/usNaukri")
print("children of root node usNaukri are ",children)
print("Java registration Successfull")	
                                                    
