#1.生成xlsx表格，并按考试时间进行排序
from sqlalchemy import create_engine
import pandas as pd
import xlwt
import sys
import io
# 设置标准输出的编码为UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
connStr="mysql+pymysql://root:woshisb@127.0.0.1:3306/python?"
engine=create_engine(connStr)
sql="select 考试名称,年级排名,总分,数学,语文,英语,理综,考试时间 from 李华的高三成绩 order by 考试时间"
grade=pd.read_sql(sql,con=engine)
grade.to_excel("D:/grade.xlsx")
print(grade[['考试名称','年级排名','总分','数学','语文','英语','理综','考试时间']]) 
