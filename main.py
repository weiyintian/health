from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

vpn_username = "weiyt2317"
vpn_password = "qq3420550"

class check_in(object):
    driver_path = r'/usr/bin/chromedriver.exe' #写chromedriver的路径
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        prefs = {'profile.managed_default_content_settings.images': 2}
        option.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=check_in.driver_path,chrome_options=option)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.url = 'https://ehall.jlu.edu.cn/'
        self.url_apply= 'https://ehall.jlu.edu.cn/infoplus/form/BKSMRDK/start'

    def run(self):           #模拟登陆vpn平台
        try:
            self.driver.get(self.url)
            self.driver.find_element_by_name("username").send_keys(vpn_username)
            self.driver.find_element_by_name("password").send_keys(vpn_password)
            self.driver.find_element_by_name("login_submit").click()
        except:
            print("加载页面太慢，停止加载，继续下一步操作")
            self.driver.execute_script("window.stop()")

    def tianxie(self):
        self.driver.execute_script("window.open('%s')" % self.url_apply)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        select_xiaoqu = Select(self.driver.find_element_by_name("fieldSQxq"))
        select_xiaoqu.select_by_value("6")
        select_gongyu = Select(self.driver.find_element_by_name('fieldSQgyl'))
        select_gongyu.select_by_value("60")
        try:
            self.driver.find_element_by_name('fieldSQqsh').clear()
        except:
            print('寝室号似乎本来就是空的！！')
        self.driver.find_element_by_name('fieldSQqsh').send_keys('318')
        try:
            self.driver.find_element_by_id('V2_CTRL28').click()
            self.driver.find_element_by_id('V2_CTRL19').click()
            self.driver.find_element_by_id('V2_CTRL23').click()
        except:
            print("莫得感情，现在还签到不了")
        self.driver.find_element_by_class_name('command_button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='dialog_button default fr']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='dialog_button default fr']").click()
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    auto_checkin = check_in()
    print("正在登陆填写平台...")
    auto_checkin.run()
    print("登陆成功...\n正在跳转填页面...")
    auto_checkin.tianxie()
    print("填报完成了！！！")
