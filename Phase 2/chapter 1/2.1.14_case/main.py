"""
1. 设计一个类 可以完成数据的封装
2. 设计一个抽象类 声明文件读取的相关功能 并使用子类定义实现具体功能
3. 读取文件 产生数据对象
4. 进行数据需求的逻辑计算
5. 通过PyEcharts进行图像绘制
"""

from file_define import FileReader, Text_FileReader, Jason_FileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

read_text = Text_FileReader("...path")
text_list: list[Record] = read_text.read_data()
    
read_json = Jason_FileReader(".....path")
json_list: list[Record] = read_json.read_data()

all_data: list[Record] = text_list + json_list

# calculation
# {"2011-01-01": 1498, "2011-01-02": 4893}
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了 累加销售额即可
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money   # first record of this date
        
# Visual chart development
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("Sales", list(data_dict.values()), label_opts = LabelOpts(is_show = False))
bar.set_global_opts(
    title_opts = TitleOpts(title="Daily sales")
)

bar.render("Daily Sales Bar Chart.html")