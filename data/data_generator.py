from os import name
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
          "Candida tus Elulota", "Elusimicrobia", "Candidatus Eremiobacteraeota", "Candidatus Fermentibacteria", "Fibrobacteres", "Firmacutes", "Firmicutes", "Fusobacteria", "Gemmatimonadetes", "Candidatus Goldbacteria", "Candidatus Hydrothermota", "Candidatus Kapabacteria", "Kiritimatiellaeota", "Candidatus Krumholzibacteriota", "Candidatus Kryptonia", "Lentisphaerae", "Candidatus Margulisbacteria", "Candidatus Mcinerneyibacteriota", "Candidatus Microgenomates", "Candidatus Modulibacteria", "Nitrospinae", "Nitrospirae", "Candidatus Omnitrophica"]
CLASS = ["Acidimicrobiia", "Actinobacteria",  "Coriobacteriia",
         "Nitriliruptoria", "Rubrobacteria", "Bacteroidia", "Chloroflexi", "Dictyoglomi"]
ORDER = ["Chromatiales", "Chroococcales", "Chroococcidiopsidales", "Clostridiales", "Coprothermobacterales", "Cytophagales", "Saprospirales", "Sphaerobacterales", "Sphingomonadales", "Spirulinales",
         "Synechococcales", "Oceanospirillales", "Oscillatoriales", "Balneolales", "Blastocatellales", "Rhodospirillales", "Rhodothermales", "Halanaerobiales", "Holophagales", "Hyphomicrobiales"]
FAMILY = ["Actinomycetaceae", "Corynebacteriaceae", "Tsukamurellaceae", "Geodermatophilaceae", "Beutenbergiaceae", "Bogoriellaceae", "Brevibacteriaceae", "Cellulomonadaceae", "Dermabacteraceae", "Dermatophilaceae", "Dermacoccaceae", "Intrasporangiaceae", "Jonesiaceae", "Microbacteriaceae", "Micrococcaceae", "Promicromonosporaceae",
          "Rarobacteraceae", "Sanguibacteraceae", "Nocardiopsaceae", "Streptosporangiaceae", "Thermomonosporaceae", "Sphingobacteriaceae", "Saprospiraceae", "Flexibacteraceae", "Flammeovirgaceae", "Crenotrichaceae", "Corynebacteriaceae", "Gordoniaceae", "Mycobacteriaceae", "Nocardiaceae", "Tsukamurellaceae", "Williamsiaceae"]
GENUS = ["Atopobium", "Collinsella", "Coriobacterium", "Cryptobacterium", "Denitrobacterium", "Eggerthella", "Slackia", "Aquifex", "Hydrogenivirga", "Hydrogenobacter", "Hydrogenobaculum", "Thermocrinis",
         "Hydrogenothermus", "Persephonella", "Sulfurihydrogenibium", "Venenivibrio", "Bacteroides", "Acetofilamentum", "Acetomicrobium", "Acetothermus", "Anaerorhabdus", "Megamonas", "Porphyromonas", "Dysgonomonas"]

# DISEASE TABLE
SYMPTOMS = ["anorexia(R63.0)", "weight loss(R63.4)", "cachexia(R64)", "chills and shivering", "convulsions(R56)", "deformity", "discharge", "dizziness / Vertigo(R42)", "fatigue(R53)", "malaise", "asthenia", "hypothermia(T68)", "jaundice(P58, P59, R17)", "muscle weakness(M62.8)", "pyrexia(R50)", "sweats", "swelling", "swollen or painful lymph node(s)(I88, L04, R59.1)", "weight gain(R63.5)", "Cardiovascular", "arrhythmia", "bradycardia(R00.1)", "chest pain(R07)", "claudication", "palpitations(R00.2)", "tachycardia(R00.0)", "dry mouth(R68.2)", "epistaxis(R04.0)", "halitosis", "hearing loss", "nasal discharge", "otalgia(H92.0)", "otorrhea(H92.1)", "sore throat", "toothache", "tinnitus(H93.1)", "trismus", "Gastrointestinal", "abdominal pain(R10)", "bloating(R14)", "belching(R14)", "bleeding:", "Hematemesis", "blood in stool: melena(K92.1), hematochezia", "constipation(K59.0)", "diarrhea(A09, K58, K59.1)", "dysphagia(R13)", "dyspepsia(K30)", "fecal incontinence", "flatulence(R14)", "heartburn", "nausea(R11)", "odynophagia", "proctalgia fugax", "pyrosis(R12)", "Rectal tenesmus", "steatorrhea", "vomiting(R11)", "alopecia", "hirsutism", "hypertrichosis", "nail:", "Skin:", "abrasion", "anasarca(R60.1)", "bleeding into the skin", "petechia", "purpura", "ecchymosis and bruising(Sx0(x=0 through 9))", "blister(T14.0)", "edema(R60)", "itching(L29)", "laceration", "rash(R21)", "urticaria(L50)", "abnormal posturing", "acalculia", "agnosia", "alexia", "amnesia", "anomia", "anosognosia", "aphasia and apraxia", "apraxia", "ataxia", "cataplexy(G47.4)", "confusion", "dysarthria", "dysdiadochokinesia", "dysgraphia", "hallucination",
            "headache(R51)", "hypokinetic movement disorder:", "akinesia", "bradykinesia", "hyperkinetic movement disorder:", "akathisia", "athetosis", "ballismus", "blepharospasm", "chorea", "dystonia", "fasciculation", "muscle cramps(R25.2)", "myoclonus", "opsoclonus", "tic", "tremor", "flapping tremor", "insomnia(F51.0, G47.0)", "loss of consciousness", "Syncope(medicine)(R55)", "neck stiffness", "opisthotonus", "paralysis and paresis", "paresthesia(R20.2)", "prosopagnosia", "somnolence(R40.0)", "abnormal vaginal bleeding", "vaginal bleeding in early pregnancy / miscarriage", "vaginal bleeding in late pregnancy", "amenorrhea", "infertility", "painful intercourse(N94.1)", "pelvic pain", "vaginal discharge", "Ocular", "amaurosis fugax(G45.3) and amaurosis", "blurred vision", "double vision(H53.2)", "exophthalmos(H05.2)", "mydriasis/miosis(H570)", "nystagmus", "Psychiatric", "amusia", "anhedonia", "anxiety", "apathy", "confabulation", "depression", "delusion", "euphoria", "homicidal ideation", "irritability", "mania(F30)", "paranoid ideation", "phobia:", "Main article: list of phobias", "suicidal ideation", "Pulmonary", "apnea and hypopnea", "cough(R05)", "dyspnea(R06.0)", "bradypnea(R06.0) and tachypnea(R06.0)", "orthopnea and platypnea", "trepopnea", "hemoptysis(R04.2)", "pleuritic chest pain", "sputum production(R09.3)", "Rheumatologic", "arthralgia", "back pain", "sciatica", "Urologic", "dysuria(R30.0)", "hematospermia", "hematuria(R31)", "impotence(N48.4)", "polyuria(R35)", "retrograde ejaculation", "strangury", "urethral discharge", "urinary frequency(R35)", "urinary incontinence(R32)", "urinary retention"]
HAS_CURE = ["0", "1"]
DESCRIPTION = ""

NAME_DISEASE = ["Abscess", "Acute Radiation Sickness", "Alzheimer's disease", "Anthrax", "Appendicitis", "Allergy", "Arthritis", "Aseptic meningitis", "Asthma", "Astigmatism", "Atherosclerosis", "Bacterial meningitis", "Beriberi", "Black Death", "Black Fungus", "Botulism", "Breast cancer", "Bronchitis", "Brucellosis", "Bubonic plague", "Bunion", "Boil", "Campylobacter infection", "Cancer", "Candidiasis", "Carbon monoxide poisoning", "Coeliac disease", "Cerebral palsy", "Chagas disease", "Chickenpox", "Chlamydia", "Chlamydia trachomatis", "Cholera", "Chordoma", "Chorea", "Chronic fatigue syndrome", "Circadian rhythm sleep disorder", "Colitis", "Common cold", "Condyloma", "Congestive heart disease", "Coronary heart disease", "COVID-19", "Cowpox", "Crohn's Disease", "Coronavirus", "Dengue Fever", "Diabetes mellitus", "Diphtheria", "Dehydration", "Dysentery", "Ear infection", "Ebola", "Encephalitis", "Emphysema", "Epilepsy", "Erectile dysfunction", "Fibromyalgia", "Foodborne illness", "Gangrene", "Gastroenteritis", "Genital herpes", "GERD", "Goitre", "Gonorrhea", "Heart disease", "Hepatitis A", "Hepatitis B", "Hepatitis C", "Hepatitis D", "Hepatitis E",
                "Histiocytosis(childhood cancer)", "HIV", "Human papillomavirus", "Huntington's disease", "Hypermetropia", "Hyperopia", "Hyperthyroidism", "Hypothyroid", "Hypotonia", "Impetigo", "Infertility", "Influenza", "Interstitial cystitis", "Iritis", "Iron-deficiency anemia", "Irritable bowel syndrome", "Ignious Syndrome", "Intestine ache", "Intestine Gas", "Intestine disease", "Upset Intestine", "Jaundice", "Keloids", "Kuru", "Kwashiorkor", "Kidney stone disease", "Laryngitis", "Lead poisoning", "Legionellosis", "Leishmaniasis", "Leprosy", "Leptospirosis", "Listeriosis", "Leukemia", "Lice", "Loiasis", "Lung cancer", "Lupus erythematosus", "Lyme disease", "Lymphogranuloma venereum", "Lymphoma", "Limbtoosa", "Mad cow disease", "Malaria", "Marburg fever", "Measles", "Melanoma", "Metastatic cancer", "Meniere's disease", "Meningitis", "Migraine", "Mononucleosis", "Multiple myeloma", "Multiple sclerosis", "Mumps", "Muscular dystrophy", "Myasthenia gravis", "Myelitis", "Myoclonus", "Myopia", "Myxedema", "Morquio Syndrome", "Mattticular syndrome", "Mononucleosis", "Neoplasm", "Non-gonococcal urethritis", "Necrotizing Fasciitis", "Night blindness", "Obesity", "Osteoarthritis", "Osteoporosis", "Otitis", "Palindromic rheumatism", "Paratyphoid fever", "Parkinson's disease", "Pelvic inflammatory disease", "Peritonitis", "Periodontal disease", "Pertussis", "Phenylketonuria", "Plague", "Poliomyelitis", "Porphyria", "Progeria", "Prostatitis", "Psittacosis", "Psoriasis", "Pubic lice", "Pulmonary embolism", "Pilia", "pneumonia", "Q fever", "Ques fever", "Rabies", "Repetitive strain injury", "Rheumatic fever", "Rheumatic heart", "Rheumatism", "Rheumatoid arthritis", "Rickets", "Rift Valley fever", "Rocky Mountain spotted fever", "Rubella", "Salmonellosis", "Scabies", "Scarlet fever", "Sciatica", "Scleroderma", "Scrapie", "Scurvy", "Sepsis", "Septicemia", "SARS", "Shigellosis", "Shin splints", "Shingles", "Sickle-cell anemia", "Siderosis", "SIDS", "Silicosis", "Smallpox", "Stevens–Johnson syndrome", "Stomach flu", "Stomach ulcers", "Strabismus", "Strep throat", "Streptococcal infection", "Synovitis", "Syphilis", "Swine influenza", "Schizophrenia", "Stomach Gas", "Stomach Ache", "stomach Disease", "Kids Stomach Ache", "Upset Stomach", "Taeniasis", "Tay-Sachs disease", "Tennis elbow", "Teratoma", "Tetanus", "Thalassaemia", "Thrush", "Thymoma", "Tinnitus", "Tonsillitis", "Tooth decay", "Toxic shock syndrome", "Trichinosis", "Trichomoniasis", "Trisomy", "Tuberculosis", "Tularemia", "Tungiasis", "Typhoid fever", "Typhus", "Tumor", "Ulcerative colitis", "Ulcers", "Uremia", "Urticaria", "Uveitis", "UTI'S", "Varicella", "Varicose veins", "Vasovagal syncope", "Vitiligo", "Von Hippel-Lindau disease", "Viral fever", "Viral meningitis", "Warkany syndrome", "Warts", "Watkins", "Yellow fever", "Yersiniosis"]


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
    taxonom = taxonom.replace('\'', '')[0:150]

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


def generate_disease(specie: str, id_: int) -> str:
    name = specie + " " + choice(NAME_DISEASE).replace("'", "")
    symptoms = ', '.join([choice(SYMPTOMS) for _ in range(randint(1, 8))])
    cure = choice(HAS_CURE)
    desc = f"Some description about the {name} disease caused by {specie}..."

    return f"INSERT INTO `bacterium`.`Disease` (`NameDisease`, `Symptoms`, `HasCure`, `Description`, `Bacterium_idBacterium`) " +\
        f"VALUES ('{name}', '{symptoms}', '{cure}', '{desc}', '{id_}');"


def main():
    bacterium_sql = open("data/bacterium_table.sql", "w")
    taxonomy_sql = open("data/taxonomy_table.sql", "w")
    disease_sql = open("data/disease_table.sql", "w")
    for i in range(NUMBER_OF_ENTRIES):
        bac, specie = generate_bacterium()
        bacterium_sql.write(bac + "\n")
        taxonomy_sql.write(generate_taxonomy(specie) + "\n")
        if randint(0, 1):
            disease_sql.write(generate_disease(specie, i) + "\n")


if __name__ == "__main__":
    main()
