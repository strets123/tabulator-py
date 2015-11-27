# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from six import add_metaclass
from abc import ABCMeta, abstractmethod


@add_metaclass(ABCMeta)
class API(object):
    """Parser representation.
    """

    # Public

    @abstractmethod
    def __init__(self, **options):
        pass

    @abstractmethod
    def open(self, loader):
        pass

    @abstractmethod
    def close(self):
        pass

    @property
    @abstractmethod
    def closed(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def reset(self):
        pass
