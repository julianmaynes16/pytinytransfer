import pytinytransfer
import numpy as np

print("Fletcher16 test...")
print(pytinytransfer.fletcher16(b"dskdfsndfs"))

print("UpdateParser test...")
ttuparser = pytinytransfer.TinyTransferUpdateParser()
print(ttuparser.processByte(27))

print("RPCParser test...")
ttrparser = pytinytransfer.TinyTransferRPCParser()
print(ttrparser.processByte(27))

print("RPCPacket test...")
ttrpacket_default = pytinytransfer.TinyTransferRPCPacket()
print(ttrpacket_default.isValid())

ttrpacket = pytinytransfer.TinyTransferRPCPacket(b"zx,.zx,.zx,.zx,.z")
print(ttrpacket.isValid())

print("UpdatePacket test...")
ttupacket_default = pytinytransfer.TinyTransferUpdatePacket()
print(ttupacket_default.serialize())

ttupacket = pytinytransfer.TinyTransferUpdatePacket(b"dskjdfskjl", 27,"logggogog", False, True)









