import pytinytransfer as m
import random

def isValid(packet):
    assert packet.isValid()

def TTUpdateParse( input_buffer, log, isCompressed, isIntegrator):
    packet = m.TinyTransferUpdatePacket(input_buffer, 1,log, isCompressed, isIntegrator)
    print("Packet size: ", packet.payloadSize)
    
    isValid(packet)

    payload = packet.serialize()
   
    parser = m.TinyTransferUpdateParser()

    completed_packet = None
    for b in payload:
        print(b)
        completed_packet = parser.processByte(b)
        if(completed_packet):
            break
    
        
        
    assert payload == completed_packet.serialize(), "IntegratorPacket: Failed to serialize"

def test_main():
    for i in range(2):
        for j in range(2):
            #No log test
            TTUpdateParse(random.randbytes(0x20), "", i, j)
            #log test
            TTUpdateParse(random.randbytes(0x20),  random.randbytes(0x20),i, j)
            #no input 
            TTUpdateParse(b"", "ABC",i, j)

    
        
    


if __name__ == "__main__":
    test_main()
