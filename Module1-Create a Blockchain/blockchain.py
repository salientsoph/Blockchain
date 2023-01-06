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
                 'proof': proof,
                 'previous_hash': previous_hash
                 }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 + previous_proof**2).encode()).hexadigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1 
        return new_proof
            
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=true).encode()
        return hashlib.sha256(encoded_block).hexdigest()
        
        
        
# Part 2 - Mining our Blockchain




