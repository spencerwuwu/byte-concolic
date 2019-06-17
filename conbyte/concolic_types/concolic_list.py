from ..utils import *
from .concolic_type import *
from .concolic_int import *

log = logging.getLogger("ct.con.list")

class ConcolicList(ConcolicType):
    def __init__(self, value=None):
        self.expr = "LIST"
        if value is None:
            self.value = []
            self.size = 0
            log.debug("  List: empty")
            return
        elif isinstance(value, ConcolicList):
            self.value = value.value
            self.size = value.size
        else:
            self.value = value
            self.size = len(value)
        log.debug("  List: %s" % ",".join(val.__str__() for val in self.value))


    def append(self, element):
        self.value.append(element)
        self.size += 1
        log.debug("  List append: %s" % element)

    def get_index(self, index=0):
        return self.value[index]

    def get_slice(self, start=None, stop=None):
        if isinstance(start, ConcolicInteger):
            start = start.value
        if isinstance(stop, ConcolicInteger):
            stop = stop.value
        return ConcolicList(self.value[start:stop])

    def get_iter(self):
        queue = Queue()
        for element in self.value:
            queue.push(element)
        return queue

    def contains(self, other):
        return ConcolicType('nil', other.value in self.value)

    def __str__(self):
        if self.size == 0:
            return "  List: nil"
        return "  List: %s" % ",".join(val.__str__() for val in self.value)
        
    def __add__(self, other):
        self.value += other.value
        self.size += other .size
        log.debug(self)
        return self

    def __radd__(self, other):
        self.value += other.value
        self.size += other .size
        return self

    def __len__(self):
        return self.size

    def len(self):
        return self.size
    
    def multiply(self, mul):
        if isinstance(mul, ConcolicInteger):
            mul = mul.value
        array = []
        for i in range(mul):
            for value in self.value:
                array.append(value)

        return ConcolicList(array)

    def store(self, index, value):
        if isinstance(index, ConcolicInteger):
            index = index.value

        self.value[index] = value
