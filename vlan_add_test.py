#just a test of a weird behaviour on python 3.9/osx: it adds vlan, but script fails before end with error 
#AttributeError: 'xml.etree.ElementTree.Element' object has no attribute 'getchildren' somewhere in ucs-mdk. 
#and it works without handle.login() - no idea, why :-\
#needs an investigation.

from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

#init handle
handle = UcsHandle("172.28.150.15","ucspe","ucspe",secure=False)

#login
#handle.login()

mo = FabricVlan(parent_mo_or_dn="fabric/lan",sharing="none",name="vlan22",id="22")
handle.add_mo(mo)
handle.commit()

#login
#handle.login()
print("vlan added")
#logout
handle.logout()
