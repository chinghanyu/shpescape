#!/usr/bin/env python
#
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models
from django.contrib.gis.geos import Point


class OAuthRequestToken(models.Model):
    """OAuth Request Token."""
    session_key = models.CharField(max_length=250)
    ft_token = models.CharField(max_length=250)
    ft_token_secret = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def is_complete(self):
      if self.ft_token and self.md_token:
        return True

class OAuthAccessToken(models.Model):
    """OAuth Access Token."""
    session_key = models.CharField(max_length=250)
    ft_token = models.CharField(max_length=250)
    ft_token_secret = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def is_complete(self):
      if self.ft_token and self.md_token:
        return True
