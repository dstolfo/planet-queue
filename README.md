# PlanetQueue :earth_americas:

PlanetQueue is a Python module which implements a FIFO queue data type class.
This class includes support for thread-safety. PlanetQueue can be both a bounded
and unbounded queue. See implementation for comments.

Thank you for the opportunity to interview. I truly admire Planet and would love
to be a member of your team :)

## Usage

Setup and installation from the shell:
```
> git clone https://github.com/dstolfo/planet-queue.git
> cd planet-queue
# execute the module tests
> python setup.py test
> python setup.py install
```

Python usage:
```
>>>> import planet_queue
>>>> q = planet_queue.PlanetQueue()
>>>> q.put(0)
>>>> q.get()
0
>>>> q.size()
0
>>>> q.empty()
True
>>>> q.full()
False
>>>> bounded_q = planet_queue.PlanetQueue(1)
```
