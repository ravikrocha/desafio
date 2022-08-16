from typing import List
import pandas as pd


# Classe de dados

from dataclasses import dataclass


@dataclass
class ValuableItem:
    name: str
    profit: float
    cost: float

    @property
    def value_density(self):
        return (
            self.profit / self.cost
        )  # desconsideraremos os casos triviais de custo nulo.


def items_to_table(items: List[ValuableItem]) -> pd.DataFrame:
    records = [
        {"Item": i.name, "Lucro (R$)": i.profit, "Custo (R$)": i.cost} for i in items
    ]
    records.append(
        {
            "Item": "Total",
            "Lucro (R$)": sum(i.profit for i in items),
            "Custo (R$)": sum(i.cost for i in items),
        }
    )
    return pd.DataFrame.from_records(records)


max_cost = 1000000

profits = [410000, 330000, 140000, 250000, 320000, 320000, 90000, 190000]

costs = [470000, 400000, 170000, 270000, 340000, 230000, 50000, 440000]


available_items = [
    ValuableItem(f"Item {i}", v, w) for i, (v, w) in enumerate(zip(profits, costs))
]

items_to_table(available_items)


def greedy(max_cost: float, available_items: List[ValuableItem]) -> List[ValuableItem]:
    """Função que retorna o algoritmo guloso aplicado a uma lista de itens. É a função básica
    que ordena os itens da lista de acordo com a densidade sem nenhuma restrição adicional.

    Args:
        max_cost (float): custo máximo de todos os investimentos
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        List[ValuableItem]: retorna a lista já ordenada.
    """
    chosen_items = []
    sorted_items = sorted(available_items, key=lambda i: i.value_density, reverse=True)
    for item in sorted_items:
        if item.cost <= max_cost:
            chosen_items.append(item)
            max_cost -= item.cost
    return chosen_items


def greedy_with4(
    max_cost: float, available_items: List[ValuableItem]
) -> List[ValuableItem]:
    """Seleciona previamente o item 4 e após isso executa o algoritmo guloso
    com os itens restantes.

    Args:
        max_cost (float): custo máximo de todos os investimentos.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        List[ValuableItem]: retorna a lista já ordenada.
    """
    chosen_items = list(filter(lambda item: item.name == "Item 3", available_items))
    if sum(item.cost for item in chosen_items) <= max_cost:
        for item in chosen_items:
            max_cost -= item.cost
            sorted_items = sorted(
                available_items, key=lambda i: i.value_density, reverse=True
            )
            for item in sorted_items:
                if item.cost <= max_cost:
                    chosen_items.append(item)
                    max_cost -= item.cost
    else:
        []
    return chosen_items


def chosen_itens_contains_2(
    max_cost: float, available_items: List[ValuableItem]
) -> bool:
    """A função retorna True se o item 2 está no algorithmo guloso básico sem as
    restrições.

    Args:
        max_cost (float): custo máximo de todos os investimentos.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        bool: True se o item 2 está na lista que a função greedy retorna.
    """
    for item in greedy(max_cost, available_items):
        if item.name == "Item 1":
            return True
    return False


def chosen_itens_contains_4(
    max_cost: float, available_items: List[ValuableItem]
) -> bool:
    """A função retorna True se o item 4 está no algorithmo guloso básico sem as
    restrições.

    Args:
        max_cost (float): custo máximo de todos os investimentos.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        bool: True se o item 4 está na lista que a função greedy retorna.
    """
    for item in greedy(max_cost, available_items):
        if item.name == "Item 3":
            return True
    return False


def chosen_itens_contains_2_after_4(
    max_cost: float, available_items: List[ValuableItem]
) -> bool:
    """Retorna True se após do item 4 ser adicionado na lista que é
    retornada da função greedy, como primeiro elemento da fila,
    o item 2 também é adicionado posteriormente.

    Args:
        max_cost (float): custo máximo de todos os investimentos.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        bool: True se o item 2 está na lista que a função greedy_with4 retorna.
    """
    for item in greedy_with4(max_cost, available_items):
        if item.name == "Item 1":
            return True
    return False


def greedy_restriction2(
    max_cost: float, available_items: List[ValuableItem]
) -> List[ValuableItem]:
    """Algoritmo levando em conta a segunda restrição.

    Args:
        max_cost (float): custo máximo de todos os investimentos.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        List[ValuableItem]: retorna a lista já ordenada e com a restrição 2 satisfeita.
    """
    available_items_without2 = list(
        filter(lambda item: item.name != "Item 1", available_items)
    )  # variável sem o item 2 da lista
    if chosen_itens_contains_2(max_cost, available_items):
        if chosen_itens_contains_4(max_cost, available_items):
            return greedy(max_cost, available_items)
        else:
            if sum(
                item.profit for item in greedy(max_cost, available_items_without2)
            ) >= sum(item.profit for item in greedy_with4(max_cost, available_items)):
                return greedy(max_cost, available_items_without2)
            else:
                if chosen_itens_contains_2_after_4:
                    return greedy_with4(max_cost, available_items)
                else:
                    return greedy(max_cost, available_items_without2)
    else:
        return greedy(max_cost, available_items)


def greedy_knapsack(
    max_cost: float, available_items: List[ValuableItem]
) -> List[ValuableItem]:
    """Função final do programa. Ela seleciona os melhores investimentos
    sem ultrapassar o valor do custo máximo usando a ordenação com relação
    a densidade. As duas regras de restrição também são satisfeitas.

    Args:
        max_cost (float): custo máximo de todos os investimentos.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        List[ValuableItem]: lista já ordenada respeitando às duas restrições.
    """
    if (  # primeira restrição
        available_items[0].value_density >= available_items[4].value_density
    ):
        return greedy_restriction2(max_cost, available_items[:4] + available_items[5:])
    else:
        return greedy_restriction2(max_cost, available_items[1:])


chosen_items = greedy_knapsack(max_cost, available_items)
items_to_table(chosen_items)
