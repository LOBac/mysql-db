from random import choice, randint
from typing import ClassVar, Tuple
import pandas as pd

NUMBER_OF_ENTRIES = 1000

# BACTERIUM TABLE
MORPHOLOGIES = ["Coccus", "Bacillus", "Other"]
YEARS = list(range(1650, 2021))
METABOLISM = ["Chemoorganotroph", "Chemolithotroph", "Phototroph"]
MOVEMENT = ["Swimming", "Corkscrew Motility", "Gliding Motility", "Chemotaxis"]
OXY_DEMAND = ["Aerobic", "Anaerobic"]
GRAM = ["0", "1"]
df = pd.read_csv("data/genomes.csv", header=0)
TAXONOM_SPECIES = list(df["Organism Name"])

# TAXONOMY TABLE
"Acidobacteria"
PHYLUM = ["Abditibacteriota", "Actinobacteria", "Candidatus Aminicenantes", "Aquificae", "Armatimonadetes", "Candidatus Atribacteria", "Bacteroidetes", "Balneolaeota", "Candidatus Binatota", "Candidatus Bipolaricaulota", "Caldiserica", "Calditrichaeota", "Chlamydiae", "Chlorobi", "Chloroflexi" "Chrysiogenetes", "Candidatus Cloacimonetes", "Coprothermobacterota", "Candidatus Cryosericota", "Cyanobacteria", "Deferribacteres", "Deinococcus-Thermus", "Candidatus Dependentiae", "Dictyoglomi", "Candidatus Dormibacteraeota",
          "Candidatus Elulota", "Elusimicrobia", "Candidatus Eremiobacteraeota", "Candidatus Fermentibacteria", "Fibrobacteres", "Firmacutes", "Firmicutes", "Fusobacteria", "Gemmatimonadetes", "Candidatus Goldbacteria", "Candidatus Hydrothermota", "Candidatus Kapabacteria", "Kiritimatiellaeota", "Candidatus Krumholzibacteriota", "Candidatus Kryptonia", "Lentisphaerae", "Candidatus Margulisbacteria", "Candidatus Mcinerneyibacteriota", "Candidatus Microgenomates", "Candidatus Modulibacteria", "Nitrospinae", "Nitrospirae", "Candidatus Omnitrophica"]
CLASS = ["Acidimicrobiia", "Actinobacteria",  "Coriobacteriia",
         "Nitriliruptoria", "Rubrobacteria", "Bacteroidia", "Chloroflexi", "Dictyoglomi"]
ORDER = ["Chromatiales", "Chroococcales", "Chroococcidiopsidales", "Clostridiales", "Coprothermobacterales", "Cytophagales", "Saprospirales", "Sphaerobacterales", "Sphingomonadales", "Spirulinales",
         "Synechococcales", "Oceanospirillales", "Oscillatoriales", "Balneolales", "Blastocatellales", "Rhodospirillales", "Rhodothermales", "Halanaerobiales", "Holophagales", "Hyphomicrobiales"]
FAMILY = ["Actinomycetaceae", "Corynebacteriaceae", "Tsukamurellaceae", "Geodermatophilaceae", "Beutenbergiaceae", "Bogoriellaceae", "Brevibacteriaceae", "Cellulomonadaceae", "Dermabacteraceae", "Dermatophilaceae", "Dermacoccaceae", "Intrasporangiaceae", "Jonesiaceae", "Microbacteriaceae", "Micrococcaceae", "Promicromonosporaceae",
          "Rarobacteraceae", "Sanguibacteraceae", "Nocardiopsaceae", "Streptosporangiaceae", "Thermomonosporaceae", "Sphingobacteriaceae", "Saprospiraceae", "Flexibacteraceae", "Flammeovirgaceae", "Crenotrichaceae", "Corynebacteriaceae", "Gordoniaceae", "Mycobacteriaceae", "Nocardiaceae", "Tsukamurellaceae", "Williamsiaceae"]
GENUS = ["Atopobium", "Collinsella", "Coriobacterium", "Cryptobacterium", "Denitrobacterium", "Eggerthella", "Slackia", "Aquifex", "Hydrogenivirga", "Hydrogenobacter", "Hydrogenobaculum", "Thermocrinis",
         "Hydrogenothermus", "Persephonella", "Sulfurihydrogenibium", "Venenivibrio", "Bacteroides", "Acetofilamentum", "Acetomicrobium", "Acetothermus", "Anaerorhabdus", "Megamonas", "Porphyromonas", "Dysgonomonas"]


def generate_bacterium() -> Tuple[str, str]:
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

    statement = f"INSERT INTO `bacterium`.`Bacterium` (`Morphology`, `YearOfDiscovery`, `TypeMetabolism`, `Movement`, `OxygenDemand`, `GramStain`, `Taxonomy_Species`) " +\
        f"VALUES ('{morphology}','{year}','{metabolism}','{movement}','{oxy_demand}','{gram}','{taxonom}');"

    return (statement, taxonom)


def generate_taxonomy(specie: str) -> str:
    phylum = choice(PHYLUM)
    class_ = choice(CLASS)
    order = choice(ORDER)
    family = choice(FAMILY)
    genus = choice(GENUS)

    return f"INSERT INTO `bacterium`.`Taxonomy` (`Phylum`, `Class`, `Order`, `Family`, `Genus`, `Species`) " +\
        f"VALUES ('{phylum}','{class_}','{order}','{family}','{genus}','{specie}');"


def main():
    bacterium_sql = open("data/bacterium_table.sql", "w")
    taxonomy_sql = open("data/taxonomy_table.sql", "w")
    for _ in range(NUMBER_OF_ENTRIES):
        bac, specie = generate_bacterium()
        bacterium_sql.write(bac + "\n")
        taxonomy_sql.write(generate_taxonomy(specie) + "\n")


if __name__ == "__main__":
    main()
