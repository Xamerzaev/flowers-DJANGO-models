from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLES = (
                 ('S', 'Seller'),
                 ('B', 'Buyer'),
                  )
    user_type = models.CharField(max_length=10, choices=USER_ROLES)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return '{} {}'.format(self.user_type, self.username)


class Flowerlot(models.Model):
    kind = models.CharField("Вид цветка", max_length=50)
    shade = models.CharField("Оттенок", max_length=50)
    quantity = models.IntegerField("Количество")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                             related_name='users')
    LOAN_STATUS = (
        ('O', 'отображать'),
        ('F', 'не отображать'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='O',
                              help_text='Отображение лота')

    class Meta:
        verbose_name = 'Экземпляр лота'
        verbose_name_plural = 'Экземпляры лот'

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.kind, self.shade,
                                    self.price, self.quantity)


class Salesman_feedback(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.PROTECT,
                               related_name="author_salesman_comments")
    salesman = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                 related_name="salesman_comments",
                                 blank=True, null=True)
    title = models.CharField("Заголовок", max_length=16)
    body = models.CharField("Отзыв", max_length=250)


class Lot_feedback(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.PROTECT,
                               related_name="author_lot_comments")
    lot = models.ForeignKey(to=Flowerlot, on_delete=models.CASCADE,
                            related_name="lot_comments", blank=True,
                            null=True)
    title = models.CharField("Заголовок", max_length=16)
    body = models.CharField("Отзыв", max_length=250)


class Transactions(models.Model):
    salesman = models.ForeignKey(to=User, on_delete=models.PROTECT,
                                 related_name="salesmans",
                                 blank=True, null=True)
    lot = models.ForeignKey(to=Flowerlot, on_delete=models.PROTECT,
                            related_name="lots", blank=True,
                            null=True)
    buyer = models.ForeignKey(to=User, on_delete=models.PROTECT,
                              related_name="buyers")

    def __str__(self) -> str:
        return '{} {} {}'.format(self.salesman, self.lot, self.buyer)
