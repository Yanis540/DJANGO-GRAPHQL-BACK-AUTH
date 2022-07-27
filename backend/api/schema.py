from graphene import ObjectType,Schema

# from .Types.types import UserType
# from .models import User
from .GraphQLSchema.Queries.UserQueries import QueryUser
from .GraphQLSchema.Mutations.UserMutations import UserMutation
class RootQuery(QueryUser,ObjectType):
    pass

class RootMutation(UserMutation,ObjectType):
    pass 

schema=Schema(query=RootQuery,mutation=RootMutation)