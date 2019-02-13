from django.urls import path, re_path
from blog.views import index, hello_times
from blog.views import articles_by_year
from django.urls import register_converter
from blog.converters import FourDigitYearConverter
from blog.converters import SlugUnicodeConverter

register_converter(FourDigitYearConverter, 'year')
register_converter(SlugUnicodeConverter, 'slug_unicode')

app_name = 'blog' # URL Reverse 기능을 할 때, 사용.

urlpatterns = [
    path('hello_times/<int:times>/', hello_times),
    path('articles/<year:year>/', articles_by_year),
    # re_path(r'blog/hello_times/(?P<times>\d+)/$, hello_times),  
    path('', index), 
]
