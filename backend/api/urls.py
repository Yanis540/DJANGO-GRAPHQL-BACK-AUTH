from django.urls import path 
from .views import test 
from graphene_django.views import GraphQLView
from .schema import schema
import logging
logging.getLogger("graphql.execution.utils").setLevel(logging.CRITICAL)
urlpatterns = [
    path('graphql',GraphQLView.as_view(graphiql=True,schema=schema))
]
