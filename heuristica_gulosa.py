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
        return self.profit / (self.cost + 1e-9)


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
    """Função que resolve o problema da mochila sem nenhuma restrição.
    Ela ordena os itens da lista de acordo com a densidade.

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


def dens_four_greater_two(available_items: List[ValuableItem]):
    """Função que retorna o valor True se a densidade do item 4 é maior que a densidade
    do item 2.

    Args:
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        bool: valor True se a densidade do item 4 é maior que a densidade do item 2.
    """
    for item1 in available_items:
        if item1.name == "Item 3":
            for item2 in available_items:
                if item2.name == "Item 1":
                    if item1.value_density > item2.value_density:
                        return True
                    else:
                        return False
    return None


def cost_ft_le_max(max_cost: float, available_items: List[ValuableItem]):
    """Indica se a soma do custo dos items 2 e 4 são menores ou igual que o custo
     total de todos os investimentos.

    Args:
        max_cost (float): custo máximo.
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        bool: Retorna True se a soma do custo dos itens são menores que o custo total
    """
    for item1 in available_items:
        if item1.name == "Item 3":
            for item2 in available_items:
                if item2.name == "Item 1":
                    if item1.cost + item2.cost <= max_cost:
                        return True
                    else:
                        return False
    return None


def greedy_with4(
    max_cost: float, available_items: List[ValuableItem]
) -> List[ValuableItem]:
    """Seleciona previamente o item 4 e após isso executa o algoritmo guloso
    com os itens restantes.
        Essa função será usada apenas quando necessária. Em alguns momentos, após
    a seleção do item 2 iremos usar essa função para satisfazer a segunda
    restrição do desafio. Note que nem sempre podemos ou devemos adicionar o item 4 de
    forma automática após a seleção do item 2.
        Utilizaremos essa função após os itens com maior densidade serem selecionados
    e após o item 2 ser escolhido. Desse modo, utilizaremos essa função quando as
    seguintes premissas estiverem presentes:

    1.  Após o item 2 ser selecionado, o item 4 deve conseguir entrar na carteira de
    investimento, ou seja, o seu custo ser menor ou igual ao custo restante.
    2. O lucro da carteira com os itens 2 e 4 deve ser maior do que a carteira sem
    esses itens, trocando esses itens por outros mais lucrativos.

    Args:
        max_cost (float): custo máximo
        available_items (List[ValuableItem]): lista representando os investimentos.

    Returns:
        List[ValuableItem]: retorna a lista já ordenada.
    """
    chosen_items = list(filter(lambda item: item.name == "Item 3", available_items))
    for item in chosen_items:
        max_cost -= item.cost
    sorted_items = sorted(available_items, key=lambda i: i.value_density, reverse=True)
    for item in sorted_items:
        if item.cost <= max_cost:
            chosen_items.append(item)
            max_cost -= item.cost
    return chosen_items


def greedy_restriction2(
    max_cost: float, available_items: List[ValuableItem]
) -> List[ValuableItem]:
    """Resolve a segunda restrição. Se o item 2 for selecionado, então o item 4
    também é escolhido caso o lucro deles forem maior que a carteira escolhendo
    outros ao invés de ambos.

    Args:
        max_cost (float): custo máximo.
        available_items (List[ValuableItem]): retorna a lista já ordenada.

    Returns:
        List[ValuableItem]: retorna a lista já ordenada e com a restrição satisfeita.
    """
    available_items_without2 = list(
        filter(
            lambda item: item.name != "Item 1", available_items
        )  # remove o item 2 da lista
    )
    if dens_four_greater_two(available_items):
        return greedy(max_cost, available_items)
    else:
        if cost_ft_le_max(max_cost, available_items):
            if sum(
                item.profit for item in greedy(max_cost, available_items_without2)
            ) >= sum(item.profit for item in greedy_with4(max_cost, available_items)):
                return greedy(max_cost, available_items_without2)
            else:
                return greedy_with4(max_cost, available_items)
        else:
            return greedy(max_cost, available_items_without2)


def greedy_knapsack(
    max_cost: float, available_items: List[ValuableItem]
) -> List[ValuableItem]:
    """Função final do programa. Ela seleciona os melhores investimentos
    sem ultrapassar o valor do custo máximo usando a ordenação com relação
    a densidade. As duas regras de restrição também são satisfeitas.

    Args:
        max_cost (float): custo máximo.
        available_items (List[ValuableItem]): lista representando os investimentos

    Returns:
        List[ValuableItem]: lista já ordenada respeitando às duas restrições.
    """
    if available_items[0].value_density >= available_items[4].value_density:
        return greedy_restriction2(max_cost, available_items[:4] + available_items[5:])
    else:
        return greedy_restriction2(max_cost, available_items[1:])


chosen_items = greedy_knapsack(max_cost, available_items)
items_to_table(chosen_items)
