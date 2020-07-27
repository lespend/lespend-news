import requests
from lxml import html

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Article
from lespendnews.settings import MEDIA_URL

def get_covid_info():
    url = 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BD%D0%B4%D0%B5%D0%BC%D0%B8%D1%8F_COVID-19#%D0%A1%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0_%D0%B7%D0%B0%D0%B1%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%BD%D0%B8%D0%B9_%D0%BF%D0%BE_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B0%D0%BC_%D0%B8_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%8F%D0%BC'
    r = requests.get(url)
    tree = html.fromstring(r.text)
    world_cases_info = tree.xpath('//*[@id="covid19-container"]/table/tbody/tr[2]/th[2]/span')[0].text
    russian_cases_info = tree.xpath('//*[@id="covid19-container"]/table/tbody/tr[6]/td[1]/span')[0].text
    return [world_cases_info, russian_cases_info]

class HomeView(TemplateView):
    template_name = 'articles/home.html'

    def get_context_data(self, **kwargs):        
        articles = Article.objects.all()[:5]

        context = super().get_context_data(**kwargs)
        context['articles'] = articles
        context['MEDIA_URL'] = MEDIA_URL
        context['covid_info'] = get_covid_info()
        return context

class ArticleDetailView(TemplateView):
    template_name = 'articles/article.html'

    def get_context_data(self, **kwargs):
        article = Article.objects.get(id=kwargs['id'])
        context = super().get_context_data(**kwargs)
        context['article'] = article
        context['MEDIA_URL'] = MEDIA_URL
        context['covid_info'] = get_covid_info()
        return context

class SearchResultsView(TemplateView):
    template_name = 'articles/search_results.html'

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     objects_list = Article.objects.filter(name__icontains=query)

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        objects_list = Article.objects.filter(title__icontains=query)
        context = super().get_context_data(**kwargs)
        context['articles'] = objects_list
        context['MEDIA_URL'] = MEDIA_URL
        context['covid_info'] = get_covid_info()
        return context