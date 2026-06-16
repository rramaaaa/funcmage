artifacts = [
        {
            'name': 'Lightning Rod',
            'power': 108,
            'type': 'weapon'
            },
        {
            'name': 'Earth Shield',
            'power': 84,
            'type': 'weapon'
            },
        {
            'name': 'Light Prism',
            'power': 73,
            'type': 'relic'
            },
        {
            'name': 'Wind Cloak',
            'power': 80, 'type': 'relic'
            }
        ]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda x: x["power"])
    return sorted_artifacts


print("Testing artifact sorter...")
artifacts = artifact_sorter(artifacts)
for i in artifacts:
    print(f"{i["name"]} ({i["power"]} power)")
    len_art = len(artifacts)
    if i["name"] != artifacts[len_art - 1]["name"]:
        print("comes before")
print()


mages = [
        {
            'name': 'River',
            'power': 64,
            'element': 'water'
            },
        {
            'name': 'River',
            'power': 89,
            'element': 'light'
            },
        {
            'name': 'Morgan',
            'power': 75,
            'element': 'lightning'
            },
        {
            'name': 'Luna',
            'power': 99,
            'element': 'lightning'
            },
        {
            'name': 'Zara',
            'power': 56,
            'element': 'water'
            }
        ]


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_power = list(filter(lambda x: x["power"] >= min_power, mages))
    return filtered_power


print("Testing power filter...")
powers = power_filter(mages, 80)
for i in powers:
    print(f"{i["name"]} ({i["power"]} power)")

print()

spells = ['earthquake', 'shield', 'meteor', 'fireball']


def spell_transformer(spells: list[str]) -> list[str]:
    transformered_spells = list(map(lambda x: "* " + x + " *", spells))
    return transformered_spells


print("Testing spell transformer...")
spells = spell_transformer(spells)
for i in spells:
    print(i, end=" ")
print()
print()


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    avg_power = round(sum(x["power"] for x in mages) / len(mages), 2)

    stats = {
            "max_power": max_power["power"],
            "min_power": min_power["power"],
            "avg_power": avg_power
            }
    return stats


print("Testing mage stats...")
mages = mage_stats(mages)
print(f"Most power = {mages["max_power"]}")
print(f"Least power = {mages["min_power"]}")
print(f"Average power = {mages["avg_power"]}")
