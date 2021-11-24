# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        x, y ,z =  self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2]
        self.vertices = [ 
                [x, y , z], #0
                [x, y,z+ self.parameters['height']], #1
                [x+self.parameters['width'], y, self.parameters['height']+z], #2
                [x+self.parameters['width'], y, z], #3
				[x+0, self.parameters['thickness']+y, z], #4
                [x+ self.parameters['width'], y+self.parameters['thickness'], z], #5
                [x+self.parameters['width'],y+ self.parameters['thickness'], z+self.parameters['height']], #6
                [x+0, y+self.parameters['thickness'], self.parameters['height']+z] #7
                ]
        self.faces = [
                [0, 1, 7, 4],
                [3, 5, 6, 2],
                [1, 2, 6, 7],
                [0, 3, 5, 4],
                ]   
        
    # Draws the faces                
    def draw(self):        
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        for i in self.faces:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
            gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
            gl.glColor3fv(self.parameters['color']) # Couleur gris moyen
            gl.glVertex3fv(self.vertices[i[0]])
            gl.glVertex3fv(self.vertices[i[1]])
            gl.glVertex3fv(self.vertices[i[2]])
            gl.glVertex3fv(self.vertices[i[3]])
            gl.glEnd()
        gl.glPopMatrix()