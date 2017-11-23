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
minio.encrypt

This module implements all helper functions.

:copyright: (c) 2017 by Minio, Inc.
:license: Apache 2.0, see LICENSE for more details.

"""

from __future__ import absolute_import
from .keys import SymmetricKey
from .cbc import AesCbcPkcs7
# _AES_CBC_PKCS7 specifies the client-side-encryption algorithm AES-CBC with
# PKCS7 padding. This algorithm is implemented for AWS compability but is
# not recommended because of security issues.
_AES_CBC_PKCS7 = "AES/CBC/PKCS7"

# AWS client-side-encryption headers.
# See: https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html
_CSE_IV = "X-Amz-Meta-X-Amz-Iv"
_CSE_KEY = "X-Amz-Meta-X-Amz-Key-v2"
_CSE_ALGORITHM = "X-Amz-Meta-X-Amz-Cek-Alg"


class Cipher(object):
    """
    Cipher is a generic class for en/decrypting streams using S3
    client/server side encryption. It adds HTTP headers to the provided
    header if needed.
    """
    def __init(self, algorithm, key):
        self._key = key
        self._algorithm = algorithm
        self._cipher = None
        try:
            if algorithm == _AES_CBC_PKCS7:
                self._cipher = AesCbcPkcs7(key)
        except:
            raise ValueError("algorithm %s is not supported" % algorithm)
    def Seal(self,header, src):
        pass
    def Open(self, header, src):
        
        pass
    def Overhead(self, size):
        """
        Overhead returns the size of an encrypted stream with the provided
        size. The size of an encrypted stream is usually larger than an 
        unencrypted one.
        """
        pass    