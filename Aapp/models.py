from django.db import models

class Joke(models.Model):
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    class Meta:
        ...
        ordering = ['-id']

    def __str__(self):
        return self.title


# class Rating(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
#     # story = models.ForeignKey(Story, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.rating


