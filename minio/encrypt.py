# -*- coding: utf-8 -*-
# Minio Python Library for Amazon S3 Compatible Cloud Storage, (C)
# 2015, 2016, 2017 Minio, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
minio.helpers

This module implements all helper functions.

:copyright: (c) 2015, 2016, 2017 by Minio, Inc.
:license: Apache 2.0, see LICENSE for more details.

"""

from __future__ import absolute_import
import io

import collections
import base64
import hashlib
import re
import os
import errno
import math

from .compat import (urlsplit, urlencode, queryencode,
                     str, bytes, basestring)
from .error import (InvalidBucketError, InvalidEndpointError,
                    InvalidArgumentError)

# Constants
