from django.shortcuts import render,redirect
from .models import Post
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

def memo(request):
  if request.GET.get('q'):
    q = request.GET.get('q')
    db = Post.objects.filter(Q(title__icontains=q) | Q(contents__icontains=q)).distinct()
    context = {
      'db':db,
    }
  else:
    db = Post.objects.all()
    context = {
      'db': db,
  }
  return render(request, 'memo/memo.html', context)


def post(request, pk):
  db = Post.objects.get(pk=pk)
  context = {
    'db':db,
  }
  return render(request, 'memo/post.html',context)

def delete(request, pk):
  print('삭제요청')
  q = Post.objects.get(pk=pk)
  q.delete()
  return redirect('memo')
