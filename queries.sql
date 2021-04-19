-- ***************************************************
--  1. simple query with WHERE conditions
-- ***************************************************

-- Select bateriums's ids of aerobic bacterias
SELECT idBacterium FROM Bacterium WHERE OxygenDemand='Aerobic';

-- Select the diseases and their symptoms that causes the bacterium
-- id="123123123"
SELECT NameDisease, Symptoms
FROM Disease
WHERE Bacterium_idBacterium='123123123'

-- ***************************************************
--  2. query using JOIN and WHERE conditions
-- ***************************************************

-- Select bacterium's ids of bacteria whose genome cat. is "plasmid"
SELECT Bacterium.idBacterium
FROM Bacterium
FULL OUTER JOIN Genome ON Bacterium.idBacterium=Genome.Bacterium_idBacterium
WHERE Genome.Category='PLASMID';



-- ***************************************************
--  3. query including subqueries and WHERE conditions
-- ***************************************************

-- Get bacterium's id="123123123" genome length
SELECT SUM(SecLen)
FROM (SELECT LENGTH(Secuence) AS SecLen
      FROM Gen
      WHERE Genome_idGenome='123123123')

-- Select all diseases that cause the coccus bacteria
SELECT NameDisease
FROM Disease
WHERE Bacterium_idBacterium IN (
	SELECT idBacterium
	FROM Bacteria
	WHERE Morphology='Coccus'
)
