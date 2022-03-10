#!/usr/bin/env python
# coding: utf-8

########## IMPORT LIBRARIES ##########
# import libraries
from bs4 import BeautifulSoup        # scraping library for .html
import queue                         # DS for BFS
import urllib.request                # generate .html from URLs
from urllib.request import urlopen   # generate .html from URLs
import re                            # regular expression



########## READ INPUT ##########
rootLink = input("Please enter your starting URL: ")   # source node
destLink = input("Please enter your ending URL: ")     # dest node



########## INIITALIZE DATA STRUCTURES ##########
adjList, parents, status = {}, {}, {} # hashtables
parents[rootLink] = None              # setting root node
q = queue.Queue()                     # init empty queue
found = False                         # terminating condition



########## HELPER METHODS ##########
### --- getSoup(nodeURL) - returns soup object for a Wikipedia URL
# input: url of the current 'node' (page)
# returns the soup of the current node
def getSoup(nodeURL):
    nodeHTML = urlopen(nodeURL)
    nodeSoup = BeautifulSoup(nodeHTML, 'html.parser')    #creates soup object for nodeURL
    return nodeSoup

### --- getTitle(link) - returns title string of Wikipedia page
#input: link of page
#output: title of page
def getTitle(link):
    soup = getSoup(link)
    title = str(soup.find('title'))
    s = title[7:-20]
    return s

### --- nestedLinks(soup, soupLink) - returns all nested links in a Wikipedia page
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



########## BUILD BFS Tree ##########
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
                for i in range(3):
                    print()
                print("******Solution Found!******")
                found = True
                break
        q.put(child)



########## BACKTRACK BFS TREE ##########
print()
print("-----Backtracking BFS Tree-----")
print()
currNode = destLink
BFSTree = []
while currNode != rootLink:
    BFSTree = [getTitle(currNode)] + BFSTree
    currNode = parents[currNode]
BFSTree = [getTitle(currNode)] + BFSTree
print('Link Tree: ' + str(BFSTree))
print()
