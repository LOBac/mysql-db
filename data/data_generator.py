from random import choice, randint
import pandas as pd

MORPHOLOGIES = ["Coccus", "Bacillus", "Other"]
YEARS = list(range(1650, 2021))
METABOLISM = ["Chemoorganotroph", "Chemolithotroph", "Phototroph"]
MOVEMENT = ["Swimming", "Corkscrew Motility", "Gliding Motility", "Chemotaxis"]
OXY_DEMAND = ["Aerobic", "Anaerobic"]
GRAM = ["0", "1"]
df = pd.read_csv("data/genomes.csv", header=0)
TAXONOM_SPECIES = list(df["Organism Name"])

NUMBER_OF_ENTRIES = 1000


def generate_insert() -> str:
    """generate_insert generates a single one random SQL INSERT statement like
    the following one:

        INSERT INTO `bacterium`.`Bacterium`
        (`Morphology`, `YearOfDiscovery`, `TypeMetabolism`, `Movement`, `OxygenDemand`, `GramStain`, `Taxonomy_Species`)
        VALUES ('A', '0000', 'B', 'C', 'Aerobic', '1', 'D');


    Returns:
        str: INSERT statement
    """
    morphology = choice(MORPHOLOGIES)
    year = choice(YEARS)
    metabolism = choice(METABOLISM)
    movement = choice(MOVEMENT)
    oxy_demand = choice(OXY_DEMAND)
    gram = choice(GRAM)
    taxonom = TAXONOM_SPECIES.pop(randint(0, len(TAXONOM_SPECIES)))
    taxonom = taxonom.replace('\'', '')[0:75]

    return f"INSERT INTO `bacterium`.`Bacterium` (`Morphology`, `YearOfDiscovery`, `TypeMetabolism`, `Movement`, `OxygenDemand`, `GramStain`, `Taxonomy_Species`) " +\
        f"VALUES ('{morphology}','{year}','{metabolism}','{movement}','{oxy_demand}','{gram}','{taxonom}');"


def main():
    with open("data/bacterium_table.sql", "w") as sql:
        for _ in range(NUMBER_OF_ENTRIES):
            sql.write(generate_insert() + "\n")


if __name__ == "__main__":
    main()
