import logging

from typing import Any

POSSIBLE_VARIANTS = {
    'paper', 'stone', 'cut'
}


class GameEngine:

    @staticmethod
    def reason(first_figure: str, second_figure: str) -> Any[str, None]:
        if first_figure not in POSSIBLE_VARIANTS and second_figure not in POSSIBLE_VARIANTS:
            logging.warning(f'{first_figure} or {second_figure} not possible')
            return None
        if first_figure == second_figure:
            return 'draw'
        if {first_figure, second_figure} == {'paper', 'stone'}:
            return 'paper'
        if {first_figure, second_figure} == {'cut', 'stone'}:
            return 'stone'
        if {first_figure, second_figure} == {'paper', 'cut'}:
            return 'cut'
