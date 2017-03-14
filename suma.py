#!/usr/bin/python3

import webapp
import socket


class sumaApp(webapp.app):
    def process(self, parsedRequest,request):
        """Process the relevant elements of the request.
        Returns the HTTP code for the reply, and an HTML page.
        """
        try:
            recurso = request.split()[1][1:]       
            sumandos = recurso.split('/')[1]
            sumando1, sumando2 = sumandos.split('+')
            suma = int(sumando1) + int(sumando2)
            return ("200 OK", "<html><body><h1>" +
                              "Me estas pidiendo:  " + sumandos +
                              ". Y la suma es:    " + str(suma) +
                              "</h1></body></html>")
        except ValueError:
            return("404 Not found", "<html><body><h1>" +
                              "Argumentos incorrectos" +
                              "</h1></body></html>")

if __name__ == "__main__":
    suma = sumaApp()
    port = 1234
    testWebApp = webapp.webApp("localhost", port, {'/suma': suma})
