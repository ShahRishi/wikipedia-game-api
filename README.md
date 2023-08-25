# Wikipedia Game API

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white)
![GitHub Actions](https://github.com/ShahRishi/wikipedia-game-api/actions/workflows/main.yml/badge.svg)


The Wikipedia Game API is an API that determines the path between two Wikipedia articles by following their links. This tool uses Breadth-First Search (BFS) to traverse through the links on Wikipedia pages, starting from a given 'start' page until it reaches the desired 'end' page. You can visualize it as the shortest path between two Wikipedia articles based purely on their links.

## 🌟 Features

- 🚀 Utilizes BFS for shortest path detection between Wikipedia articles.
- 📜 Returns a list of Wikipedia article titles that constitute the path between the starting and ending URL.
- 🔥 Easily deployable Flask application.
- 🕸️ Built-in support for BeautifulSoup to parse web content.

## 🚀 API Endpoint

### `GET /query`

Fetch the shortest path between two Wikipedia articles using their links.

**Parameters:**
- `start_url`: The full Wikipedia URL from where the search begins.
- `end_url`: The full Wikipedia URL where the search ends.

**Response:**
- A list of Wikipedia article titles from `start_url` to `end_url`, representing the path.

## 🌐 Deployment

This API was deployed to a simple Debian server. You can try the live version of this tool at [http://45.33.125.208:5000/query?start_url=[start_url]&end_url=[end_url]](http://45.33.125.208:5000/).

## 💡 How to Run Locally
1. Clone the repository.
```bash
   git clone https://github.com/ShahRishi/wikipedia-game-api.git
   cd wikipedia-game-api
```
2. Set up a virtual environment (optional)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages.
```bash
pip install -r requirements.txt
```
4. Run API
```bash
python3 app.py
```
