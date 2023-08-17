from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField("عنوان", max_length=100)
    author = models.ForeignKey('Author', verbose_name="نویسنده", on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', verbose_name="ژانر", on_delete=models.CASCADE)
    publishDate = models.DateTimeField("تاریخ انتشاز")
    ISBN = models.CharField("شابک", max_length=20)
    price = models.PositiveSmallIntegerField("قیمت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'کتاب'


class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    class Meta:
        verbose_name_plural = 'نویسنده'


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ژانر'


class LibraryUser(User):
    MEMBERSHIP_TYPE_CHOICES = (
        ('0', 'غیرفعال'),
        ('1', 'عادی'),
        ('2', 'ویژه'),
    )
    membershipType = models.CharField("نوع عضویت", max_length=1, choices=MEMBERSHIP_TYPE_CHOICES, default='0')
    membershipValidityDate = models.DateField("اعتبار عضویت", auto_now_add=True)

    class Meta:
        verbose_name_plural = 'کاربر کتابخانه'


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="کتاب")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    isReturned = models.BooleanField("برگشت شد", default=False)
    borrowDate = models.DateTimeField("تاریخ امانت دادن", auto_now_add=True)
    returnDate = models.DateTimeField("تاریخ برگشت")
    cost = models.PositiveSmallIntegerField("هزینه")

    def __str__(self):
        return f'{self.book} -> {self.user}'

    class Meta:
        verbose_name_plural = 'رزرو'
