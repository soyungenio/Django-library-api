from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.author)


class Readers(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    books = models.ManyToManyField(Books, through="Readerbooks")

    def __str__(self):
        return "{}".format(self.first_name)


class Readerbooks(models.Model):
    book = models.ForeignKey('Books', on_delete=models.CASCADE)
    reader = models.ForeignKey('Readers', on_delete=models.CASCADE)

    def __str__(self):
        return ""
