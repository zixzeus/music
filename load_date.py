import pandas as pd
from sqlalchemy import create_engine
import os,sys
import xlrd
# 读取Excel文件s
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
print(BASE_DIR)

folder_path = "./data/"

# 获取文件夹下所有文件和文件夹的名字
files_list = os.listdir(folder_path)
engine = create_engine('mysql+mysqlconnector://root:!1995127Zx@localhost/music_db')
# 打印所有文件名

def remove_suffix(s, suffix):
    return s.replace(suffix, '')

df = pd.read_excel(f"./data/index_song.xlsx",engine="openpyxl")
df.to_sql("index_song", con=engine, if_exists='replace', index=False)

for file in files_list:
    if file.endswith('.xlsx'):
        df = pd.read_excel(f"./data/{file}", engine='openpyxl')
        table = remove_suffix(file, '.xlsx')

        df.to_sql(table, con=engine, if_exists='replace', index=False)
# df = pd.read_excel('/data/index_comment.xls')

# 创建MySQL引擎


# # 将数据导入MySQL
# df.to_sql('your_table', con=engine, if_exists='replace', index=False)
