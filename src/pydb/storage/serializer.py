# TODO
# I need to think about providing table schema to serializers

class Serializer:
    
    def __init__(self):
        pass
    
    def serialize(self, row, format: list[str]):
        
        if len(row) != len(format): raise ValueError("Length of row doesnt match the length of schema format.")
        output = bytes()
        for x, z in zip(row, format):
            if z == "INT":
                output += self.int_serialize(x)
            elif z == "TEXT":
                output += self.string_serialize(x)
            else:
                raise TypeError("Unsupported type for serialization.")
        return output    
        
    def int_serialize(self, integer: int, signed=True): # int = 4 bytes signed little-endian
        
        return integer.to_bytes(4, byteorder='little', signed=signed)

    def string_serialize(self, string: str): 
        
        string_to_utf = string.encode("utf-8")
        prefix = self.int_serialize(len(string_to_utf), signed=False)
        
        return prefix + string_to_utf
        
class Deserializer:
    
    def __init__(self):
        pass
    
    def deserialize(self, row: bytes, format: list[str]):
        
        output = []
        i = 0
        for x in format:
            if x == "INT":
                data = row[i:i+4]
                a = self.int_deserialize(data)
                i += 4
                output.append(a)
            elif x == "TEXT":
                length = self.int_deserialize(row[i:i+4], signed=False)
                i += 4
                if len(row[i:i+length]) < length:
                    raise ValueError("prefix doesn't match the real length of a string.")
                data = row[i:i+length]
                a = self.str_deserialize(data)
                i += length
                output.append(a)
            else:
                raise TypeError("Unsupported type for deserialization.")
            
        if i != len(row):
            raise ValueError("Wrong schema, wrong record boundary, or corrupted data.")      
         
        return output    
    
    def int_deserialize(self, data: bytes, signed=True):
        
        if len(data) != 4: raise ValueError("Bytes not of length 4.")
        return int.from_bytes(data, byteorder="little", signed=signed)
    
    def str_deserialize(self, data: bytes):
        
        string = data.decode("utf-8")
        return string


