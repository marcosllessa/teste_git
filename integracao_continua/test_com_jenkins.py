import pytest


@pytest.fixture()
def setup():
    print("Entre aqui primeiro")


def test_teste1(setup):
    print("Executando teste 1")

def test_uol(setup):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://www.uol.com.br/")

    print(driver.title)
    print(driver.current_url)

    driver.find_element_by_xpath("//*[@id='HU_header']/div[2]/div/div[2]/div[1]/div/div/a").click()

    time.sleep(3)

    driver.close()


