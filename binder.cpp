#define TINY_TRANSFER_UPDATE_MAX_PAYLOAD_LENGTH    1024
#define TINY_TRANSFER_UPDATE_MAX_LOG_LENGTH        1024


#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "tinyTransfer.h"
#include <string>


PYBIND11_MODULE(pytinytransfer, m) {
    pybind11::class_<TinyTransferUpdateParser>(m, "TinyTransferUpdateParser")
        .def(pybind11::init<>())
        .def("processByte", [](TinyTransferUpdateParser& self, uint8_t i_byte) -> pybind11::object {
            return self.processByte(i_byte) ? pybind11::cast(self.completedPacket) : pybind11::object(pybind11::cast(nullptr));
        })
        .def("getState", [](TinyTransferUpdateParser& self) {
            return self.state;
        })
        .def_readwrite("state", &TinyTransferUpdateParser::state)
        .def_readwrite("soh", &TinyTransferUpdateParser::soh)
        .def_readwrite("inputPacket", &TinyTransferUpdateParser::inputPacket)
        .def_readwrite("completedPacket", &TinyTransferUpdateParser::completedPacket)
        .def_readwrite("position", &TinyTransferUpdateParser::position);
        

    pybind11::class_<TinyTransferRPCParser>(m, "TinyTransferRPCParser")
        .def(pybind11::init<>())
        .def("processByte", &TinyTransferRPCParser::processByte);

    pybind11::class_<TinyTransferRPCPacket>(m, "TinyTransferRPCPacket")
        .def(pybind11::init<>())
        .def(pybind11::init([](pybind11::bytes data) {
            pybind11::buffer_info data_buf(pybind11::buffer(data).request());
            const char *data_ptr = reinterpret_cast<const char *>(data_buf.ptr);
            return new TinyTransferRPCPacket((uint8_t*)data_ptr);
        }))
        .def("isValid", &TinyTransferRPCPacket::isValid);

    pybind11::class_<TinyTransferUpdatePacket>(m, "TinyTransferUpdatePacket")
        .def(pybind11::init<>())
        .def(
            pybind11::init<>([](pybind11::bytes data, uint32_t packetId, std::string log, bool compressed, bool isIntegrator){
                
                pybind11::buffer_info data_buf_data(pybind11::buffer(data).request());
                char *data_ptr_data = reinterpret_cast<char *>(data_buf_data.ptr);
                size_t data_length = static_cast<size_t>(data_buf_data.size);

                if(data_length > TINY_TRANSFER_UPDATE_MAX_PAYLOAD_LENGTH){
                    throw pybind11::value_error("Payload too large: can only be a max of 1024 bytes");
                }
                
                pybind11::buffer_info data_buf_log(pybind11::buffer(pybind11::bytes(log)).request());
                char *data_ptr_log = reinterpret_cast<char *>(data_buf_log.ptr);
                size_t log_size = log.size();

                return new TinyTransferUpdatePacket((uint8_t*)data_ptr_data, data_length, packetId, data_ptr_log, log_size, compressed, isIntegrator);
            }),
            pybind11::arg("data"), 
            pybind11::arg("packetId"),
            pybind11::arg("log") = "",
            pybind11::arg("compressed") = true,
            pybind11::arg("isIntegrator") = false
        )
        
        .def("serialize", [](TinyTransferUpdatePacket& self) {
            uint8_t serialize_buf[sizeof(TinyTransferUpdatePacket)];
            uint16_t length = self.serialize(serialize_buf);
            return pybind11::bytes((char*)serialize_buf, length);
        })

        .def("isValid", &TinyTransferUpdatePacket::isValid)
        .def("isCompressed", &TinyTransferUpdatePacket::isCompressed)
        .def("decompressPayload", [](TinyTransferUpdatePacket& self){
            uint8_t decompress_buf[sizeof(TinyTransferUpdatePacket)];
            uint16_t length = self.decompressPayload(decompress_buf);
            return pybind11::bytes((char*)decompress_buf, length);
        })
        .def_readwrite("headerChecksum", &TinyTransferUpdatePacket::headerChecksum)
        // .def_property("payload", [](TinyTransferUpdatePacket& self) -> pybind11::array {
        //     auto dtype = pybind11::dtype(pybind11::format_descriptor<TinyTransferUpdatePacket>::format());
        //     auto base = pybind11::array(dtype, {TINY_TRANSFER_UPDATE_MAX_PAYLOAD_LENGTH}, {sizeof()});
        //     return pybind11::array(dtype, {TINY_TRANSFER_UPDATE_MAX_PAYLOAD_LENGTH}, {sizeof(TinyTransferUpdatePacket)}, self.payload, base);
        //   }, [](TinyTransferUpdatePacket& self) {});
        // .def_readwrite("log", &TinyTransferUpdatePacket::log)
        .def_readwrite("startOfHeader", &TinyTransferUpdatePacket::startOfHeader)
        .def_readwrite("packetId", &TinyTransferUpdatePacket::packetId)
        .def_readwrite("packetFlags", &TinyTransferUpdatePacket::packetFlags)
        .def_readwrite("payloadSize", &TinyTransferUpdatePacket::payloadSize)
        .def_readwrite("payloadChecksum", &TinyTransferUpdatePacket::payloadChecksum)
        .def_readwrite("headerChecksum", &TinyTransferUpdatePacket::headerChecksum)
        .def_readwrite("logSize", &TinyTransferUpdatePacket::logSize);


    m.def("fletcher16", [](pybind11::bytes data) {
        pybind11::buffer_info data_buf(pybind11::buffer(data).request());
        const char *data_ptr = reinterpret_cast<const char *>(data_buf.ptr);
        size_t length = static_cast<size_t>(data_buf.size);
        return fletcher16((uint8_t*)data_ptr, length);
    });


    m.attr("__version__") = "dev";
}
