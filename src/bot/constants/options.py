from discord_slash.utils.manage_commands import create_choice

rarity_choices = [
    create_choice(
        name="Poor",
        value="Poor"
    ),
    create_choice(
        name="Common",
        value="Common"
    ),
    create_choice(
        name="Uncommon",
        value="Uncommon"
    ),
    create_choice(
        name="Rare",
        value="Rare"
    ),
    create_choice(
        name="Epic",
        value="Epic"
    ),
    create_choice(
        name="Legendary",
        value="Legendary"
    ),
    create_choice(
        name="Mythical",
        value="Mythical"
    )
]
