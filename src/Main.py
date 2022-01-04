# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

from Configuration import Configuration
from Section import Section
from Wall import Wall
from Door import Door
from Window import Window
from House import House
from Opening import Opening
import copy


def Q1a():
    return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}).display()
    
def Q1b_f():
    return Configuration({'screenPosition': -5, 'xAxisColor': [1, 1, 0]}). \
        setParameter('xAxisColor', [1, 1, 0]). \
        setParameter('yAxisCo lor', [0,1,1]). \
        display()
        
def Q2b():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6})
            ) 

def Q2c():
    # Ecriture en utilisant le chaînage
    return Configuration().add(
            Section({'position': [1, 1, 0], 'width':7, 'height':2.6, 'edges': True})
            )

def Q3a():
    return Configuration().add(Wall({'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.6, 'color': [1, 0.74, 0.46]})) #'color': [255, 190, 118]

def Q4a():
    # Ecriture en utilisant des variables : A compléter
    wall1 = Wall({'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.6, 'color': [1, 0.74, 0.46]})
    wall2 = Wall({'width': 4, 'height': 2.5, 'orientation': 0, 'thickness': 0.6, 'color': [1, 0.74, 0.46]})
    wall3 = Wall({'position': [0, 7.4, 0], 'width': 4, 'height': 2.5, 'orientation': 0, 'thickness': 0.6, 'color': [1, 0.74, 0.46]})
    wall4 =  Wall({'position': [0, -4.6, 0], 'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.6, 'color': [1, 0.74, 0.46]})  
    house = House({'position': [-3, 1, 0], 'orientation':0})
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    return Configuration().add(house)   
    
def Q5a():  
    # Ecriture avec mélange de variable et de chaînage    
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})    
    return Configuration().add(opening1).add(opening2)
    
def Q5b():  
    # Ecriture avec mélange de variable et de chaînage   
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    opening3 = Opening({'position': [4, 0, 1.7], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    
    print(section.canCreateOpening(opening1))
    print(section.canCreateOpening(opening2))    
    print(section.canCreateOpening(opening3))
    return Configuration()    
    
def Q5c1():      
    section = Section({'width':7, 'height':2.6})
    opening1 = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    sections = section.createNewSections(opening1)
    configuration = Configuration()
    for x in sections:
        configuration.add(x)    
    return configuration     
    
def Q5c2():      
    section = Section({'width':7, 'height':2.6})
    opening2 = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    sections = section.createNewSections(opening2)
    configuration = Configuration()
    for section in sections:
        configuration.add(section)    
    return configuration    

def Q5d():      
    wall = Wall({"position":[0, 0, 0], 'width':7, 'height':2.6})
    door = Opening({'position': [2, 0, 0], 'width':0.9, 'height':2.15, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]})
    window = Opening({'position': [4, 0, 1.2], 'width':1.25, 'height':1, 'thickness':0.2, 'color': [0.7, 0.7, 0.7]}) 
    wall.add(door), wall.add(window)
    return Configuration().add(wall)
    
def Q6():  
    wall1 = Wall({'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    wall2 = Wall({'width': 4, 'height': 2.5, 'orientation': 0, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    wall3 = Wall({'position': [0, 7.8, 0], 'width': 4, 'height': 2.5, 'orientation': 0, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    wall4 = Wall({'position': [0, -4.2, 0], 'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    door = Door({'position': [2, 0.1, 0]})
    window = Window({'position': [4, 0.1, 1.25]}) 
    wall1.add(door)
    wall1.add(window)
    house = House()
    house.add(wall1).add(wall3).add(wall4).add(wall2)
    return Configuration().add(house)  

def Q7():
    wall1 = Wall({'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    wall2 = Wall({'width': 4, 'height': 2.5, 'orientation': 0, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    wall3 = Wall({'position': [0, 7.8, 0], 'width': 4, 'height': 2.5, 'orientation': 0, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})
    wall4 = Wall({'position': [0, -4.2, 0], 'width': 8, 'height': 2.5, 'orientation': 90, 'thickness': 0.2, 'color': [1, 0.74, 0.46]})

    door = Door({'position': [2, 0.1, 0]})
    window = Window({'position': [4, 0.1, 1.25]}) 
    wall1.add(door)
    wall1.add(window)

    house1 = House()
    house2 = House({'position': [0, 8, 0]})
    house1.add(wall1).add(wall3).add(wall4).add(wall2)
    house2.add(wall1).add(wall3).add(wall4).add(wall2)
    
    return Configuration().add(house1).add(house2)

def main():
    # Enlever un des commentaires pour la question traitée
    
    #configuration = Q1a()
    #configuration = Q1b_f()
    #configuration = Q2b()
    #configuration = Q2c()
    #configuration = Q3a()
    #configuration = Q4a()
    #configuration = Q5a()
    #configuration = Q5b()
    #configuration = Q5c1()
    #configuration = Q5c2() 
    #configuration = Q5d()
    #configuration = Q6()
    configuration = Q7()
    configuration.display()     
         
# Calls the main function
if __name__ == "__main__":
    main()    
