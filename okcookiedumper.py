import pickle
import selenium.webdriver
from selenium.webdriver.common.by import By

driver = selenium.webdriver.Firefox()
driver.get("https://ok.ru/dk?st.cmd=anonymMain&st.fflo=on&st.lgn=on")

driver.find_element(by=By.ID, value='field_email').send_keys('Тут введи логин')
driver.find_element(by=By.ID, value='field_password').send_keys('Тут введи пароль')
driver.find_element(by=By.XPATH, value='/html/body/div[11]/div[5]/div[2]/div[1]/div/div/div/div[2]/div[3]/div[4]/div/div/main/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/form/div[4]/input').click()
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))