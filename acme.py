#!/usr/bin/env python3

import sys
import os
from inwx import domrobot

__author__ = u'Stephan Müller'
__copyright__ = u'2018, Stephan Müller'
__license__ = u'MIT'


API_URL = os.getenv("INWX_API_URL", "https://api.domrobot.com/xmlrpc/")
USER = os.getenv("INWX_USER")
PASSWORD = os.getenv("INWX_PASSWORD")
DEBUG = bool(os.getenv("INWX_DEBUG", False))

inwx_conn = domrobot(API_URL, DEBUG)
inwx_conn.account.login({'lang': 'en', 'user': USER, 'pass': PASSWORD})


def delete_record(domain_name, domain):
    search_params = {
        'domain': domain_name,
        'name': '_acme-challenge.' + domain,
        'type': 'TXT',
    }
    info = inwx_conn.nameserver.info(search_params)
    if 'resData' in info and 'record' in info['resData'] and info['resData']['record']:
        inwx_conn.nameserver.deleteRecord({'id': info['resData']['record'][0]['id']})


def create_record(domain_name, domain, token):
    params = {
        'domain': domain_name,
        'name': '_acme-challenge.' + domain,
        'type': 'TXT',
        'content': token,
        'ttl': 300,
    }
    inwx_conn.nameserver.createRecord(params)


if __name__ == '__main__':

    if len(sys.argv) != 5:
        raise AttributeError("Wrong number of arguments")
    record_name = sys.argv[2]
    token = sys.argv[3]
    domain_name = ".".join(record_name.split(".")[-3:-1])
    domain = ".".join(record_name.split(".")[1:-1])

    if sys.argv[1] == 'present':
        delete_record(domain_name, domain)
        create_record(domain_name, domain, token)

    elif sys.argv[1] == 'cleanup':
        delete_record(domain_name, domain)

    else:
        raise NotImplementedError
