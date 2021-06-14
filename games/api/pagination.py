from rest_framework.pagination import PageNumberPagination


# custom pagination class
class SmallPagination(PageNumberPagination):
    page_size = 40