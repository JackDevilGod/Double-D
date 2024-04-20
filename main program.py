def main():
    factions: dict = dict()
    entities: list[str] = []

    faction_request_string: str = "faction names or blank to stop \n"
    faction_name: str = input(faction_request_string)

    while faction_name != "":
        factions[faction_name] = None
        faction_name: str = input(faction_request_string)

    entity_request_string: str = "entity name or blank to stop \n"
    entity_name = input(entity_request_string)

    while entity_name != "":
        entities.append(entity_name)

        if input("is in a faction? (YES/NO) \n").lower() == "yes":
            print(factions)
            belong_to = input("faction name \n")
            factions[belong_to] = len(entities) - 1

        entity_name = input(entity_request_string)

    action: str | None = None

    while True:
        print(entities)
        print(factions)

        action = input("select action")


if __name__ == "__main__":
    main()
