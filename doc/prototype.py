# the basic idea for the syntax this allows

"""
NOTE: use struct.Struct to save 30ns (thanks olaf)

# TODO: should this use typing.Protocol? (most likely) X
# abstract class that provides methods for reading (bytes?) from some (byte?) readable thing
class Provider:
    ...

    read_formatted_data("struct format string") -> tuple[Any * n] | Any
    write_formatted_data(...) -> inverse

    open/close?
        . allow context manager
            with Provider(...) as prov:
                object = DataObject(prov)

        . what providers could you not open or close?
            . may not want to close some of them
                just dont use context manager for them i.e. SocketProvider(...)?
        . can open:
            . processes
            . files
            . data streams


# Provider class that allows for reading from objects with a .read method that returns
#  bytes or bytearray?
open("rb").read ->
BytesIO().read ->

    class ByteReadable(Protocol):
        def read(...) -> bytes
        def write(..., bytes) -> number of bytes written?

class DataProvider:
    ...




class User(DataObject):
    # reads a string which is prefixed with a u32 typed size
    name: str = SizedString(Unsigned4)
    id: int = Unsigned8()
    num_children: Unsigned4()
    children: list["User"] = Seq("User", "num_children")


test = 0x5 a b c d e

SizedString(Unsigned1)



"""
