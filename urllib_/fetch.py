# https://docs.python.org/3/howto/urllib2.html
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
print(html)


# If you wish to retrieve a resource via URL and store it in a temporary location,
# you can do so via the shutil.copyfileobj() and tempfile.NamedTemporaryFile() functions:
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass