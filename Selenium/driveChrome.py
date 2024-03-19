from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:\\caminho\\para\\chrome.exe'  
chrome_driver_path = 'F:\\Downloads\\chromedriver_win32\\chromedriver.exe' 

chrome_options.add_experimental_option("detach", True)

# Passando o caminho do ChromeDriver diretamente nas opções do ChromeOptions
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://web.whatsapp.com/")
time.sleep(10)

while True:
    # Procura por todas as conversas individuais
    conversations = driver.find_elements_by_class_name("_1T6Gw")

    # Verifica cada conversa em busca de mensagens não lidas
    for conversation in conversations:
        # Verifica se há um indicador de mensagem não lida na conversa
        unread_indicator = conversation.find_elements_by_class_name("_31gEB")

        if unread_indicator:
            # Clica na conversa para abrir o chat
            conversation.click()
            time.sleep(2)  # Aguarda 2 segundos para carregar a conversa

            # Encontra a caixa de texto onde podemos digitar a resposta
            chat_box = driver.find_element_by_class_name("_3uMse")

            # Digita uma mensagem qualquer (no caso, um ponto) como resposta
            chat_box.send_keys(".")
            chat_box.send_keys(Keys.RETURN)  # Pressiona Enter para enviar a mensagem

            # Aguarda um curto período de tempo para evitar envio repetido
            time.sleep(1)

    # Aguarda 5 segundos antes de verificar novamente
    time.sleep(5)