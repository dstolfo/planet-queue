
import threading


class PlanetQueue(object):
    """Queue class for Planet interview :)"""

    def __init__(self, maxsize=0):
        # if maxsize <= 0, the queue size is "infinite"
        self.maxsize = maxsize
        self.lock = threading.Lock()
        # The maximum size allowable for an unbounded PlanetQueue would depend
        # on a couple of factors. With an unbounded memory limit, the largest List
        # in Python is PY_SSIZE_T_MAX/sizeof(PyObject*). Or approximately, 5.4x10^8
        # elements on a 32-bit OS. Typically though your application will run inside
        # a container or environment limiting the maximum memory. In either case
        # Python will raise a MemoryError if we cannot append more items to an
        # unbounded queue; this would also be coupled with signficant performance
        # implications.
        self.queue = []

    def put(self, item):
        with self.lock:
            if not self._full():
                self.queue.append(item)
            else:
                raise Exception("PlanetQueue full")

    def get(self):
        with self.lock:
            if not self._empty():
                return self.queue.pop(0)
            else:
                raise Exception("PlanetQueue empty")

    def size(self):
        with self.lock:
            return self._size()

    def _size(self):
        """
        ** Using a private function to have a non-lock context size function
        for internal use is a trade-off between using threading.Condition. If I'm writing
        something that is wildly shared, I'd probably use a lock condition instead.
        """
        return len(self.queue)

    def empty(self):
        with self.lock:
            return len(self.queue) == 0

    def _empty(self):
        return len(self.queue) == 0

    def full(self):
        with self.lock:
            if self.maxsize > 0:
                return self._size() == self.maxsize
            else:
                return False

    def _full(self):
        if self.maxsize > 0:
            return self._size() == self.maxsize
        else:
            return False

