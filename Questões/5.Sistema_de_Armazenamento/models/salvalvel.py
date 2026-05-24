from typing import Protocol, runtime_checkable

@runtime_checkable
class Salvavel(Protocol):
    def salvar(dado)-> None:
        ...
