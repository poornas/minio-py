from .encrypt import Cipher
class AesCbcPkcs7(Cipher):
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

  class AesCbcPkcs7Reader(object):
    def __init_(self):
      pass
    def Read(self, buf):
      pass
    
    def Close(self):
      pass
