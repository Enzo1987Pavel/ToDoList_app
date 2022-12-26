import requests
from django.conf import settings
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bot.models import TgUser
from goals.models import Board

from .serializers import TgUserSerializer
from .tg.client import TgClient


class VerificationView(generics.UpdateAPIView):
    model = TgUser
    serializer_class = TgUserSerializer
    http_method_names = ["patch"]
    permission_classes = [IsAuthenticated]

    # def get_object(self):
    #     return get_object_or_404(TgUser, verification_code=self.request.data["verification_code"])
    def patch(self, request: requests, *args: str, **kwargs: int) -> Response:
        serializer: TgUserSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tg_user: TgUser = serializer.validated_data['tg_user_id']
        tg_user.user = self.request.user
        tg_user.save(update_fields=['user'])
        instance_serializer: TgUserSerializer = self.get_serializer(tg_user)
        board = Board(title='Telegram board')
        board.save()
        # board_p = TgUserSerializer(board=board, user=tg_user.user)
        # board_p.save()
        tg_client = TgClient(settings.BOT_TOKEN)
        tg_client.send_message(tg_user.tg_chat_id, 'Вы успешно подтвердили свою личность.')

        return Response(instance_serializer.data)
