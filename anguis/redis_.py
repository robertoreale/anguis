#!/usr/bin/env python

# anguis - A generic key-store library

# The MIT License (MIT)
# 
# Copyright (c) 2018-21 Roberto Reale
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from anguis.base import AnguisBase

try:
    from redis.client import Redis
except ModuleNotFoundError:
    print("Please run: pip3 install --upgrade --user redis")

class AnguisRedis(AnguisBase):

    def __init__(self, host='localhost', port=6379, db=0, *args, **kwargs):
        self.r = Redis(host, port, db)
        super(AnguisRedis, self).__init__()

    def __del__(self):
        super(AnguisRedis, self).__del__()

    def __getitem__(self, key):
        return self.unserialize(self.r.get(key))

    def __setitem__(self, key, obj):
        self.r.set(key, self.serialize(obj))

    def __delitem__(self, key):
        return self.r.delete(key)

    def __iter__(self):
        return iter(self.r.keys())

    def __len__(self):
        return len(self.r.keys())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
