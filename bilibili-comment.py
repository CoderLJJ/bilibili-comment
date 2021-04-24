import xlrd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
start = time.time()
option = webdriver.ChromeOptions()
# 设置为开发者模式，避免被识别
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument(
    r'--user-data-dir=C:\Users\81316\AppData\Local\Google\Chrome\linjj\Default')  # 加载前面获取的 个人资料路径
driver = webdriver.Chrome(options=option)
driver.maximize_window()
data = xlrd.open_workbook('逻辑教育.xlsx')
table = data.sheets()[0]
links = table.col_values(int(1))
for url in links[1:]:
    values = ['666！膜拜大佬!', '大佬，学习的榜样！', '一起加油！','哈哈哈']
    juzi = random.choice(values)
    print(juzi)
    wait = WebDriverWait(driver, 10, 0.2) #设置等待时间
    driver.get(url)
    try:
        comment = wait.until(
            EC.presence_of_element_located(
                (By.ID, 'comment')),message="不存在评论区域")
        # 滑动滚动条到指定的
        driver.execute_script("return arguments[0].scrollIntoView();", comment)
        textarea = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//textarea[@class="ipt-txt"]')),
                              message="不存在评论框")[0]
        button = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//button[@class="comment-submit"]')),
                            message="不存在提交按钮")[0]
        textarea.send_keys(juzi)
        time.sleep(2)
        button.click()
        time.sleep(5)
    except Exception as e:
        print(e)
driver.quit()
end = time.time()
print("总共耗时：%f" % (end - start))
