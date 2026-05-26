"""Garden advice program.

Prompts the user for the current season and plant type, then prints
gardening advice based on those inputs.
"""


def get_season_advice(season):
    """Return gardening advice for the given season.

    Args:
        season (str): The current season (e.g. "summer", "winter").

    Returns:
        str: A piece of advice based on the season.
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice for the given plant type.

    Args:
        plant_type (str): The type of plant (e.g. "flower", "vegetable").

    Returns:
        str: A piece of advice based on the plant type.
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Run the garden advice program."""
    # Ask the user for the season and plant type
    season = input("Enter the current season (e.g. summer, winter): ").strip().lower()
    plant_type = (
        input("Enter the plant type (e.g. flower, vegetable): ").strip().lower()
    )

    # Build and print the combined advice
    advice = f"{get_season_advice(season)}\n{get_plant_advice(plant_type)}"
    print(advice)


if __name__ == "__main__":
    main()
