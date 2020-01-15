from typing import Generic, TypeVar, TYPE_CHECKING, Type, cast

from django.db import models


_T = TypeVar('_T', bound=models.Model)
_NT = TypeVar('_NT', bound='NukableModel')


class NukableQuerySet(models.QuerySet, Generic[_NT]):
    def nuke(self) -> None:
        self.update(is_nuked=True)


if TYPE_CHECKING:
    class _Manager(models.Manager[_T], Generic[_T]):
        ...
else:
    class _Manager(models.Manager):
        ...


class NukableManager(_Manager, Generic[_NT]):
    queryset_class: Type[NukableQuerySet[_NT]] = NukableQuerySet

    def get_queryset(self) -> 'NukableQuerySet[_NT]':
        return cast(NukableQuerySet[_NT],
                    super().get_queryset().filter(is_nuked=False))


class NukableModel(models.Model, Generic[_T]):
    is_nuked = models.BooleanField(default=False, null=False)

    objects = NukableManager['NukableModel[_T]']()
    all_objects = models.Manager()

    class Meta:
        abstract = True
