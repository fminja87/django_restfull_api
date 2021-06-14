from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from .serializers import StorySerializer
from .models import Story


# Create your views here.


class StoryAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = StorySerializer
    queryset = Story.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return  self.destroy(request, id)
