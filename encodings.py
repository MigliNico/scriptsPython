import base64
Str = "This is string example...wow!!!" 
Str = base64.b64encode(Str.encode("utf-8"))
print ("encoded string",Str)
Str = base64.b64decode(Str.decode("utf-8"))
print ("decoded string",Str)
