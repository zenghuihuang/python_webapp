# Simple Python Web Server

This is a basic Python web server built using the http.server module. It serves an HTML response for GET requests.
## Prerequisites

Python 3.x installed on your system

## Usage
Use the Secure Copy Protocol (SCP) to transfer files to a remote host over SSH. The command below demonstrates how to transfer a file to a Raspberry Pi that is connected to the same network as the host.
```bash
scp web_server.py <username>@<raspberry_pi_ip>:~/repos/web_server.py
```
## Or use 

```bash
scp -r . <username>@<raspberry_pi_ip>:~/repos
```
 - -r → Copies directories recursively.  
 - Replace <raspberry-pi-ip> with your actual Raspberry Pi IP address.  
 - ~/repos → This is the destination folder on your Raspberry Pi.

## Run curl or wget to check your web app:

```bash
curl http://localhost:8080
```
or 
```bash
wget -qO- http://localhost:8080
```
You can also access the web app from your local machine using a browser by entering the IP address of your Raspberry Pi,
like this: http://<raspberry_pi_ip>:8080.

