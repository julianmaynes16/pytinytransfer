import pytinytransfer as m
import random

def isValid(packet):
    assert packet.isValid()

def TTUpdateParse(log,isCompressed, isIntegrator):
    input_buffer = random.randbytes(0x20)
    packet = m.TinyTransferUpdatePacket(input_buffer, 1,log, isCompressed, isIntegrator)
    print("Packet size: ", packet.payloadSize)
    
    isValid(packet)

    payload = packet.serialize()
    print(payload)
    parser = m.TinyTransferUpdateParser()

    completed_packet = None
    for b in payload:
        completed_packet = parser.processByte(b)
        
        
    assert payload == completed_packet.serialize(), "IntegratorPacket: Failed to serialize"

def test_main():
    for i in range(2):
        for j in range(2):
            #No log test
            TTUpdateParse("",i,j)
            print(i, j)
            #log test
            #TTUpdateParse(random.randbytes(0x4), i, j)

    
        
    


if __name__ == "__main__":
    test_main()
