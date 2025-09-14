from yapf.yapflib.yapf_api import FormatFile

reformatted_code, encoding, changed = FormatFile("foo.py")

print(str(encoding))
print(str(changed))