#!/usr/bin/env python

import httplib;
import json;

class Typekit():

    def __init__(self, id, token):
        self.id = id;
        self.token = token;
        self.endpoint = 'typekit.com';

    ##
    # Create a secure connection.
    #
    # @return HTTPSConnection
    ##
    def connection(self):
        return httplib.HTTPSConnection(self.endpoint);

    ##
    # Build required request headers.
    #
    # @return object
    ##
    def headers(self):
        return {
            'X-Typekit-Token': self.token
        };

    ##
    # Build params required for updating a kit.
    #
    # @param array domains
    #
    # @return string
    ##
    def params(self, domains):
        return 'domains=' + ','.join(domains)

    ##
    # Using the connection, make a request to the API using the correct endpoint.
    #
    # @param string method
    # @param string endpoint
    # @param string body
    #
    # @return bool|object
    ##
    def request(self, method, endpoint, body = ''):
        try :
            conn = self.connection();
            conn.request(method, endpoint, body, self.headers());
            response = conn.getresponse();
            if response.status != 200:
                return False;
            else:
                return json.loads(
                    response.read()
                );
        finally:
            conn.close();

    ##
    # Fetch a single kit using an id.
    #
    # @return bool|array
    ##
    def kit(self):
        response = self.request('GET', '/api/v1/json/kits/' + self.id);
        return response['kit'] if response else False;

    ##
    # Add domains to a single kit.
    #
    # @param array domains
    #
    # @return bool
    ##
    def add(self, domains):
        response = self.request('POST', '/api/v1/json/kits/' + self.id, self.params(domains));
        return True if response else False;

    ##
    # Publish a single kit.
    #
    # @return bool
    ##
    def publish(self):
        response = self.request('POST', '/api/v1/json/kits/' + self.id + '/publish');
        return True if response else False;
