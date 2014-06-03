#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# server.py — this file is part of minipaas, a tiny platform as a service.
# Copyright 2014 Kuno Woudt <kuno@frob.nl>
#
# minipaas is licensed under copyleft-next version 0.3.0, see
# LICENSE.txt for more information.
#

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import redis
import pystache
import codecs
from os import path
from flask import Flask, request

app_name = 'autoincrement'
application = Flask (app_name)

template_file = path.join (path.dirname(__file__), 'index.html')

@application.route ('/', methods=['GET', 'POST'])
def index():

    redis_host = os.environ['REDIS_PORT_6379_TCP_ADDR']
    redis_port = os.environ['REDIS_PORT_6379_TCP_PORT']

    r = redis.StrictRedis (host=redis_host, port=redis_port, db=0)
    if request.method == 'POST':
        r.incr (app_name)

    data = { 'value': r.get (app_name) }
    template = codecs.open (template_file, 'rb', 'utf-8').read ()

    return pystache.render (template, data)

if __name__ == "__main__":
    application.run()
