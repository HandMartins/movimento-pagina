from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import time
from selenium.webdriver.support.select import Select           #Interagindo com dropdown
import os
from datetime import datetime


class CursoAutomacao:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path=r'C:\Windows\chromedriver.exe',options=chrome_options)
        
        
    def Iniciar(self):    
        # self.driver.get("https://cursoautomacao.netlify.com")
        # #Movimentação Vertical
        # self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  #Indo até o final da página
        # sleep(2)
        # self.driver.execute_script('window.scrollTo(0, document.body.scrollTop);') #Indo até o inicio da página
  
        #Movimentação Horizontal
        self.driver.get("https://josephmark.ventures")
        self.driver.execute_script('window.scrollBy(5000,0)')  # Indo até a direita da página
        sleep(2)
        self.driver.execute_script('window.scrollBy(-5000,0)')  # Indo até a esquerda da página

        #Subindo e descendo por pixel
        self.driver.get("https://coolors.co")
        self.driver.execute_script('window.scrollBy(0,1000)')  # Navegando até 1000 px inferior
        sleep(2)
        self.driver.execute_script('window.scrollBy(0,-1000)') # Navegando até 1000 px superior


        
curso = CursoAutomacao()
curso.Iniciar()