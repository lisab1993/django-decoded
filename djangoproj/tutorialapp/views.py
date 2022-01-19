from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from tutorialapp.serializers import UserSerializer, GroupSerializer, StepSerializer, PageSerializer
from tutorialapp.models import Step, Page


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class StepView(generics.RetrieveAPIView):
    queryset = Step.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = StepSerializer(queryset, many=True)
        return Response(serializer.data)


class PageView(generics.RetrieveAPIView):
    queryset = Page.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PageSerializer(queryset, many=True)
        return Response(serializer.data)

# class StepViewSet(viewsets.ModelViewSet):

#     queryset = Step.objects.all()
#     serializer_class = StepSerializer

# def myview(request):
#     return HttpResponse('myview worked')


# # Create your views here.
# def frontend(request):
#   return HttpResponse(render(request, 'vue_index.html'))
