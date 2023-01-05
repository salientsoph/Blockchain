#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Module 1 - Create a Blockchain 
"""
Created on Thu Jan  5 21:06:29 2023

@author: salient
"""

# Importing the libraries 
import datetime #각 블록마다 블록이 생성되고 채굴된 정확한 날짜의 타임스탬프를 가짐
import hashlib #블록을 해시할 때 사용함
import json #블록을 해시하기 전 블록 인코딩을 위해 dumps 함수 사용을 위해
from flask import Flask, jsonify 
#Flask: 웹 애플리케이션이 되는 Flask 클래스의 객체를 생성
#Jsonify: postman에서 블록체인과 상호작용할 때 메세지를 보내기 위해 사용하는 함수
#예시1. postman에서 전체 블록체인을 표시하기 위해 블록체인의 실제 상태를 요청할 때 사용 - Jsonify를 이용해 요청에 관한 응답을 표시함
#예시2. 새로운 블록을 채굴하여 블록체인에 추가할 때. Jsonify 함수를 이용해 Json 형식으로 채굴된 새로운 블록의 핵심 정보로 돌아감


# Part 1 - Building a Blockchain
Class Blockchain:
    def __init__(self): 
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

# Part 2 - Mining our Blockchain




