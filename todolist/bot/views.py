from django.conf import settings
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.client import TgClient
from goals.models import Board, BoardParticipant


class VerificationView(GenericAPIView):
    model = TgUser
    permission_classes = [IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        serializer: TgUserSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tg_user: TgUser = serializer.validated_data["TG_user"]
        tg_user.user = self.request.user
        tg_user.save(update_fields=["user"])
        instance_serializer: TgUserSerializer = self.get_serializer(tg_user)
        board = Board(title="Telegram board")
        board.save()
        board_p = BoardParticipant(board=board, user=tg_user.user)
        board_p.save()
        tg_client = TgClient(settings.BOT_TOKEN)
        tg_client.send_message(tg_user.tg_chat_id, "Вы успешно подтвердили свою личность.")

        return Response(instance_serializer.data)
