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
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import UnsupportedAlgorithm
class CryptKey(object):
  """
  Key - generic class to encrypt/decrypt a key.
  We use it to encrypt/decrypt content
  """
  def __init__(self, master_key):
    self.master_key = master_key
  def encrypt(self,plainText):
    pass
  def decrypt(self, cipherText):
    pass

class SymmetricKey(CryptKey):
  def encrypt(self, plainText):
    try:
      key_block = Cipher(algorithms.AES(self.master_key), modes.CBC, default_backend())

    except UnsupportedAlgorithm:
      raise ValueError("")
class CBC:
  def Seal(header, reader):
    pass
  
  def Open(header,reader):
    pass

  def Overhead(size):
    pass