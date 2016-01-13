import datetime
from haystack import indexes
from rtiapp import models
from rtiapp.models import User_profile,RTI_query,RTI_response,Department,State, Tag, Blog
from django.contrib.auth.models import User

class user_index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class RTI_query_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    query = indexes.CharField(model_attr='query_text')   

    def get_model(self):
        return RTI_query

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class RTI_response_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True) 

    def get_model(self):
        return RTI_response

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
        
class Department_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, model_attr='department_name') 

    def get_model(self):
        return Department

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class Topic_Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, model_attr='tag_text') 

    def get_model(self):
        return Tag

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class state_Index(indexes.SearchIndex, indexes.Indexable):
    #this suggests states only based on name and not on capital
    text = indexes.EdgeNgramField(document=True, model_attr='state_name') 

    def get_model(self):
        return State

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class blog_Index(indexes.SearchIndex, indexes.Indexable):
    #this suggests states only based on name and not on capital
    text = indexes.EdgeNgramField(document=True, model_attr='heading') 

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
