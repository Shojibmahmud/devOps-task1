import os
from datetime import datetime

print('Content-Type: text/html')
print()
print('<!DOCTYPE html>')
print('<head>')
print('<title> WellCome</title>')
print('</head>')
print('<body>')
print('<h3>How are you doing</h3>')
print('<p>Date and time:', datetime.now().strftime('%c'), '</p>')
print('<p>IP:', os.environ['REMOTE_ADDR'], '</p>')
print('<p>Http-User-Agent:', os.environ['HTTP_USER_AGENT'], '</p>')
print('</body>')
print('</html>')
