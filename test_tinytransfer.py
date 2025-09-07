import pytinytransfer as m
import random

def test_main():
    TTUpdatePacketTest()
    TTRPCPacketTest()
    MaxValueTest()

def isValid(packet):
    assert packet.isValid()
        
def TTUpdatePacketTest():
    for i in range(2):
        for j in range(2):
            #Data is tested with 0x200 size because of compression entropy

            #No log test
            TTUpdateParse(random.randbytes(0x200), "", i, j) 
            #log test
            TTUpdateParse(random.randbytes(0x200),  random.randbytes(0x400),i, j)
            #no payload CURRENTLY AN EDGE CASE WITHIN ACTUAL NEWHAMSTER WHERE LOG BUT NO PAYLOAD
            # print("No payload")
            # TTUpdateParse(b"", random.randbytes(0x400),i, j)
            #No log or payload
            TTUpdateParse(b"", "",i, j)

def TTRPCPacketTest():
    #ping
    TTRPCParse(b"NMEI\xdb\xb8\x85C\x00\x00\x00\x00\x00\x00\x87\xb2")         
    #halt
    TTRPCParse(b"NMEI\x01\xf9\x88C\x01\x00\x00\x00\x00\x00\xf1\x8f")
    #step
    TTRPCParse(b"NMEI\xa2\xac\x8aC\x02\x00\x00\x00\x00\x00I>")
    #set state armed
    TTRPCParse(b"NMEI\xfaw\x8bC\x04\x00\x01\x00\x01\x01r\xed\x01")
    #set cache to "lmao"
    TTRPCParse(b'NMEI\xa6"\x8cC\x05\x00\x00\x00\x00\x00\xc7\xa9')
    #spi write "ruby"
    TTRPCParse(b"NMEI\xd6\x19\x8dC\x06\x00\x00\x00\x00\x00\xf0H")
    #Wipe flashlog (CURRENTLY BUGGED)

    #flight mode
    TTRPCParse(b"NMEI\x01\x9d\x8fC\x08\x00\x00\x00\x00\x00\xa3\xb2")

def TTUpdateParse(input_buffer, log, isCompressed, isIntegrator):
    packet = m.TinyTransferUpdatePacket(input_buffer, 1,log, isCompressed, isIntegrator)

    #Asserts that a valid packet was created
    isValid(packet)

    #turn packet into sendable byte string
    payload = packet.serialize()

    parser = m.TinyTransferUpdateParser()

    #copy byte to new packet
    completed_packet = None
    for b in payload:
        completed_packet = parser.processByte(b)

        if(completed_packet):
            break

    assert payload == completed_packet.serialize(), "IntegratorPacket: Failed to serialize"

def TTRPCParse(input_buffer):
    packet = m.TinyTransferRPCPacket(input_buffer)
    isValid(packet)
   
    parser = m.TinyTransferRPCParser()

    completed_packet = None
    for b in input_buffer:
        completed_packet = parser.processByte(b)

        if(completed_packet):
            break
        
    assert completed_packet

def MaxValueTest():
    MaxPayload()
    MaxLog()
    MaxArg()

def MaxPayload():
    try:
        max_payload_packet = m.TinyTransferUpdatePacket(random.randbytes(0x401), 1 ,"", 0, 0)
        assert False
    except ValueError:
        assert True

def MaxLog():
    try:
        max_log_packet = m.TinyTransferUpdatePacket(b"", 1 ,random.randbytes(0x401), 0, 0)
        assert False
    except ValueError:
        assert True 
def MaxArg():
    try:
        max_arg_packet = m.TinyTransferRPCPacket(random.randbytes(0x401))
        assert False
    except ValueError:
        assert True


if __name__ == "__main__":
    test_main()
    print("Success!!")
