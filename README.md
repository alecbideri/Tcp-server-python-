## TCP Server

## Overview

This repository contains a simple multithreaded TCP server implemented in Python. The server listens for incoming connections, handles each connection in a separate thread, and responds with a predefined message. This can serve as a foundational codebase for various applications such as command shells, proxy servers, chat applications, and more.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Potential Applications](#potential-applications)
- [Limitations](#limitations)
- [Improvements](#improvements)
- [Contributing](#contributing)
- [License](#license)
- [Further Reading](#further-reading)

## Installation

To run this TCP server, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Clone this repository to your local machine:

```bash
git clone https://github.com/alecbideri/TCP-SERVER-python.git
cd TCP-SERVER-python
```

## Usage

Run the TCP server script using the following command:

```bash
python test_tcp_server.py
```

The server will start listening on all available network interfaces (`0.0.0.0`) and port `9998`. When a client connects, the server will handle the connection in a new thread and respond with a predefined message.

## Code Explanation

The code is structured into two main functions:

1. `main()`: Initializes the server, binds it to the specified IP and port, and listens for incoming connections. Each connection is handled in a separate thread.

2. `handle_client(client_socket)`: Handles the client connection, receives data from the client, sends a response, and then closes the connection.

For a detailed explanation of the code, refer to the [Google Docs documentation](https://docs.google.com/document/d/12loVy4EQqJ5R78CtPgF1uM_2473xI4ki9HZBCpUJSPw/edit?usp=sharing).
