# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:38:59 2019

@author: User
"""

import BBNode as bn
root = bn.BBNode(None, '', '', 0)
node1 = bn.BBNode(root, 'x1', 'ub', 1)
node2 = bn.BBNode(root, 'x1', 'lb', 2)
node21 = bn.BBNode(node2, 'x2', 'ub', 2)
node22 = bn.BBNode(node2, 'x2', 'lb', 3)

dvNode = node22

print 'Showing bounds from node 22 to root'
while dvNode != root:
    print dvNode.dv, dvNode.boundSense, dvNode.bound
    dvNode = dvNode.parent