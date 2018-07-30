from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0"
)

options = webdriver.ChromeOptions()
# options.set_headless()
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()

try:
    driver.get("https://www.kaishiba.com/project/more")
    driver.find_element_by_xpath('//*[@id="userLogout"]/a[1]').click()
    driver.find_element_by_name("phone").send_keys("18771696825")
    driver.find_element_by_name("password").send_keys("kaishiba.123")
    driver.find_element_by_class_name("ksui-btn-green").click()

    for i in range(1950//6+1):
        time.sleep(3)
        # driver.execute_script("window.scrollBy(0,2000)")
        js = "window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)

    datas = driver.find_elements_by_class_name("title")
    for data in datas:
        print(data.text)
        # driver.find_element_by_class_name("title").click()
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        # print(driver.page_source)
        # time.sleep(2)
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        # driver.close()

finally:
    driver.quit()

