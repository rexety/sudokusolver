from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np

newgame = driver.find_element_by_class_name("game-cell")
newgame.click()
newgame = driver.find_element_by_class_name("cell-value")
newgame.send_keys(Keys.NUMPAD2)