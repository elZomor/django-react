from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from apps.visitors.models import Event, Click
from apps.visitors.serializers.event_serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ClickViewSet(viewsets.ViewSet):
    queryset = Click.objects.all()

    @action(detail=False, methods=['POST'])
    def add_click(self, request, *args, **kwargs):
        event_id = request.data.get('id')
        event = Event.objects.filter(id=event_id).last()
        click = Click.objects.create(event=event)
        click.save()
        return Response({"code": "Success"}, status=status.HTTP_200_OK)


def index(request):
    return render(request, 'index.html')