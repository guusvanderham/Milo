# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:08:04 2021

@author: guusv
"""
import pickle
class Child: 
    def __init__(self, name, img, pages_read, font_size, geluid_zichtbaar, opnieuw_zichtbaar, prikkelarm, knopgr): 
        self.name = name
        self.img = img
        self.pages_read = pages_read
        self.font_size = font_size
        self.geluid_zichtbaar = geluid_zichtbaar
        self.opnieuw_zichtbaar = opnieuw_zichtbaar 
        self.prikkelarm = prikkelarm
        self.knopgr = knopgr
dummy = Child('Tim', 'images/sdier1.png', [], 13, 0, 0, 0, 0)

with open('data_kinderen.pkl', 'wb') as output:
    
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)