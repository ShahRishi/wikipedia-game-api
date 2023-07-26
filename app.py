from bs4 import BeautifulSoup
import queue
import urllib.request
from urllib.request import urlopen
import re
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/query')
def solve():
    bfs_solver = BFSSolver(request.args.get('start_url'), request.args.get('end_url'))
    return jsonify(bfs_solver.solve())


class BFSSolver:
    def __init__(self, start_url, end_url):
        self.start_url = start_url
        self.end_url = end_url
        self.adjList, self.parents, self.status = {}, {}, {}
        self.parents[self.start_url] = None
        self.q = queue.Queue()
        self.found = False

    def getSoup(self, nodeURL):
        nodeHTML = urlopen(nodeURL)
        nodeSoup = BeautifulSoup(nodeHTML, 'html.parser')
        return nodeSoup

    def getTitle(self, link):
        soup = self.getSoup(link)
        title = str(soup.find('title'))
        s = title[7:-20]
        return s

    def nestedLinks(self, soup, soupLink):
        links = []
        for link in soup.find_all('a'):
            if self.found:
                break
            if link.get('href') is not None and re.match(r'/wiki/*', link.get('href')):
                nestedLink = 'https://en.wikipedia.org' + link.get('href')
                links.append(nestedLink)
        self.adjList[soupLink] = links
        return links

    def solve(self):
        self.q.put(self.start_url)
        while not self.q.empty() and not self.found:
            x = self.q.get()
            for child in self.nestedLinks(self.getSoup(x), x):
                if child not in self.parents:
                    self.status[child] = 'visited'
                    self.parents[child] = x
                    print(child)
                    if child == self.end_url:
                        self.found = True
                        break
                self.q.put(child)
        return self.backtrack()

    def backtrack(self):
        currNode = self.end_url
        bfs_tree = []
        while currNode != self.start_url:
            bfs_tree = [self.getTitle(currNode)] + bfs_tree
            currNode = self.parents[currNode]
        bfs_tree = [self.getTitle(currNode)] + bfs_tree
        return bfs_tree


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
