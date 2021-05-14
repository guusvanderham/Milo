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
dummy2 = Child('Lieke', 'images/sdier2.png', [], 13, 0, 0, 0, 0)
dummy3 = Child('Jorik','images/sdier3.png', [], 13, 0, 0, 0, 0)
dummy4 = Child('Noraja','images/sdier4.png', [], 13, 0, 0, 0, 0)
dummy5 = Child('Sophie','images/sdier7.png', [], 13, 0, 0, 0, 0)
dummy6 = Child('Arjan','images/sdier6.png', [], 13, 0, 0, 0, 0)
dummy7 = Child('Anne','images/sdier5.png', [], 13, 0, 0, 0, 0)

with open('data_kinderen.pkl', 'wb') as output:
    
    pickle.dump(dummy, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy2, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy3, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy4, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy5, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy6, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(dummy7, output, pickle.HIGHEST_PROTOCOL)