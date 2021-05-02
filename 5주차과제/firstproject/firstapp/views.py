from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html")
    # welcome이라는 이름의 함수는 render로 welcome.html 실행
    # request는 그냥 자동 입력

def hello(request):
    userName = request.GET['name']
    return render(request, 'hello.html', {'userName':userName})