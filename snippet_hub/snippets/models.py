from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    code = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    tags = models.ManyToManyField("Tag")
    copy_count = models.PositiveBigIntegerField(default=0)

    # class Meta:
    #     ordering = ['created']

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

# class Comment(models.Model):
#     text = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     creator = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
#     snippet = models.ForeignKey(Snippet, related_name='comments', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.text