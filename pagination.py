from rest_framework.pagination import PageNumberPagination, CursorPagination

class BasicPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_query_param = "page"
    page_size_query_param = "page_size"


class IndustryCursorPagination(CursorPagination):
    page_size = 20
    ordering = "-id"