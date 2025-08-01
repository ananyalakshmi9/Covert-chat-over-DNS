# Covert DNS Chat Application

[![Python-3.9+-blue](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![dnslib-orange](https://img.shields.io/badge/Library-dnslib-orange)](https://pypi.org/project/dnslib/)
[![dnspython-brightgreen](https://img.shields.io/badge/Library-dnspython-brightgreen)](https://pypi.org/project/dnspython/)

A proof-of-concept chat application that uses the DNS protocol to send and receive messages, demonstrating the principles of DNS tunneling.

## ⚠️ Disclaimer

This project is for **educational and research purposes only**. Using DNS for covert communication can violate the terms of service of network providers and may be flagged by security monitoring systems. Do not use this for malicious or unauthorized activities.

## 🎯 Key Features

* **DNS Tunneling:** Encapsulates chat messages within DNS queries and responses.
* **Client-Server Architecture:** Includes a custom DNS server and a graphical client.
* **Data Encoding:** Messages are encoded using `base64` to ensure they are safe for transmission as part of a domain name.
* **Custom DNS Server:** Built with `dnslib`, the server listens for specific DNS queries, decodes the messages, and sends a reply.
* **GUI Client:** A simple and user-friendly chat interface built with `tkinter`.
* **TCP/UDP Support:** The server is configured to handle DNS queries over both TCP and UDP.

---

## ⚙️ How It Works

The application leverages the structure of DNS queries to covertly transmit data.

1.  **User Input:** The user types a message in the `tkinter` GUI client.
2.  **Encoding:** The message is encoded into a URL-safe `base64` string.
3.  **Query Formulation:** The encoded string is used as a subdomain label for a predefined domain. For example, the message "hello" becomes `aGVsbG8`, which is then formed into a query for `aGVsbG8.dnschat.test`.
4.  **DNS Query:** The client sends a DNS query for a `TXT` record for this unique domain name to the custom DNS server.
5.  **Server-Side Processing:** The DNS server receives the query, extracts the subdomain (`aGVsbG8`), and decodes it back into the original message ("hello").
6.  **Server Response:** The server logs the message and sends a DNS reply containing a `TXT` record (e.g., "Received: hello") back to the client.
7.  **Display:** The client receives the DNS response, extracts the content from the `TXT` record, and displays it in the chat window.

---

## 🛠️ Tech Stack

* **Language:** Python
* **DNS Server:** `dnslib`
* **DNS Client:** `dnspython`
* **GUI:** `tkinter`

---

## 📂 Project Structure

.
├── 📁 client/
│   ├── 📜 chat_gui.py     # The graphical chat client
│   └── 📜 utils.py         # Helper functions for encoding/decoding
│
├── 📁 server/
│   └── 📜 dns_server.py     # The custom DNS server
│
└── 📜 requirements.txt    # Project dependencies


---

## 🚀 Getting Started

### Prerequisites

* Python 3.9 or higher
* Administrator/root privileges to run the server on a privileged port (if you change it from 5353 to 53).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(You will need to create a `requirements.txt` file containing `dnspython`, `dnslib`, and `windows-curses` for Windows users.)*

### Running the Application

You must run the server first, then the client.

1.  **Start the DNS Server:**
    Open a terminal and run the server script.
    ```bash
    python server/dns_server.py
    ```
    You should see the message: `DNS Server running on port 5353 (TCP and UDP)...`

2.  **Run the Chat Client:**
    Open a **second terminal** and run the client GUI script.
    ```bash
    python client/chat_gui.py
    ```
    A chat window will appear.

3.  **Configure DNS Resolution (Important):**
    For the client to find the server, your system's DNS resolver must know where to send queries for the `dnschat.test` domain. For local testing, you must configure your client's DNS resolver to point to `127.0.0.1`.
    * **On Windows/Linux/macOS:** You may need to edit your `hosts` file or network adapter settings to use `127.0.0.1` as your primary DNS server for this to work.

4.  **Start Chatting:**
    Type a message in the client window and press Enter or click Send. The message will appear in the 
