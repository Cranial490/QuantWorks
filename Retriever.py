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


def getRequestToken(ResponseUrl):
    start = ResponseUrl.index('request_token')
    end = ResponseUrl.index('&action')
    tokenString = ResponseUrl[start:end]
    return tokenString[tokenString.index('=') + 1:]


def getAccessToken():
    userId = 'ZE0956'
    password = 'Colesprouse@490'
    api_key = "irtkrxee8bs6fecn"
    api_secret = "tvxt0yqzkkpkb90f6a78gliz3sk97ebe"
    pin = '016479'

    # Download the webdriver and give the correct path of the webdriver file below
    browser = webdriver.Chrome(
        '/Users/pp067807/Desktop/deleteLater/workSpace/dependencies/chromedriver')
    browser.get('https://kite.trade/connect/login?v=3&api_key=irtkrxee8bs6fecn')

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
