import pytinytransfer as pytinytransfer


def UpdatePacketSubroutine(packet_id):
    m_packet_id = packet_id
    isCompressed = True
    isIntegrator = False
    packet = pytinytransfer.TinyTransferUpdatePacket(b"Data", m_packet_id, "Log Data", isCompressed, isIntegrator)

    print("Packet is valid: " + str(packet.isValid()))

    print("Packet id: " + str(packet.packetId))
    print("Log size: " + str(packet.logSize))
    print("Payload checksum: " + str(packet.payloadChecksum))

    payload = packet.serialize()
    parser = pytinytransfer.TinyTransferUpdateParser()
    completed_packet = None

    for b in payload:
        completed_packet = parser.processByte(b)
        if(completed_packet):
            break

    print("Packet successfully processed: " + str(completed_packet != None))
    print("Packet contents: " + str(completed_packet.serialize()))


def RPCPacketSubroutine(input_data):
    packet = pytinytransfer.TinyTransferRPCPacket(input_data)

    print("Packet is valid: " + str(packet.isValid()))

    print("Packet Nonce: " + str(packet.packetNonce))

    parser = pytinytransfer.TinyTransferRPCParser()
    completed_packet_parse = None

    for b in input_data:
        completed_packet_parse = parser.processByte(b)
        if(completed_packet_parse):
            break

    print("Packet successfully processed: " + str(completed_packet_parse != None))




if __name__ == "__main__":
    UpdatePacketSubroutine(4)
    RPCPacketSubroutine(b"Petscop 2")