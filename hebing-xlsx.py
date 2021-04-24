import pandas as pd
import os

rootpath = os.getcwd()
print(rootpath)
excel_dir = rootpath + '\\excel'  # 项目文件下面创建excel文件夹存放xlsx文件
print(excel_dir)  # 添加设置excel文件的路径
os.chdir(excel_dir)  # 修改excel文件路径
print(os.getcwd())  # 获取修改后的路径
li = []
print(os.listdir(excel_dir))
# 输出所有excel文件
for i in os.listdir(excel_dir):
    print(i) #逐一打印文件夹每个xlsx文件
    li.append(pd.read_excel(i)) #逐一合并到test.xlsx文件中
    # print(pd.read_excel(i))
    print('已合并' + i)
writer = pd.ExcelWriter('test.xlsx')
pd.concat(li).to_excel(writer, 'Sheet1', index=False)
writer.save() #保存
print('合并完成')
