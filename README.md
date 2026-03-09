# Caching Proxy CLI

A command-line tool that starts a caching proxy server. The proxy forwards incoming HTTP requests to an origin server, caches responses, and serves cached responses for repeated requests to improve performance and reduce unnecessary network calls.

---

## Overview

This project implements a simple **HTTP caching proxy**. When a client makes a request to the proxy server, the proxy:

1. Checks whether a cached response for that request already exists.
2. If cached, returns the stored response.
3. If not cached, forwards the request to the origin server.
4. Stores the response in the cache.
5. Returns the response to the client.

The proxy also includes a mechanism to **clear the cache**.
Project url: https://roadmap.sh/projects/caching-server
---

## Features

* CLI tool for starting a caching proxy
* Request forwarding to an origin server
* In-memory caching of responses
* Cache hit/miss response headers
* Manual cache clearing
* Supports multiple HTTP methods (GET, POST, PUT, DELETE, PATCH)
* Asynchronous request handling

---

## Technologies Used

* Python 3
* FastAPI
* Uvicorn
* HTTPX
* cachetools

---

## Project Structure

```
caching-proxy/
│
├── main.py           # FastAPI application
├── proxy_server.py   # Request forwarding and caching logic
├── cache.py          # Cache implementation
├── cli.py            # CLI entry point
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/caching-proxy.git
cd caching-proxy
```

### 2. Create a virtual environment

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Usage

Start the proxy server using the CLI.

```
python cli.py --port <number> --origin <url>
```

### Example

```
python cli.py --port 3000 --origin https://jsonplaceholder.typicode.com
```

This will:

* Start the proxy server on port **3000**
* Forward requests to **https://jsonplaceholder.typicode.com**

---

## Making Requests

Once the proxy server is running, send requests to it instead of the origin server.

Example request:

```
curl http://localhost:3000/posts
```

The proxy forwards the request to:

```
https://jsonplaceholder.typicode.com/posts
```

---

## Cache Headers

The proxy adds an `X-Cache` header to indicate whether the response was served from cache.

### Cache Miss

First request:

```
X-Cache: MISS
```

Meaning the proxy forwarded the request to the origin server.

### Cache Hit

Subsequent requests:

```
X-Cache: HIT
```

Meaning the response was served from the proxy's cache.

---

## Clearing the Cache

You can clear the cache using the CLI.

```
python cli.py --clear-cache
```

After clearing the cache, the next request will result in a **cache miss**.

---

## Example Workflow

Start the proxy:

```
python cli.py --port 3000 --origin https://jsonplaceholder.typicode.com
```

Make a request:

```
curl -i http://localhost:3000/posts
```

First response:

```
X-Cache: MISS
```

Repeat the request:

```
curl -i http://localhost:3000/posts
```

Second response:

```
X-Cache: HIT
```

---

## How Caching Works

Each request is identified using a **cache key** composed of:

```
HTTP_METHOD + URL
```

Example:

```
GET:http://localhost:3000/posts
```

If the key exists in the cache, the stored response is returned instead of contacting the origin server.

The cache uses a **TTL (time-to-live)** strategy to automatically remove old entries.

---

## Limitations

* Cache is stored in memory and is cleared when the server stops.
* Large responses may consume significant memory.
* Cache invalidation is manual or TTL-based.

---

## Possible Improvements

Future enhancements could include:

* Redis or disk-based caching
* Cache size limits with LRU eviction
* Streaming large responses
* Cache invalidation rules
* Logging and monitoring
* Docker support

---

## License

This project is open source and available under the MIT License.
