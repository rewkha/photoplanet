from django.http import HttpResponse

def home(request):
    content = '''<html>
<body>
Hello, World!
</body>
</html>'''
    return HttpResponse(content)