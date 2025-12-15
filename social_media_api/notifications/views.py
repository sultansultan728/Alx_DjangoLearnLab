from rest_framework import generics, permissions
from .models import Notification
from rest_framework.response import Response


class NotificationListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(
            recipient=request.user
        ).order_by('-timestamp')

        data = [
            {
                "actor": n.actor.username,
                "verb": n.verb,
                "timestamp": n.timestamp,
                "is_read": n.is_read
            }
            for n in notifications
        ]

        return Response(data)

