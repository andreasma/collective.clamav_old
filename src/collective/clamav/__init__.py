# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory
from Products.validation import validation


_ = MessageFactory('collective.clamav')

from collective.clamav.validator import clamavValidator
validation.register(clamavValidator('isVirusFree'))
