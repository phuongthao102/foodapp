from rest_framework.pagination import PageNumberPagination


class FoodPaginator(PageNumberPagination):
    page_size = 2