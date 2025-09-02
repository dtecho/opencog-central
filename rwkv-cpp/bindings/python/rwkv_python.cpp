
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "rwkv_wrapper.h"

namespace py = pybind11;

PYBIND11_MODULE(rwkv_cpp, m) {
    m.doc() = "RWKV.cpp Python bindings";
    
    py::class_<rwkv_cpp::RWKVModel>(m, "RWKVModel")
        .def(py::init<const std::string&, uint32_t, uint32_t>(),
             py::arg("model_path"), py::arg("threads") = 4, py::arg("gpu_layers") = 0)
        .def("eval", &rwkv_cpp::RWKVModel::eval)
        .def("get_vocab_size", &rwkv_cpp::RWKVModel::get_vocab_size)
        .def("get_embed_size", &rwkv_cpp::RWKVModel::get_embed_size)
        .def("get_layer_count", &rwkv_cpp::RWKVModel::get_layer_count)
        .def("get_state_size", &rwkv_cpp::RWKVModel::get_state_size)
        .def("get_logits_size", &rwkv_cpp::RWKVModel::get_logits_size)
        .def("is_loaded", &rwkv_cpp::RWKVModel::is_loaded)
        .def_static("get_system_info", &rwkv_cpp::RWKVModel::get_system_info);
    
    py::class_<rwkv_cpp::TextGenerator>(m, "TextGenerator")
        .def(py::init<std::shared_ptr<rwkv_cpp::RWKVModel>>())
        .def("generate", &rwkv_cpp::TextGenerator::generate,
             py::arg("prompt"), py::arg("max_tokens") = 100, 
             py::arg("temperature") = 0.8f, py::arg("top_p") = 0.9f);
}
