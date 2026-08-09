from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import TelegramUser
from .serializers import TelegramUserSerializer


@api_view(['POST'])
def register(request):
    """Регистрация пользователя Telegram через POST /api/register/."""
    telegram_id = request.data.get('telegram_id')

    # Уже зарегистрирован? Отдадим его данные, без ошибки.
    existing = TelegramUser.objects.filter(telegram_id=telegram_id).first()
    if existing:
        return Response(
            {'status': 'already_registered', 'user': TelegramUserSerializer(existing).data},
            status=status.HTTP_200_OK,
        )

    # Новый: сериализатор проверяет данные и сохраняет.
    serializer = TelegramUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        {'status': 'created', 'user': serializer.data},
        status=status.HTTP_201_CREATED,
    )


@api_view(['GET'])
def user_info(request, telegram_id):
    """Данные пользователя по telegram_id: GET /api/user/<telegram_id>/."""
    user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
    if user is None:
        return Response(
            {'error': 'Пользователь не зарегистрирован'},
            status=status.HTTP_404_NOT_FOUND,
        )
    return Response(TelegramUserSerializer(user).data, status=status.HTTP_200_OK)
