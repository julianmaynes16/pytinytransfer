import pytinytransfer
import numpy as np
import random

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


input_buffer = random.randbytes(0x402)
ttupacket = pytinytransfer.TinyTransferUpdatePacket(input_buffer, 255,"HIJKLMNOP", True, False)

print(hex(pytinytransfer.fletcher16(b"ABCDEFG")))

print(ttupacket.serialize())







