from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer,UserSerializer

class UserCreate(generics.CreateAPIView):
serializer_class = UserSerializer


from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate


urlpatterns = [
# ...
path("users/", UserCreate.as_view(), name="user_create"),
]
