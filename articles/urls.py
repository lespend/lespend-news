from django.urls import path
from .views import HomeView, ArticleDetailView, SearchResultsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articles/<int:id>', ArticleDetailView.as_view()),
    path('search', SearchResultsView.as_view(), name='search-results')
]