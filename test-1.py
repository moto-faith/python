import xlrd
import xlwt
data = xlrd.open_workbook('test.xlsx')
table = data.sheets()[0]
for i in range(table.nrows):
    print(table.row_values(i))
for k in range(table.ncols):
    print(table.col_values(k))
print(table.cell(1,1).value)
for j in range(1,table.nrows):
    print(table.row_values(j))
    print("----------------")
 workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('个人信息')
title = ['编号','姓名','性别','年龄']
data = [['张一','男','18'],['李二','女','20'],['黄三','男','38'],['刘四','男','88']]
for m in range(len(title)):
    worksheet.write(0,m,title[m])
    data[m].insert(0,m+1)
    for n in range(len(data[m])):
        worksheet.write(m+1,n,data[m][n])
workbook.save('test0.xls') 