# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
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
                [0, 3, 2, 1],
                [4, 5, 6, 7],
                [0, 1, 7, 4],
                [3, 5, 6, 2],
                [1, 2, 6, 7],
                [0, 3, 5, 4],
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        if x.getParameter("position")[0] + x.getParameter("width") > self.parameters["position"][0] + self.parameters["width"]:
            return False
        elif x.getParameter("position")[0]< self.parameters["position"][0] :
            return False
        elif x.getParameter("position")[2] + x.getParameter("height") > self.parameters["position"][2] + self.parameters["height"]:
            return False
        elif x.getParameter("position")[2] < self.parameters["position"][2]:
            return False  
        return True
            
    # Creates the new sections for the object x
    def createNewSections(self, x):
        section = []
        
        section1 = Section({
                "position": self.parameters["position"], 
                "width": x.getParameter("position")[0], 
                "height": self.parameters["height"], 
                "thickness": self.parameters["thickness"], 
                "color" : self.parameters["color"], 
                "edges": self.parameters['edges'], 
                "orientation": self.parameters["orientation"]})
        
        section2 = Section({
                "position": [self.parameters["position"][0] + section1.parameters["width"], self.parameters["position"][1], self.parameters["position"][2] + x.getParameter("position")[2]+x.getParameter("height")],
                "width":        x.getParameter("width"), 
                "height":       self.parameters["height"]-x.getParameter("height")-(x.getParameter("position")[2]-self.parameters["position"][2]),
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
    
        section3 = Section({
                "position": [self.parameters["position"][0] +    section1.parameters["width"], self.parameters["position"][1], self.parameters["position"][2]],
                "width":        x.getParameter("width"),
                "height":       self.parameters["height"]-x.getParameter("height")-section2.parameters["height"],
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
    
        section4 = Section({
                "position":[self.parameters["position"][0] + section1.parameters["width"]+x.getParameter("width"), self.parameters["position"][1], self.parameters["position"][2]],
                "width":        self.parameters["width"]-section1.parameters["width"]-x.getParameter("width"),
                "height":       self.parameters["height"],
                "thickness":    self.parameters["thickness"],
                "color" :       self.parameters["color"],
                "edges":        self.parameters['edges'],
                "orientation":  self.parameters["orientation"]
            })
    
        if section1.parameters["width"] > 0 : 
            section.append(section1)        
    
        if section2.parameters["height"] > 0 : 
            section.append(section2)

        if section3.parameters["height"] > 0 : 
            section.append(section3)
            
        if section4.parameters["width"] > 0 : 
            section.append(section4)
        
        return section             
        
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        index = [0, 1, 2, 3, 0]
        for i in self.faces:
            for k in range(1, len(index)):
                gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) # on trace les faces : GL_FILL
                gl.glBegin(gl.GL_LINES) # Tracé d’un quadrilatère
                gl.glColor3fv([self.parameters['color'][0]*0.8, self.parameters['color'][1]*0.8, self.parameters['color'][2]*0.8]) # Couleur gris moyen
                gl.glVertex3fv(self.vertices[i[index[k-1]]])
                gl.glVertex3fv(self.vertices[i[index[k]]])
                gl.glEnd()
            
                    
    # Draws the faces
    def draw(self):
        gl.glPushMatrix()
        if self.parameters['edges'] == True:
            self.drawEdges()
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
  