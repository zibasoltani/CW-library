from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    ISBN = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return f"{self.title}"


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    membership_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book} {self.member}"



