from .models import Store, Food
from django.db.models import Count

def load_food(params={}):
    q = Food.objects.filter(active=True)

    kw = params.get('kw')
    if kw:
        q = q.filter(subject__icontains=kw)

    store_id = params.get('Store_id')
    if store_id:
        q = q.filter(Store_id=store_id)
    return q

def count_food_by_cate():
    return Store.objects.annotate(count=Count('food')).values("id", "name", "count").order_by('count')
