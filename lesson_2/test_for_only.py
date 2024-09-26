from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get('https://only.digital/')

driver.implicitly_wait(20)




try:

    #проверяем, что на странице есть футер
    assert driver.find_element(By.TAG_NAME, "footer"), "Footer not found" 

    #проверяем, что номер телефона в ссылке корректный
    assert driver.find_element(By.CSS_SELECTOR, "a[href='tel:+74957409979']"), "Number incorrect"
    
    #выводим в консоль информацию, что на странице есть футер и номер в ссылке корректный
    print("Footer is found on the main page")
    print("Number in link is correct on the main page")

    
  
    #находим ссылку "карьера" и с помощью скрипта проходим по ней
    job = driver.find_element(By.CSS_SELECTOR, "a[href='/job']")
    driver.execute_script("arguments[0].click();", job)

  
    #ищем футер на странице карьера
    assert driver.find_element(By.TAG_NAME, "footer"), "Footer not found"
    #проверяем ссылку на телефон на странице карьера
    assert driver.find_element(By.CSS_SELECTOR, "a[href='tel:+74957409979']"), "Number incorrect"

    #выводим в консоль информацию, что на странице карьера есть футер и номер в ссылке корректный
    print("Footer is found on the job page")
    print("Number in link is correct on the job page")


finally:
    
    #закрываем страницу
    driver.quit()

