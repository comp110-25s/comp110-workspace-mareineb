"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        survive_fish: list[Fish] = []
        survive_bear: list[Bear] = []
        idx: int = 0
        while idx < len(self.fish):
            if self.fish[idx].age <= 3:
                survive_fish.append(self.fish[idx])
            idx += 1
        idx = 0
        while idx < len(self.bears):
            if self.bears[idx].age <= 5:
                survive_bear.append(self.bears[idx])
            idx += 1
        self.fish = survive_fish
        self.bears = survive_bear
        return None

    def remove_fish(self, amount: int):
        idx: int = 0
        self.fish.pop(idx)

    def bears_eating(self):
        idx: int = 0
        while idx < len(self.bears):
            if len(self.fish) >= 5:
                self.remove_fish(3)
                self.bears[idx].eat(3)
            idx += 1
        return None

    def check_hunger(self):
        idx: int = 0
        survive_bears: list[Bear] = []
        while idx < len(self.bears):
            if self.bears[idx].hunger_score > 0:
                survive_bears.append(self.bears[idx])
            idx += 1
        self.bears = survive_bears
        return None

    def repopulate_fish(self):
        num_fish: int = len(self.fish)
        add_fish: int = (num_fish // 2) * 4
        while add_fish > 0:
            self.fish.append(Fish())
            add_fish -= 1
        return None

    def repopulate_bears(self):
        num_bears: int = len(self.bears)
        add_bears: int = num_bears // 2
        while add_bears > 0:
            self.bears.append(Bear())
            add_bears -= 1
        return None

    def view_river(self) -> None:
        x: int = self.day
        y: int = len(self.fish)
        z: int = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")
        print(f"Bear population: {z}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        idx: int = 0
        while idx <= 7:
            self.one_river_day()
            idx += 1
