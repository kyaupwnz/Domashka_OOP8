import os

class ChangeDir:

  def __init__(self, _dir):
    self._dir = _dir
    self.current_dir = os.getcwd()
  def __enter__(self):
      os.chdir(self._dir)

  def __exit__(self, exc_type, exc_val, exc_tb):
      os.chdir(self.current_dir)

with ChangeDir('dir1'):
  print(os.listdir())

with ChangeDir('dir2'):
  print(os.listdir())

# вывод в консоль
#['log.txt']
#['file1.py', 'file2.py']
