from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Group


def group_required(group_names):
    """Декоратор, который проверяет, входит ли пользователь в одну из указанных групп."""

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and (
                user.is_superuser or user.groups.filter(name__in=group_names).exists()
            ):
                return view_func(request, *args, **kwargs)
            else:
                # Если у пользователя нет прав, отправляем его на страницу с ошибкой 403
                raise PermissionDenied

        return wrapper

    return decorator
