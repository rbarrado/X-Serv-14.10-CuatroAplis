#!/usr/bin/python3

import webapp
import socket


class aleatApp(webapp.app):
    def process(self, parsedRequest,request):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        import random
        numero = random.randint(1,10000)
        return ("200 OK", "<html><body><a href=http://localhost:1234/aleat/" + str(numero) + "'>Dame otra mas</a></body></html>")

if __name__ == "__main__":
    aleatoria = aleatApp()
    port = 1234
    testWebApp = webapp.webApp("localhost", port, {'/aleat': aleatoria})
