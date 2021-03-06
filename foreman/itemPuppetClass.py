#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Authors:
# @author: David Blaisonneau <david.blaisonneau@orange.com>
# @author: Arnaud Morin <arnaud1.morin@orange.com>

from foreman.item import ForemanItem
from pprint import pprint as pp


class ItemPuppetClass(ForemanItem):
    """
    ItemPuppetClass class
    Represent the content of a foreman PuppetClass as a dict
    """

    objName = 'puppetclasses'
    payloadObj = 'puppetclass'
    objNameSet = 'puppetclasses'


    def __init__(self, api, key,
                 objName, payloadObj,
                 *args, **kwargs):
        ForemanItem.__init__(self, api, key,
                             objName, payloadObj,
                             *args, **kwargs)

    def smartClassParametersList(self):
        return {x['parameter']: x['id'] for x in
                self['smart_class_parameters']}
