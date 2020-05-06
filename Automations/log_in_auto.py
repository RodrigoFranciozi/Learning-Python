from selenium import webdriver

driver = webdriver.Chrome('Caminho do chrome driver')
driver.get("Adicionat URL do Site")

username = driver.find_element_by_id("id do login HTML")
username.clear()
username.send_keys("Seu usuário")

password = driver.find_element_by_name("id da senha HTML")
password.clear()
password.send_keys("Sua senha")

driver.find_element_by_name("nome do botão a ser clicado em HTML").click()

#CTRL + SHIFT + C para abrir o inspecionar