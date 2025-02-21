addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request))
  })
  
  async function handleRequest(request) {
    // Set the target URL (Telegram API)
    const url = new URL(request.url)
  
    // Check if the request is for a health check or ping service
    if (url.pathname === '/ping') {
      // Return a simple success message
      return new Response('Service is up and running', {
        status: 200,
        headers: { 'Content-Type': 'text/plain' }
      })
    }
  
    // For other paths, forward the request to the Telegram API
    const apiUrl = url.pathname.includes('/proxy/') ? url.pathname.replace('/proxy/', 'https://api.telegram.org/') : `https://api.telegram.org${url.pathname}`;
    
    // Construct the forwarded request
    const init = {
      method: request.method,
      headers: request.headers,
      body: request.method !== 'GET' ? request.body : null, // Send body for non-GET requests
    }
  
    try {
      // Send the request to the Telegram API
      const response = await fetch(apiUrl, init)
  
      // Return the response from the Telegram API
      return new Response(response.body, {
        status: response.status,
        headers: response.headers
      })
    } catch (err) {
      // If there's an error, return a custom error message
      return new Response('Error contacting API' + err.message, { status: 500 })
    }
  }
  