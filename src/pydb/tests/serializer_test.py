from pydb.storage.serializer import Serializer, Deserializer
import pytest

test_values = [-20, 5, 0, 10, 10000, -23000]

def func(x):
    
    serializer = Serializer()
    test_output = [serializer.int_serialize(i) for i in test_values]
    
    return test_output
