import pytinytransfer as m
import random

def isValid(packet):
    assert packet.isValid()

def TTUpdateParse(isCompressed, isIntegrator):
    input_buffer = random.randbytes(0x4)
    packet = m.TinyTransferUpdatePacket(input_buffer, 1,"ABC", isCompressed, isIntegrator)
    isValid(packet)

    payload = packet.serialize()
    #print(payload)
    parser = m.TinyTransferUpdateParser()

    completed_packet = None
    for b in payload:
        completed_packet = parser.processByte(b)
        print(parser.state)
    assert payload == completed_packet.serialize(), "IntegratorPacket: Failed to serialize"

def test_main():
    for i in range(2):
        for j in range(2):
            TTUpdateParse(i,j)
        
    


if __name__ == "__main__":
    test_main()
