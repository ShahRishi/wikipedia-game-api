#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from queue import Queue
import urllib.request
from urllib.request import urlopen
import re
import queue


# In[10]:


rootLink = input("Please enter your starting URL: ")
rootHTML = urlopen(rootLink)
destLink = input("Please enter your ending URL: ")
#destHTML = urlopen(destLink)


# In[11]:


adjList, parents, status = {}, {}, {}
parents[rootLink] = None
q = queue.Queue()
found = False


# In[12]:


#input: link of page
#output: title of page
def getTitle(link):
    soup = getSoup(link)
    title = str(soup.find('title'))
    s = title[7:-20]
    return s


# In[13]:


#input: soup page
#output: list of all strings in a file
#houskeeping: adds parents of children of soup, 
def nestedLinks(soup, soupLink):
    global found
    links = []
    for link in soup.find_all('a'):
        if found == True:
            break
        if link.get('href') != None:
            if re.match(r'/wiki/*', link.get('href')):
                nestedLink = 'https://en.wikipedia.org' + link.get('href')
                links += [nestedLink]            #bucket for input soupLink
    adjList[soupLink] = links                    #creates adjacency list
    return links



#input: url of the current 'node' (page)
#returns the soup of the current node
def getSoup(nodeURL):
    nodeHTML = urlopen(nodeURL)
    nodeSoup = BeautifulSoup(nodeHTML, 'html.parser')    #creates soup object for nodeURL
    return nodeSoup



q.put(rootLink)
while (q.empty() == False) and (found == False):
    x = q.get()
    print(x)
    for child in nestedLinks(getSoup(x), x):
        if child not in parents:
            status[child] = 'visited'
            parents[child] = x
            print(child)
            if child == destLink:
                print("******Solution Found!******")
                found = True
                break
        q.put(child)


# In[8]:




print("Backtracking BFS Tree")
currNode = destLink
BFSTree = []

while currNode != rootLink:
    print(currNode)
    BFSTree = [currNode] + BFSTree
    currNode = parents[currNode]
BFSTree = [currNode] + BFSTree
print(BFSTree)



