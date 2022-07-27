from graphene import ObjectType,Schema

# from .Types.types import UserType
# from .models import User
from .GraphQLSchema.Queries.UserQueries import QueryUser
class RootQuery(QueryUser,ObjectType):
    pass


schema=Schema(query=RootQuery)