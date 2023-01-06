#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Module 1 - Create a Blockchain 
"""
Created on Thu Jan  5 21:06:29 2023

@author: salient
"""

# Importing the libraries 
import datetime 
import hashlib 
import json 
from flask import Flask, jsonify 


# Part 1 - Building a Blockchain
Class Blockchain:
    def __init__(self): 
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain) + 1,
                 'timestamp': str(datetime.date.now()),
                 'proof': 
                 }

# Part 2 - Mining our Blockchain




