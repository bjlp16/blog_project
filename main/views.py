from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def main(request):
	'''
	render the main page
	'''
	
	#原本的html str 移到 template/main/main.html
	'''
	htmlStr = 
	<html>
	<head>
	<title>部落格</title>
	<meta charset='utf-8'>
	</head>
	<body>
	<p>這是html字串的hello world</p>
	</body>
	</html>	
	'''
	#return HttpResponse(htmlStr)
	#return HttpResponse('hello world(this is main/views.py)')
	
	context = {'like':'Django棒棒der'}
	return render(request, 'main/main.html', context)
	
def about(request):
	'''
	render the about page
	'''
	context2 = {'like':'Django呵呵der'}
	return render(request, 'main/about.html', context2)


