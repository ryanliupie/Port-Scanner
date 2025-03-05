### What is a Port Number? 

<p> 
    A port number is simply a number that identifies a specific service running on a computer. For example, when you visit a website, your computer uses the HTTP service (which runs on port 80) or the HTTPS service (which runs on port 443). These services help your computer communicate with websites through web browsers like Firefox or Google Chrome. But remember, the browser (like Chrome) is not the service itself – it's the app that helps you access the communication services.
</p>
<p> 
    For example, when you type "https://amazon.com" into your browser, it connects to Amazon’s website using the HTTPS service. This service uses TLS (Transport Layer Security) or SSL (Secure Socket Layer) to secure the connection. When your browser connects to the website, the website sends a certificate to prove its identity. Once everything checks out, you can safely view the site and start interacting with it.
</p>
<p>
    In simple terms, when you use your computer (like a MacBook Pro) to browse the web, port numbers help your computer know where to send requests. The server (the computer hosting the website) listens for incoming requests and looks at the port number to figure out which service the request is meant for. If everything matches up, the server allows the connection to happen.
</p>

<hr>

### What is Port Scanner? 

<p> 
    Since we know what ports are, a port scanner is a type of tool that sends traffic to a certain port and exams the outcome of it. The outcome usually gives us one of the three statues for each port including: 
</p>
<p>
    <b>Open:</b> This a port where a service is actively listening for incoming connections. This means that the port is open to recieving traffic (web server, database, SSH) actively waiting for communication. These are essential for services to run but they can also expose the system to security risks especially if there are vulnerabilites within the services. 
</p>
<p>
    <b>Closed:</b> This is a port that is not open to receive connections. When you send a request to a closed port, it will usually respond with an ICMP (Internet Control Message Protcol) packet which replies "destination unreachable" or a TCP RST (rest message). 
</p>
<p>
    <b>Filtered:</b> This is a port that is blocked caused by a firewall or some kind of security device, making it inaccessible to the scanner. This is usually a sign of a well-protected system. 
</p>