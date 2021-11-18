import sys
import base64
import numpy as np
import cv2
import requests
import tensorflow as tf

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

model = tf.keras.models.load_model("./control_model")

valid_characters = "0123456789abcdefghijklmnopqrstuvwxyz"

def predict(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    if img is not None:
        img = img / 255.0
    else:
        print("Not detected");
    res = np.array(model.predict(img[np.newaxis, :, :, np.newaxis]))
    ans = np.reshape(res, (5, 36))
    l_ind = []
    probs = []
    for a in ans:
        l_ind.append(np.argmax(a))

    capt = ''
    for l in l_ind:
        capt += valid_characters[l]
    return capt

with webdriver.Chrome() as driver:
    # get link
    driver.get("https://LoganLieou.github.io/Lettuce")

    # hacking
    img = driver.find_element(By.TAG_NAME, "img").get_attribute("src")

    # wow so scuffed
    img_data= base64.b64decode(img[22:])

    # hacker moment
    with open("temp.png", "wb") as f:
        f.write(img_data)
        f.close()

    prediction = predict("temp.png")
    print(prediction)

    # get element by name and pass keys to that element
    driver.find_element(By.TAG_NAME, "input").send_keys(prediction)
    driver.find_element(By.CLASS_NAME, "submit").click()

    while True:
        print("scuffed")

