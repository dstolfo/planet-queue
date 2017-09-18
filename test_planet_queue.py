from unittest import TestCase

import planet_queue


class TestPlanetQueue(TestCase):
    """Tests for PlanetQueue"""

    def test_put_PlanetQueue(self):
        # test that FIFO order is preserved for put.
        q = planet_queue.PlanetQueue()
        items = ['item1', 'item2']
        for item in items:
            q.put(item)
        # Given this is a FIFO queue, we expect q.queue
        # and items to have the same order. In Python, lists are
        # equal if that have the same element at the same index,
        # therefore this assertion should be true.
        self.assertEquals(q.queue, items)

        # test that maxsize is enforced for put.
        q = planet_queue.PlanetQueue(1)
        with self.assertRaises(Exception):
            for item in items:
                q.put(item)

    def test_get_PlanetQueue(self):
        # test that FIFO order is preserved for get.
        q = planet_queue.PlanetQueue()
        items = ['item1', 'item2']
        q.queue = items[:]
        retrieved = []
        exc = True
        while exc:
            try:
                retrieved.append(q.get())
            except Exception:
                exc = False
        self.assertEquals(retrieved, items)

    def test_size_PlanetQueue(self):
        # test that queue size is correct for an unbounded queue.
        q = planet_queue.PlanetQueue()
        self.assertEquals(q.size(), 0)
        for x in range(5):
            q.put(x)
        self.assertEquals(q.size(), 5)

        # test that queue size correct for a bounded queue.
        q = planet_queue.PlanetQueue(3)
        for x in range(5):
            try:
                q.put(x)
            except Exception:
                pass
        self.assertEquals(q.size(), 3)

    def test_empty_PlanetQueue(self):
        # test correct behavior for empty().
        q = planet_queue.PlanetQueue()
        self.assertTrue(q.empty())
        for x in range(1):
            q.put(x)
        self.assertFalse(q.empty())
        for x in range(2):
            try:
                q.get()
            except Exception:
                pass
        self.assertTrue(q.empty())

    def test_full_PlanetQueue(self):
        # test correct behavior for full() with an unbounded queue.
        q = planet_queue.PlanetQueue()
        self.assertFalse(q.full())
        q.put(0)
        self.assertFalse(q.full())

        # test correct behavior for full() with a bounded queue.
        q = planet_queue.PlanetQueue(2)
        q.put(0)
        self.assertFalse(q.full())
        q.put(1)
        self.assertTrue(q.full())
        q.get()
        self.assertFalse(q.full())

