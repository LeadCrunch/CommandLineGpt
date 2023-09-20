# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from abc import abstractmethod


class LlmApi:
    @abstractmethod
    def get_chat_completion(self, messages):
        pass
