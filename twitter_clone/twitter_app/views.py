# from rest_framework import generics,permissions
# from .models import Tweet
# from .serializers import TweetSerializer,ReplySerializer
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsTweetOwner

# class TweetListCreateView(generics.ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#     permission_classes = [IsAuthenticated]
    

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class TweetRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#     permission_classes = [IsAuthenticated, IsTweetOwner]                           


# class ReplyCreateView(generics.CreateAPIView):
#     serializer_class = ReplySerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         tweet_id = self.kwargs.get('tweet_id')
#         tweet = Tweet.objects.get(id=tweet_id)
#         serializer.save(user=self.request.user,tweet=tweet)