from datetime import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime


XPARH_DESDE = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[1]/fieldset/div/div[1]/div/label/div/input[1]"
XPARH_HACIA = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[1]/fieldset/div/div[3]/div[2]/label/div/input[1]"
XPARH_BTN_SOLO_IDA = "//*[@id='tab-navigation-1']/li[2]/a"
XPARH_FECHA_IDA = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[2]/fieldset/div/div/div[1]/label/div/input[1]"
XPARH_BTN_ADD_PASAJERO = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[3]/fieldset/div/div[1]/div[1]/label/div/span/i"
XPARH_BTN_ADD_PASAJERO_ADULTO = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[3]/fieldset/div/div[1]/div[2]/div[2]/div[2]/div[3]"
XPARH_BTN_ADD_PASAJERO_NINOS = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[3]/fieldset/div/div[1]/div[2]/div[3]/div[2]/div[3]"
XPARH_BTN_ADD_PASAJERO_BEBES = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[3]/fieldset/div/div[1]/div[2]/div[4]/div[2]/div[3]"
XPARH_BTN_BUSCAR_VUELOS = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[3]/fieldset/div/div[4]/button"
XPARH_CALENDARIO = "/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/section/div[3]/div[3]/div[2]/div/form/div/div[2]/div/div/div[2]/fieldset/div/div/div[3]/div[1]/table/tbody/tr/td[1]/div[3]/table/tbody/tr[3]"


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.avianca.com/co/es/")
driver.maximize_window()
time.sleep(5)

elementBtnReserva = driver.find_element_by_id('reservatuvuelo') 
elementBtnReserva.click()
time.sleep(3)

elementBtnSoloIda = driver.find_element_by_xpath(XPARH_BTN_SOLO_IDA)
elementBtnSoloIda.click()

elementDesde = driver.find_element_by_xpath(XPARH_DESDE)
elementDesde.clear()
time.sleep(2)
elementDesde.send_keys("Medell")
time.sleep(3)
elementDesde = driver.find_element_by_xpath("//*[@data-terminal='MDE']")
time.sleep(1)
elementDesde.click()


elementHacia = driver.find_element_by_xpath(XPARH_HACIA)
elementHacia.clear()
time.sleep(2)
elementHacia.send_keys("Bogot")
time.sleep(3)
elementHacia = driver.find_element_by_xpath("//*[@data-terminal='BOG']")
time.sleep(2)
elementHacia.click()
time.sleep(5)

elementDate = driver.find_element_by_xpath(XPARH_FECHA_IDA)
elementDate.click()
time.sleep(2)
date = datetime.today().strftime('%Y-%m-%d')
elementDate = driver.find_element_by_xpath(XPARH_CALENDARIO + "//*[@data-date='"+date+"']/div")
elementDate.click()
time.sleep(2)

btnAddpasajero = driver.find_element_by_xpath(XPARH_BTN_ADD_PASAJERO)
btnAddpasajero.click()
time.sleep(1)
btnAddpasajero = driver.find_element_by_xpath(XPARH_BTN_ADD_PASAJERO_ADULTO)
btnAddpasajero.click()
time.sleep(1)
btnAddpasajero = driver.find_element_by_xpath(XPARH_BTN_ADD_PASAJERO_NINOS)
btnAddpasajero.click()
time.sleep(1)
btnAddpasajero = driver.find_element_by_xpath(XPARH_BTN_ADD_PASAJERO_BEBES)
btnAddpasajero.click()
time.sleep(1)

btnAddpasajero = driver.find_element_by_xpath(XPARH_BTN_BUSCAR_VUELOS)
btnAddpasajero.click()
time.sleep(10)

element = driver.find_element_by_xpath("/html/body/app-root/main/div/avail-page/div/avail-cont/avail-pres/div[1]/air-calendar-cont/air-calendar-pres/expander-elem/div[2]/div/div/button[1]")

statusTest = "el boton no esta con error"
className = element.get_attribute("class")
if className == "day selected ng-star-inserted":
    statusTest = "Test Ok"

print(statusTest)
driver.close()
