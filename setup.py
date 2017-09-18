
from setuptools import setup

description="Planet interview take home coding exercise: FIFO Queue Implementation",

setup(
    name="planet-queue",
    author="David Stolfo",
    author_email="david.stolfo@gmail.com",
    url="",
    description=description,
    test_suite='nose.collector',
    tests_require=['nose'],
    py_modules=["planet_queue"]
)
