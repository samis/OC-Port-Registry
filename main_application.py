#!/usr/bin/env python
# coding: utf-8
#
# Copyright 2010 Alexandre Fiori
# based on the original Tornado by Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys
import os
from cyclone.bottle import run, route

"""This file contains the main application code for this web application"""


def add_fork_ribbon(web):
    web.write("<link rel=\"stylesheet\" href=\"//cdnjs.buttflare.com/ajax/libs/github-fork-ribbon-css/0.1.1/gh-fork-ribbon.min.css\" />")
    web.write("<div class=\"github-fork-ribbon-wrapper right\">\
        <div class=\"github-fork-ribbon\">\
            <a href=\"https://github.com/simonwhitaker/github-fork-ribbon-css\">Fork me on GitHub</a>\
        </div>\
    </div>")

@route("/")
def index(web):
    add_fork_ribbon(web)
    web.write("<p>Hello, world</p>")

run(host="0.0.0.0", port=int(os.environ['PORT']), log=sys.stdout)
