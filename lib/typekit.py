#!/usr/bin/env python

import httplib;
import json;

class Typekit():

    def __init__(self, id, token):
        self.id = id;
        self.token = token;
        self.endpoint = 'typekit.com';

    def connection(self):
        return httplib.HTTPSConnection(self.endpoint);

    def headers(self):
        return {
            'X-Typekit-Token': self.token
        };

    def params(self, domains):
        return 'domains=' + ','.join(domains)

    def request(self, method, endpoint, body = ''):
        try :
            conn = self.connection();
            conn.request(method, endpoint, body, self.headers());
            response = conn.getresponse();
            if response.status != 200:
                return False;
            return json.loads(
                response.read()
            );
        finally:
            conn.close();

    def kit(self):
        return self.request(
            'GET',
            '/api/v1/json/kits/' + self.id
        );

    def add(self, domains):
        return self.request(
            'POST',
            '/api/v1/json/kits/' + self.id,
            self.params(domains)
        );

    def publish(self):
        return self.request(
            'POST',
            '/api/v1/json/kits/' + self.id + '/publish'
        );
