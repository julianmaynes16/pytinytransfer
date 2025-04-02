import pytinytransfer as m
import random


def test_main():
    input_buffer = random.randbytes(0x402)
    packet = m.TinyTransferUpdatePacket(input_buffer, 1,"", True, True)
    #packet = m.TinyTransferUpdatePacket()
