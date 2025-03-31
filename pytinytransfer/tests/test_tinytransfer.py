import pytinytransfer as m
import random


    


def test_main():
    input_buffer = random.randbytes(0x812)
    packet = m.TinyTransferUpdatePacket(input_buffer, 1,"", False, True)
#     size = packet.serialize()
#     parser = m.TinyTransferUpdateParser()
#     for i in range(len(size)):
#          parser.processByte(input_buffer[i])

#     assert parser.packIntReady
#     assert parser.getIntPacket().diff(input_buffer) == False
