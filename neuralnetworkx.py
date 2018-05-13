#encoding=utf-8
import networkx as nx
import matplotlib.pyplot as plt 
import random 
import numpy as np 
# import matplotlib.animation
from matplotlib import animation 
# fig = plt.figure(facecolor='white')



class Graph(object):
    def __init__(self, layer_sizes=[2,3,1], position=[.1, .9, .1, .9]):
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.setSize(layer_sizes)
        self.setPosition(position)
        self.image_pos = []
        self.G = nx.Graph()
        # self.fig = plt.figure(num=None, figsize=None, dpi=None, facecolor='black', edgecolor=None, frameon=True, FigureClass=Figure)
        # self.weighted_color=range(len(self.G.edges))
        # self.draw()
    # def __call__(self, layer_sizes):
    #     return self.setSize(layer_sizes)

    def setSize(self, layer_sizes):
        self.layer_sizes = layer_sizes
    def setPosition(self, position):
        self.position = position
        
    def setGraph(self):
        self.node_count = 0
        [left, right, bottom, top] = self.position
        v_spacing = (top - bottom)/float(max(self.layer_sizes))
        h_spacing = (right - left)/float(len(self.layer_sizes) - 1)
        
        for i, v in enumerate(self.layer_sizes):
            layer_top = v_spacing*(v-1)/2. + (top + bottom)/2.
            for j in range(v):
                self.G.add_node(self.node_count, pos=(left + i*h_spacing, layer_top - j*v_spacing))
                self.node_count += 1
        for x, (left_nodes, right_nodes) in enumerate(zip(self.layer_sizes[:-1], self.layer_sizes[1:])):
            for i in range(left_nodes):
                for j in range(right_nodes):
                    self.G.add_edge(i+sum(self.layer_sizes[:x]), j+sum(self.layer_sizes[:x+1])) 
    
    def from_torch(self, net):
        self.layer_sizes = []
        self.weighted_color = []
        for idx, m in enumerate(net.named_modules()):
            if idx:
                array = eval('net.'+m[0]+'.weight.data.numpy()')
                t = array.shape
                darray = array.reshape((t[0]*t[1]), order='F')
                self.weighted_color = np.append(self.weighted_color, darray)
                if idx==1:
                    self.layer_sizes.append(t[1])
                    self.layer_sizes.append(t[0])
                else:
                    self.layer_sizes.append(t[0])


    def draw(self):
        nx.draw(self.G, 
                pos=nx.get_node_attributes(self.G,'pos'),
                node_color=range(self.node_count), 
                # with_labels=True,
                node_size=200, 
                # edge_color=[-0.2 for i in range(len(self.G.edges))],
                # edge_color=np.arange(len(self.G.edges)),
                # edge_color=[int(i) for i in 10*self.weighted_color],
                edge_color=self.weighted_color,
                # edge_color = range(50),
                width=3, 
                cmap=plt.cm.Dark2, # matplotlib的调色板，可以搜搜，很多颜色呢
                edge_cmap=plt.cm.Blues
               )
    def show(self):
        self.setGraph()
        self.draw()
        plt.plot()
        plt.show()
    def animation(self):
        self.G = nx.Graph()
        self.setGraph()
        nodes = nx.draw_networkx_nodes(self.G, 
            pos=nx.get_node_attributes(self.G,'pos'),
            node_color=range(self.node_count), 
            node_size=200, 
            cmap=plt.cm.Dark2,)
        edges = nx.draw_networkx_edges(self.G, 
            pos=nx.get_node_attributes(self.G,'pos'),
            edge_color=self.weighted_color*1000,
            width=3,
            edge_cmap=plt.cm.Blues)
        self.image_pos.append([nodes, edges,])

    def ani_show(self, interval=10):
        ani_pos = animation.ArtistAnimation(self.fig, self.image_pos, interval=interval, repeat=False)
        plt.show()













