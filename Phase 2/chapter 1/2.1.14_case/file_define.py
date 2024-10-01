"""
file relevant
"""
from data_define import Record
import json

# abstract class
# no __init__: 
# 1. mainly used to define many interface
# 2. subclass responsible for object instantiation 
class FileReader:
    
    def read_data(self) -> list[Record]:
        """读取文件的数据 读到的每一条数据都转换为Record对象 将它们都封装到list内返回"""
        pass
    

class Text_FileReader(FileReader):
    
    def __init__(self, path):
        self.path = path
        
    # override 
    def read_data(self) -> list[Record]:
        f = None
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        
        for line in f.readlines():
            # print(line)
            # temporary variable using
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3]) # 先把一条完整数据集成到一个record里
            record_list.append(record)    
            
        f.close()
        return record_list
    
class Jason_FileReader(FileReader):
    
    def __init__(self, path):
        self.path = path
        
    # override 
    def read_data(self) -> list[Record]:
        f = None
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        
        for line in f.readlines():
            # temporary variable using
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)    
            
        f.close()
        return record_list


# for test
if __name__ == "__main__":
    read_text = Text_FileReader("...path")
    text_list = read_text.read_data()
    
    read_json = Jason_FileReader(".....path")
    json_list = read_json.read_data()