from django.db import models

class Product(models.Model):
    CATS = (
        ('jacket', 'Пальто|куртки'),
        ('costume', 'Костюмы'),
        ('pullover', 'Свитера'),
        ('blazer','Блейзеры'),
        ('shirt', 'Рубашки'),
        ('jeans', 'Джинсы'),
        ('trousers', 'Брюки'),
        ('shorts', 'Шорты'),
        ('shoes', 'Обувь'),
        ('bag', 'Сумки|рюкзаки'),
        ('accessories', 'Аксессуары')
    )
    title = models.CharField(verbose_name='Название товара', max_length=128)
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена')
    category = models.CharField(verbose_name='Категория', max_length=128, choices=CATS)
    sale = models.BooleanField(verbose_name='Участие в распродаже')
    new_col = models.BooleanField(verbose_name='Новая коллекция')
    image_path = models.CharField(verbose_name='Путь у изображению товара', max_length=512)
    def __str__(self):
        self.title

class Order(models.Model):
    DELIVERY_TYPES=(('courier', 'курьер'), ('client','самовывоз'))
    PAYMENT_TYPES = (('card', 'карта'), ('cash', 'наличные'))
    order_id = models.IntegerField(verbose_name='Номер заказа')
    name = models.CharField(verbose_name='Имя заказчика', max_length=128)
    phone = models.CharField(verbose_name='Номер телефона заказчика', max_length=128)
    mail = models.CharField(verbose_name='Почта заказчика', max_length=128)
    address = models.CharField(verbose_name='Адресс заказчика', max_length=128, null=True)
    goods = models.TextField(verbose_name='Список с элементами из 2 позиций: \n 1 - id товара \n 2 -  число товаров данного типа')
    price = models.IntegerField(verbose_name='Стоимость заказа')
    delivery = models.CharField(verbose_name='Способ доставки', max_length=128, choices=DELIVERY_TYPES)
    payment = models.CharField(verbose_name='Способ оплаты', max_length=128, choices=PAYMENT_TYPES)
    def __str__(self):
        self.order_id
