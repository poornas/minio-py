from .encrypt import Cipher
class DareHmacSha256(Cipher):
  def __init__(self, key):
    self.key = key
  def Seal(self, headerMap, reader):
    pass
  def Open(self, headerMap, reader):
    pass
  def Overhead(self, size):
    pass
  def __str__(self):
    return self.key