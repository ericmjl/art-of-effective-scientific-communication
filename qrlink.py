"""
Author: Eric J. Ma
Date: 29 December 2016
"""

import pyqrcode as pq

code = pq.create('https://ericmjl.github.io/art-of-effective-scientific-communication/')
code.svg('figures/slides-qr.svg')
