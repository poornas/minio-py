from .encrypt import (Cipher, _AES_CBC_PKCS7, _CSE_ALGORITHM, _CSE_IV , _CSE_KEY)
from minio.helpers import read_full
from cryptography.hazmat.primitives.ciphers import algorithms, modes, default_backend
import io, os, bytes
import base64
_ENCRYPT_MODE = True
_DECRYPT_MODE = False
 class AesCbcPkcs7Reader(object):
    def __init_(self, reader, src_buf, dest_buf, encrypt_mode, encryptor):
      self.reader = reader
      self.src_buf = src_buf
      self.dest_buf = dest_buf
      self.encryptor = encryptor
      self.encrypt_mode = encrypt_mode
      
    def Read(self, buf):
      
    
    def Close(self):
        self.reader.Close()



class AesCbcPkcs7(Cipher):
 
  def __init__(self, key):
    self._key = key
 
  def Seal(self, header, reader):
    if not callable(getattr(reader, 'read')):
      raise ValueError(
          'Invalid input data does not implement a callable read() method')
    content_key = read_full(reader,algorithms.AES.block_size * 2)
    iv = os.urandom(algorithms.AES.block_size)
    encrypted_key = self._key.encrypt(content_key)
    aes_cipher = self._cipher(iv)
    header[_CSE_IV] = base64.standard_b64encode(iv)
    header[_CSE_KEY] = base64.standard_b64encode(encrypted_key)
    header[_CSE_ALGORITHM] = _AES_CBC_PKCS7
    return AesCbcPkcs7Reader(reader,io.BytesIO(), io.BytesIO(), _ENCRYPT_MODE, aes_cipher.encryptor())
  
  def Open(self, header, reader):
    if header[_CSE_ALGORITHM] != _AES_CBC_PKCS7:
      raise ValueError("Invalid encryption algorithm")
    iv = base64.standard_b64decode(header[_CSE_IV])
    encrypted_key = base64.standard_b64decode(header[_CSE_KEY])
    content_key = self._key.decrypt(encrypted_key)
    aes_cipher = self._cipher(content_key)
    return AesCbcPkcs7Reader(reader,io.BytesIO(), io.BytesIO(), _DECRYPT_MODE, aes_cipher.decryptor())

  def Overhead(self, size):
    return size + (algorithms.AES.block_size - ( size % algorithms.AES.block_size))
  
  def __str__(self):
    return self._key
  
  def _cipher(self, iv):
        return Cipher(
            algorithms.AES(self._key),
            modes.CBC(iv),
            backend=default_backend()
        )

def pkcs7Unpad(buf, block_size):
  return buf[:-ord(buf[len(buf) - 1:])]
def pkcs7Pad(buf):
  pad = cipher.AES.block_size - len(buf) % cipher.AES.block_size
  return buf + pad * chr(pad)