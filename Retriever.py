#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 09:42:33 2019

@author: cranial490
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from kiteconnect import KiteConnect
import util


def getRequestToken(ResponseUrl):
    start = ResponseUrl.index('request_token')
    end = ResponseUrl.index('&action')
    tokenString = ResponseUrl[start:end]
    return tokenString[tokenString.index('=') + 1:]


def getAccessToken(localPath):
    configParser = util.fetch_config(localPath)
    userId = util.get_config(configParser, 'login', 'username')
    password = util.get_config(configParser, 'login', 'password')
    api_key = util.get_config(configParser, 'connection', 'api_key')
    api_secret = util.get_config(configParser, 'connection', 'api_secret')
    pin = util.get_config(configParser, 'login', 'pin')

    # Download the webdriver and give the correct path of the webdriver file below
    browser = webdriver.Chrome(util.get_config(
        configParser, 'paths', 'chromeDriver'))
    browser.get(util.get_config(configParser, 'connection', 'endpoint_url'))

    browser.implicitly_wait(10)

    userIdField = browser.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[2]/form/div[1]/input')
    userIdField.send_keys(userId)

    passField = browser.find_element_by_xpath(
        '//*[@id="container"]/div/div/div[2]/form/div[2]/input')
    passField.send_keys(password)
    passField.send_keys(Keys.ENTER)

    browser.implicitly_wait(5)

    pinField = browser.find_element_by_xpath(
        '//*[@id="container"]/div/div/div/form/div[2]/div/input')
    pinField.send_keys(pin)
    pinField.send_keys(Keys.ENTER)

    time.sleep(1)
    ResponseUrl = browser.current_url
    browser.quit()
    # extract the request token from the ReposnseUrl
    print("Received Url:", ResponseUrl)
    requestToken = getRequestToken(ResponseUrl)
    print("Extracted request token:", requestToken)
    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(requestToken, api_secret)
    accessToken = data["access_token"]
    print("Retrieved Token:", accessToken)
    return accessToken

    #searchBut = browser.find_element_by_class_name('gNO89b')
    # searchBut.click()
