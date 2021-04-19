from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import random

qty = int(input("Quantidade de testes: "))

driver = webdriver.Chrome()
driver.get('https://forms.gle/Ct1st5o4vfD6PfZPA')

def bot():
  for i in range(qty):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    question1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    words = ["Elefante", "Macarrão", "Batata", "Palhaço", "Gatinho", "Vinho", "42"]

    answerList = [
      "Acho que a resposta correta é {var}!".format(var = random.choice(words)), 
      "Acredito que {var} é a resposta!".format(var = random.choice(words)), 
      "{var}, é {var}!".format(var = random.choice(words)),
      "{var}, apenas!".format(var = random.choice(words))
    ]

    question1.send_keys(random.choice(answerList))

    question2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question2.send_keys(random.choice(answerList))

    question3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    question3.send_keys(random.choice(answerList))

    op1 = driver.find_element_by_xpath('//*[@id="i17"]/div[3]/div')
    op2 = driver.find_element_by_xpath('//*[@id="i20"]/div[3]/div')
    op3 = driver.find_element_by_xpath('//*[@id="i23"]/div[3]/div')
    op4 = driver.find_element_by_xpath('//*[@id="i26"]/div[3]/div')
    op5 = driver.find_element_by_xpath('//*[@id="i29"]/div[3]/div')

    question4 = [op1, op2, op3, op4, op5]
    opAnswer = random.choice(question4)
    opAnswer.click()

    if (opAnswer == op5):
      answerOp5 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]/div/span/div/div/div[1]/input')
      answerOp5.click()
      answerOp5.send_keys(random.choice(answerList))

    question5 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    question5.click()
    question5.send_keys(Keys.ARROW_LEFT)
    question5.send_keys(Keys.ARROW_LEFT)

    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1940, 2021)

    question5.send_keys(f"{day:02d}", f"{month:02d}", year)

    el1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    el2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
    question6 = [el1, el2]

    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)

    question6[0].click()
    question6[0].send_keys(f"{hours:02d}")
    question6[1].click()
    question6[1].send_keys(f"{minutes:02d}")

    sendButton = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

    sendButton.click()
    print("Número de formulários enviados: ", i + 1)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')))

    answerAgain = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
    answerAgain.click()

bot()
