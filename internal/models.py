from enum import IntEnum

from django.contrib import admin


class ImprovedModelAdmin(admin.ModelAdmin):
    ...


class EnumChoicesBase(IntEnum):
    """Enum was used as choices of Game.status because explicit is better than implicit"""

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
