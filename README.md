# Port Scanner

### What is a Port Number? 


 A port number is a numerical identifier that helps route traffic to the correct service running on a server. For example, when you visit a website, your computer uses the HTTP protocol (which runs on port 80) or HTTPS protocol (which runs on port 443).  These protocols allow your web browser to communicate with web servers, where a web service processes the incoming request and responds accordingly. 

For example, when you type "https://amazon.com" into your browser, it immediately connects to Amazon’s website. Why? 

- Your browser sends an HTTPS request to Amazon's web server, using port 443 (the standard port for HTTPS traffic).

- Since the request is on port 443, Amazon's web server knows it should be handled using the HTTPS protocol.

- The web server application or service, such as Apache or Nginx, processes the request.

- Right before communication continues, your browser requests a security certificate from the server, which is done through TLS (Transport Layer Security), but also for encrypting and securing the entire communication session. 

- Once verified, Amazon's web server sends a response back to your web browser, allowing secure communication and displaying the website. ✔
<hr>

### What is a Port Scanner? 

Since we know what ports are, a port scanner is a type of tool that sends traffic to a certain port and examines the outcome. The result usually gives us one of the three states for each port including: 

<b>Open:</b> This is a port where a service is actively listening for incoming connections. This means that the port is open to receiving traffic (web server, database, SSH) and is actively waiting for communication. These are essential for services to run but they can also expose the system to security risks, especially if there are vulnerabilities within the services. 

<b>Closed:</b> This is a port that is not open to receive connections. When you send a request to a closed port, it will usually respond with an ICMP (Internet Control Message Protocol) packet that replies "destination unreachable" or a TCP RST (reset message). 


 <b>Filtered:</b> This is a port that is blocked by a firewall or another security device, making it inaccessible to the scanner. This is usually a sign of a well-protected system. 

<hr>

To clone the repository, use: `https://github.com/ryanliupie/Port-Scanner.git` 