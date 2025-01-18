"""To find how much money is needed for a cozy tea party!"""

__author__: str = "730611339"


def main_planner(guests: int) -> None:
    """Compiles the tea, treats, and money needed for a cozy tea party!"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(
                tea_count=tea_bags(people=guests),
                treat_count=int(treats(people=guests)),
            )
        )
    )


def tea_bags(people: int) -> int:
    """Finds how many tea bags are needed"""
    return int(people * 2)


def treats(people: int) -> int:
    """Finds how many treats each guest needs for their tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Evaluates the cost for all treats and tea."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
