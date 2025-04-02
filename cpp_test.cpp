#include "tinyTransfer.h"
#include <random>

int main(){
    uint8_t input_buffer[0x800];

    uint8_t payload[0x800];
    for(int i = 0; i < 0x800; i++){
        payload[i] = rand() % 256;
    }
    
    TinyTransferUpdatePacket packet(input_buffer, sizeof(input_buffer), 0, nullptr, 0, true, true);
}