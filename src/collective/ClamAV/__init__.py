# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory
from Products.validation import validation


_ = MessageFactory('collective.ClamAV')

from collective.ClamAV.validator import ClamAVValidator
validation.register(ClamAVValidator('isVirusFree'))
