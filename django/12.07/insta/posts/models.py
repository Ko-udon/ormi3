from django.db import models
from users.models import User

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  image = models.ImageField(blank=True, upload_to='posts/images/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # 모델의 객체가 어떻게 문자열로 표현될지를 결정할 수 있습니다.
  # 이렇게 하면 객체 반환시 author-pk 값으로 반환합니다.
  def __str__(self):
    return f'{self.author} - {self.pk}'
  
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.post} - {self.pk}'
    

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    # related_name 역참조시 사용하기 위해
    # Like에서 Comment로, Comment에서 Like에 참조하기 위해
    # Comment.likes.all()


    def Meta(self):
        unique_together = ('author', 'post')

    def __str__(self):
        return f'{self.author} - {self.post}'