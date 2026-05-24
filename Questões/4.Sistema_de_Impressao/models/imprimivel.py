from typing import Protocol


class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...




def processarImpressao(Item: Imprimivel) -> None:
    Item.imprimir()
