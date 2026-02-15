---
title: HTTP and response codes
url: https://woocommerce.com/document/http-and-response-codes/
---

When managing a website, understanding HTTP and response codes is helpful for ensuring your site runs smoothly. HTTP (HyperText Transfer Protocol) forms the backbone of how users and sites communicate data over the web. Whether you’re browsing a website or managing your own, every interaction on the internet involves HTTP requests and responses.

HTTP codes are the responses that servers send back to your browser. These codes are not just numbers; they tell you if your request was successful, if there was an error, or if you need to take another action.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

HTTP operates on a client-server model, which relies on the request-response process:

1. **Initiating a Request**: When you type a URL into your browser or click a link, this prompts your browser to establish a TCP connection (a reliable link between your browser and the server) to the server that hosts the requested URL. This connection is necessary for sending and receiving data reliably.
2. Sending the Request : Through the established connection, your browser sends an HTTP request to the server. This request includes:
  - **HTTP Method**: Indicates the action you want the server to take, such as GET to retrieve data or POST to submit data.
  - **Resource Path**: Specifies the location of the resource you are requesting, like a webpage or image.
  - **Headers**: Carry additional options and information like browser type, supported content formats, and authentication tokens.
  
3. **Processing the Request**: The server receives and processes the request. It may retrieve data, interact with other backend systems, or execute server-side logic to generate dynamic content based on the request.
4. Generating a Response : After processing the request, the server responds with an HTTP response. This response contains:
  - **Status Code**: A numerical code indicating the result of the request (e.g., 200 for success or 404 for not found).
  - **Response Body**: The actual data requested, such as HTML content.
  - **Response Headers**: Instructions for the browser on how to handle the response, such as content type and caching policies.
  
5. **Closing the Connection**: The connection between the browser and server may close or remain open for further requests, depending on the headers. This helps optimize subsequent interactions by reducing the time needed to reestablish connections.

Here is an in-depth example of the request-response process.

Imagine you want to access the homepage of a website, say example.com. Your browser would send an HTTP request that might look like this:

```
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

- **GET**: The HTTP method used to request data from a specified resource.
- **/**: The path to the resource on the server (in this case, the root directory).
- **HTTP/1.1**: The version of the HTTP protocol being used.
- **Host**: The domain name of the server (here, example.com).
- **User-Agent**: Information about the browser making the request.
- **Accept**: The types of content the client can process.
- **Accept-Language**: The language preference of the client.
- **Accept-Encoding**: The encoding formats accepted by the client.
- **Connection**: Indicates if the connection will be closed or kept alive after the transaction.

In response to the above request, the server might send back something like this:

```
HTTP/1.1 200 OK
Date: Mon, 23 Oct 2023 14:22:18 GMT
Server: Apache/2.4.1 (Unix)
Last-Modified: Wed, 20 Oct 2023 07:28:00 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 3423
Accept-Ranges: bytes
Connection: close

<html>
<head>
    <title>An Example Page</title>
</head>
<body>
    <h1>Welcome to example.com!</h1>
    <p>This is a simple example of an HTTP response.</p>
</body>
</html>
```

- **HTTP/1.1 200 OK**: The status line includes the HTTP version, status code (200), and reason phrase (OK) indicating that the request has succeeded.
- **Date**: The date and time at which the response was sent.
- **Server**: Information about the server software being used.
- **Last-Modified**: The date and time the requested resource was last modified.
- **Content-Type**: The type of data the response contains.
- **Content-Length**: The length of the response body in bytes.
- **Accept-Ranges**: Indicates the server accepts range requests for the resource.
- **Connection**: Specifies that the connection will be closed after completing the request.

This example illustrates a basic interaction between a client (browser) and a server using HTTP.

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP, using encryption to safeguard data exchanged between your browser and websites.

It employs SSL (Secure Sockets Layer) certificates to establish a secure connection, ensuring that the data remains private and that the website you’re connecting to is authentic. This added layer of security protects sensitive information from interception.

You can learn more about [SSL and HTTPS for your WooCommerce store here](https://woocommerce.com/document/ssl-and-https/).

When browsing the web, you might occasionally encounter HTTP error messages. These errors indicate that something went wrong during your interaction with a website. The first digit of the status code groups HTTP codes into five categories:

- 1xx (Informational): These codes indicate that the server has received the request and is continuing the process with a temporary response.
- 2xx (Successful): These codes show that the server successfully received, understood, and accepted the request.
- 3xx (Redirection): These codes inform the browser that additional action, such as a redirect to another URL, is needed to complete the request.
- 4xx (Client Error): These codes signal errors caused by bad syntax in the request or an inability to fulfill it, such as a 404 Not Found error when a requested page is unavailable.
- **5xx (Server Error)**: These indicate problems on the server side that prevent it from fulfilling a valid request, like a 500 Internal Server Error.

Understanding these categories helps in diagnosing and resolving issues when a website doesn’t behave as expected. Each category pinpoints a different area of responsibility, from client-side problems to server-side issues that might require different approaches to solve.

Here’s a succinct overview using bullet points to list the most common HTTP codes within each category:

- 1xx (Informational)
  - **100 Continue**: The server has received the initial part of the request and is waiting for the remainder.
  - **101 Switching protocols**: The requester has asked the server to switch protocols and the server has agreed.
  
- 2xx (Successful)
  - 200 OK: The server successfully received, understood, and accepted the request.
  - 201 Created: The server fulfilled the request and created a new resource as a result.
  
- 3xx (Redirection)
  - **301 Moved permanently**: The URL of the requested resource has been changed permanently. The response provides the new URL.
  - **302 Found**: The server has found a temporary redirection. Use this URL again next time since it is only temporary.
  
- 4xx (Client error)
  - **400 Bad request**: The server cannot process the request due to a client error.
  - **401 Unauthorized**: Necessary authentication credentials are not provided or are invalid.
  - **403 Forbidden**: The server understood the request, but is refusing to fulfill it.
  - **404 Not found**: The server can’t find the requested resource.
  - **405 Method not allowed**: The method specified in the request is not allowed for the resource.
  - **408 Request timeout**: The server timed out waiting for the request.
  - **429 Too many requests**: The user has sent too many requests in a given amount of time.
  
- 5xx (Server error)
  - **500 Internal server error**: The server encountered an unexpected condition.
  - **501 Not implemented**: The server does not support the functionality required to fulfill the request.
  - **502 Bad gateway**: The server received an invalid response from the upstream server.
  - **503 Service unavailable**: The server is currently unable to handle the request due to temporary overload or scheduled maintenance.
  - **504 Gateway timeout**: The server did not receive a timely response from an upstream server.
  

You can identify error codes from several places during web browsing and site management. Here are the most common areas where you can find these codes:

1. **Web browser**: When an HTTP error occurs, most web browsers display the error code directly in the browser window. For example, the browser will display a “404 Not Found” error if it cannot find a page. Similarly, if there’s a server error, you might see a “500 Internal Server Error”.
2. Developer tools : You can use the network tab in the browser’s developer tools to view detailed information about each HTTP request and response. This includes the status codes for each transaction. To access this:
  - In Chrome, Firefox, or Edge, right-click on the webpage, select “Inspect” or “Inspect Element,” then navigate to the “Network” tab.
  - Reload the page to capture the HTTP traffic and look for the request that corresponds to the error. Clicking on it will display details, including the status code.
  
3. Server logs : Server-side logs are a valuable resource for identifying error codes, especially for codes that might not result in visible changes on the client side, like certain 5xx errors. Access to these logs depends on your hosting environment:
  - For servers like Apache or Nginx, you can typically find logs in directories like /var/log/apache2 or /var/log/nginx.
  - For managed hosting environments, you may need to access these through your hosting control panel.
  - **Please reach out to your hosting provider for further help with this.**
  
4. **Email alerts and monitoring tools**: You can use website monitoring tools to alert you via email or SMS when your site returns specific HTTP error codes. These tools continuously check your site and can provide immediate notifications about problems.

Identifying where to find these error codes is the first step in troubleshooting issues, allowing you to respond promptly and maintain your site’s reliability.

**Note:**This document is meant to serve as a helpful guide for advanced troubleshooting; however, the procedures described are beyond the scope of our [support policy](https://woocommerce.com/support-policy/) and we cannot provide direct assistance with implementing them. If you would like to seek assistance from a qualified WordPress/WooCommerce developer, we highly recommend [Codeable](https://codeable.io/?ref=z4Hnp) or a [Woo Agency Partner](https://woocommerce.com/development-services/).

After you have identified an HTTP error, you can follow these steps troubleshooting steps to find the root cause:

- **Review the error code**: Look up the specific HTTP error code to understand whether the issue is on the client side (4xx errors) or the server side (5xx errors). This will help guide your troubleshooting efforts.
- **Check recent changes**: If you recently updated your website or server settings, review these changes. Sometimes, reverting to the previous configuration can resolve the issue.
- **Inspect server logs**: Access your server logs to find any detailed error messages or clues about what might be causing the issue, especially for 5xx errors.
- **Contact your host**: If the error persists and you’re unable to resolve it yourself, contact your hosting provider. Hosting services often have specific insights into server configurations and network issues that might not be immediately apparent to you. They can provide direct assistance and are crucial in resolving issues that are beyond simple configuration errors.
- **Use monitoring tools**: Consider setting up monitoring tools that can alert you to HTTP errors as they happen. This proactive approach helps in quickly addressing issues that could impact user experience.

