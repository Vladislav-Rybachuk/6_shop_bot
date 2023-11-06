from django.db import models

class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBasedModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(unique=True,default=1, verbose_name="ID Пользователя Telegram")
    name = models.CharField(max_length=100, verbose_name="Имя Пользователя Telegram")
    username = models.CharField(max_length=100, verbose_name="Username Telegram")
    email = models.CharField(max_length=100, verbose_name="Email", null=True)

    def __str__(self):
        return f"№{self.id} ({self.user_id} - {self.name})"


class Category(TimeBasedModel):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    title = models.CharField(max_length=255, verbose_name="Название Категории")

    def __str__(self):
        return self.title


class SubCategory(TimeBasedModel):
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название Подкатегории")

    def __str__(self):
        return self.title


class Product(TimeBasedModel):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название Товара")
    description = models.TextField(verbose_name="Описание Товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена Товара")
    available = models.BooleanField(default=True, verbose_name="Доступность")

    def __str__(self):
        return self.title


class Order(TimeBasedModel):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая Цена")
    is_processed = models.BooleanField(default=False, verbose_name="Обработан")
    quantity = models.IntegerField(verbose_name="Количество")
    order_time = models.DateTimeField(auto_now_add=True, verbose_name="Время заказа")
    shipping_address= JSONField(null=True, verbose_name="Адрес доставки")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.CharField(max_length=100, verbose_name="Email", null=True)
    receiver = models.CharField(max_length=100, verbose_name="Имя получателя")
    successful  = models.BooleanField(default=False, verbose_name="Оплачено")

    def __str__(self):
        return f"Заказ №{self.id} на {self.quantity}шт. от {self.user}"


class OrderItem(models.Model):
    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"
