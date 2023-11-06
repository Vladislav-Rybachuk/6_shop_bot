from django_project.telegrambot.adminmanage import User, Category, SubCategory, Product, Order, OrderItem
from asqiref.sync import add_user


def select_user(user_id: int):
    user = User.objects.filter(user_id=user_id).first()
    return user
@sync_to_async
def add_user(user_id, full_name, username):
    try:
        return User(user_id=int(user_id), name = full_name, username = username).save()
    except Exception:
        return select_user(int(user_id))

@sync_to_async
def select_all_users():
    users = User.objects.all()
    return users

@sync_to_async
def count_users():
    return User.objects.all().count()


@sync_to_async
def add_product(**kwargs):
    new_product = Product(**kwargs).save()
    return new_product


@sync_to_async
def get_categories() -> list[Product]:
    return Product.objects.distinct("category_name").all()


@sync_to_async
def get_subcategories(category_code) -> list[Product]:
    return Product.objects.distinct("subcategory_name").filter(category_name=category_code).all()


@sync_to_async
def count_products(category_code, subcategory_code=None) -> int:
    if subcategory_code:
        conditions.update(subcategory_code=subcategory_code)

    return Product.objects.filter(**conditions).count()


@sync_to_async
def get_products(category_code, subcategory_code) -> list[Product]:
    return Product.objects.filter(category_code=category_code, subcategory_code=subcategory_code).all()


@sync_to_async
def get_product(product_id) -> Product:
    return Product.objects.filter(id=int(item_id)).first()
