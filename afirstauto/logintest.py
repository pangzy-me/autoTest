'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import xlrd

def open_excel(file='login.xlsx'):
    try:
        data = xlrd.open_workbook(file)  # 打开Excel文件读取数据
        return data
    except Exception as e:
        print
        str(e)

    # 根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引

def excel_table_byindex(file='login.xlsx', colnameindex=0, by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]  # 通过索引顺序获取获取一个工作表
    nrows = table.nrows  # 获取行数
    colnames = table.row_values(colnameindex)  # 获取某一行数据
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
                list.append(app)
    return list

def Login():
    listdata = excel_table_byindex("E:\\Python_Test\\autoTest\\login.xlsx",0)
    if (len(listdata) <= 0):
        assert 0, u"Excel数据异常"

    for i in range(1, len(listdata)):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
#        assert u"百度一下，你就知道" in driver.title
        # 点击登录按钮
        driver.find_element_by_name("tj_login").click()
        driver.find_element_by_name("tj_login").submit()
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        url = driver.current_window_handle
        driver.switch_to.window(url)
        time.sleep(3)
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(listdata[i]['passname'])
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(listdata[i]['password'])
        driver.find_element_by_name("memberPass").click()
        time.sleep(15)
        driver.find_element_by_id("TANGRAM__PSP_8__submit").click()

        time.sleep(5)
        try:
            elem = driver.find_element_by_id("kw")
        except NoSuchElementException:
            assert 0, u"登录失败，找不到右上角头像"
        driver.close()

if __name__ == '__main__':
    Login()

'''