import xlrd
import sys,os

#xls转xml
#for android tranlations



def run():
    try:
        workbook = xlrd.open_workbook("D:\\strings.xls")
    except:
        print("在D:\\下没有strings.xls文件")
    sheet = workbook.sheet_by_name("Android")
    dat1 = []
    strend = "</string>"
    for x in range(sheet.ncols):#列数
        if x == 0:#str name 列
            cell = sheet.col_values(x)
            for y in range(sheet.nrows):#行数
                danyuange = cell[y]
                strname = "<string name=" + "\"" + danyuange + "\"" + ">"
                print(strname)
                dat1.append(strname)
        else:
            cells = sheet.col_values(x)#content列
            filename = cells[0]
            with open("D:\\translations\\" + filename + "_string_smk.xml","a+",encoding="utf8") as f:
                f.write('<?xml version="1.0"  encoding="utf-8"?>\n<resources>\n')

                for contentrow in range(1,sheet.nrows):
                    danyuange_trans = str(cells[contentrow])
                    if danyuange_trans == None:
                        res = dat1[contentrow] + strend + "\n"
                        f.write(res)
                    else:
                        res = dat1[contentrow] + danyuange_trans + strend + "\n"
                        f.write(res)
                f.write("</resources>")
                f.close()
    # if x>0:
    #     cels = sheet.row_values(x)
    #     strname = cels[0]
    #     strname = "<string name=" + "\"" + strname + "\"" + ">"
    #     for contentnum in range(1,13):
    #         with open()
    #
# print(dat1)


def mkdirpath(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except:
        print("创建文件夹失败")
if __name__ == '__main__':
    mkdirpath("D:\\translations")
    run()


