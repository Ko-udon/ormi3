from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main(request):
    return render(request, 'main/main.html')

@login_required
def notice(request):
    return render(request, 'main/notice.html')
