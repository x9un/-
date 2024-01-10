#筛选出某一列中某些值重复的行 并且给他搞个新列标明重复
import pandas as pd

target=pd.read_excel(r'qiyue.xlsx','Sheet1')
data=target.iloc[272:,4]#从274行开始到最后,第五列数据 返回series类型,不知道为什么从272开始的，反正试了是这样
t=data.str.split("t=").str[1]#提取t=的后半部分字符 
repeat=t.duplicated(keep=False)#标记重复项
for i in t[repeat].index: #在重复series的下标值中取值循环
	target.iloc[i,6]="封面重复"
target.to_excel('qi.xlsx')#生成文件
