/* File automatically generated by the macro OPENCOG_CXX_ATOMTYPES. Do not edit */
#include <opencog/atoms/atom_types/atom_types.h>
#include <opencog/atoms/base/Handle.h>
#include <opencog/atoms/base/Node.h>
#include <opencog/atoms/base/Link.h>

namespace opencog {

#define NODE_CTOR(FUN,TYP) inline Handle FUN(std::string name) {\
    return createNode(TYP, std::move(name)); }

#define LINK_CTOR(FUN,TYP) template<typename ...Atoms>\
    inline Handle FUN(Atoms const&... atoms) {\
       return createLink(TYP, atoms...); }

NODE_CTOR(Storage, STORAGE_NODE)
NODE_CTOR(PostgresStorage, POSTGRES_STORAGE_NODE)
NODE_CTOR(FileStorage, FILE_STORAGE_NODE)
NODE_CTOR(MonoStorage, MONO_STORAGE_NODE)
NODE_CTOR(RocksStorage, ROCKS_STORAGE_NODE)
NODE_CTOR(CogSimpleStorage, COG_SIMPLE_STORAGE_NODE)
NODE_CTOR(CogStorage, COG_STORAGE_NODE)
NODE_CTOR(ForeignStorage, FOREIGN_STORAGE_NODE)
NODE_CTOR(BridgeStorage, BRIDGE_STORAGE_NODE)
NODE_CTOR(Proxy, PROXY_NODE)
NODE_CTOR(NullProxy, NULL_PROXY_NODE)
NODE_CTOR(ReadThruProxy, READ_THRU_PROXY_NODE)
NODE_CTOR(SequentialReadProxy, SEQUENTIAL_READ_PROXY_NODE)
NODE_CTOR(WriteThruProxy, WRITE_THRU_PROXY_NODE)
NODE_CTOR(ReadWriteProxy, READ_WRITE_PROXY_NODE)
NODE_CTOR(WriteBufferProxy, WRITE_BUFFER_PROXY_NODE)
NODE_CTOR(CachingProxy, CACHING_PROXY_NODE)
NODE_CTOR(DynamicDataProxy, DYNAMIC_DATA_PROXY_NODE)
LINK_CTOR(ProxyParameters, PROXY_PARAMETERS_LINK)
LINK_CTOR(FetchValueOf, FETCH_VALUE_OF_LINK)
LINK_CTOR(StoreValueOf, STORE_VALUE_OF_LINK)
#undef NODE_CTOR
#undef LINK_CTOR
} // namespace opencog
