from typing import List

from observerInterfaces import Observer, Subject


class Clerk(Subject):
    _managers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._managers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._managers.remove(observer)

    def notify(self) -> None:
        for observer in self._managers:
            observer.update(self)
