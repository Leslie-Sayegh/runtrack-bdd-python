-- sources:
-- https://waytolearnx.com/2019/09/liste-des-commandes-mysql.html?utm_content=cmp-true


-- mysql installation pour windows
-- proccessus d'installation windows
-- https://help.eset.com/protect_install/80/fr-CA/mysql_windows.html
-- https://dev.mysql.com/downloads/installer/

-- Au cas ou on vous demande d'installer microsofts c+++ selon les version de windows
-- installation microsofts c+++
-- https://youtu.be/MhaH7o3lf4E



-- mysql installation mac
-- proccessus d'installation mac
-- https://www.geeksforgeeks.org/how-to-install-mysql-on-macos/

-- https://downloads.mysql.com/archives/community/
-- Pour installer python connector mysql
-- pip3 install mysql-connector-python



-- 1. Pour vous connecter à mysql
mysql -u username -p

-- 1. Pour vous connecter (à partir du shell Unix), utilisez -h uniquement si nécessaire.
[répertoire mysql]/bin/mysql -h hostname -u root -p

-- 2. Pour créez une base de données SQL.
create database [databasename];

-- 3. Pour afficher toutes les bases de données sur le serveur SQL.
show databases;

-- 4. Pour sélectionnez une base de données.
use [database];

-- 5. Pour voir toutes les tables dans une base de données.
show tables;

-- 6. Pour afficher la structure d’une table:
describe [table];

-- 7. Pour supprimer une base de données.
drop database [databasename];

-- 8. Pour supprimer une table.
drop table [tablename];

-- 9. Afficher toutes les données d’une table.
SELECT * FROM [tablename];

-- 10. Renvoie les colonnes et les informations sur des colonnes relatives à une table.
SHOW COLUMNS FROM  [tablename];

-- 11. Déterminez quelle base de données est utilisée:
select database();

-- 12. Pour lister tous les index d’une table:
show index from [table];

-- 13. Créer une nouvelle table avec des colonnes:
CREATE TABLE [tablename] ([colonne1] VARCHAR(50), [colonne2] DATETIME);

-- 14. Pour ajouter une colonne:
ALTER TABLE [tablename] ADD COLUMN [colonne3] VARCHAR(100);

-- 15. Pour ajouter une colonne avec un ID unique par incrémentation automatique:
ALTER TABLE [tablename] ADD COLUMN [colonne4] int NOT NULL AUTO_INCREMENT PRIMARY KEY;

-- 16. Insérer un enregistrement dans une table SQL:
INSERT INTO [tablename] ([colonne1], [colonne2]) VALUES ('[valeur1]', '[valeur2]');

-- 17. Fonction MySQL pour afficher la date actuelle:
NOW()

-- 18. Pour afficher le plan d’exécution d’une requête SQL:
EXPLAIN SELECT * FROM [tablename];

-- 19. Pour sélectionner une parties d’un enregistrement:
SELECT [colonne1], [colonne2] FROM [table];

-- 20. Pour compter le nombre d’enregistrement dans une table.
SELECT COUNT([colonne]) FROM [table];

-- 21. Pour sélectionner des enregistrements spécifiques:
SELECT * FROM [table] WHERE [colonne] = [valeur];

-- D’autre sélecteurs: <, >, !=; pour combiner plusieurs sélecteurs utiliser les opérateurs AND et OR. Exemple:
SELECT * FROM users WHERE name = 'Alex' OR age > 30;

-- 22. Sélectionnez les enregistrements qui contiennent la valeur [val].
SELECT * FROM [table] WHERE [colonne] LIKE '%[val]%';
-- Exemple: Sélectionnez tous les noms qui contiennent ‘al’
SELECT * FROM users WHERE name LIKE '%al%';
-- Sortie:
+--------+-----------+--------+
|  id    |    name   |  age   |
+--------+-----------+--------+
|  101   |   ali     |   25   |
|  102   |  Malis    |   15   |
|  103   |  Mokali   |   35   |
|  104   |  Manali   |   40   |
+--------+-----------+--------+

-- 23. Sélectionnez les enregistrements qui commencent par la valeur [val].
SELECT * FROM [table] WHERE [colonne] LIKE '[val]%';
-- Exemple: Sélectionnez tous les noms commençant par « Yo »
SELECT * FROM users WHERE name LIKE 'Yo%';

-- 24. Sélectionnez les enregistrements commençant par ‘val1’ et se terminant par ‘val2’.
SELECT * FROM [table] WHERE [colonne] LIKE '[val1_val2]';
-- Exemple: Sélectionnez toutes les descriptions commençant par « T » et se terminant par « T »
SELECT * FROM product WHERE description LIKE 'T_T';
-- Sortie:
+--------+---------------+
|  id    |  description  |
+--------+---------------+
|  101   |      TiT      |
|  102   |      ToT      |
|  103   |      TaT      |
|  104   |      TuT      |
+--------+---------------+

-- 25. Sélectionner un intervalle de données.
SELECT * FROM [table] WHERE [colonne] BETWEEN [valeur1] and [valeur2];
-- Exemple:
SELECT * FROM users WHERE age BETWEEN 20 and 30;
-- Sortie:
+--------+-----------+--------+
|  id    |    name   |  age   |
+--------+-----------+--------+
|  115   |   Yohan   |   20   |
|  130   |   Thomas  |   25   |
|  109   |    Jean   |   29   |
|  144   |    Alex   |   21   |
+--------+-----------+--------+

-- 26. Sélectionnez avec un ordre personnalisé et seulement une limite:
SELECT * FROM [table] WHERE [colonne] ORDER BY [colonne] ASC LIMIT [valeur];
-- Ordre: DESC (Descendant) ↓, ASC (ascendant) ↑.
-- Exemple:
SELECT * FROM users ORDER BY age ASC LIMIT 3;
-- Sortie:
+--------+-----------+--------+
|  id    |    name   |  age   |
+--------+-----------+--------+
|  115   |   Yohan   |   20   |
|  130   |   Thomas  |   21   |
|  109   |    Jean   |   25   |
+--------+-----------+--------+

-- 27. Mettre à jour des enregistrements:
UPDATE [table] SET [colonne] = '[new_val]' WHERE [colonne] = '[old_val]';

-- Exemple:
UPDATE [table] SET [colonne] = '[new_val]' WHERE [colonne] = '[old_val]';
-- Exemple:
UPDATE users SET age = '30' WHERE age = '25';

-- 28. Supprimer des enregistrements:
DELETE FROM [table] WHERE [colonne] = [valeur];

-- 29. Supprimer tous les enregistrements d’une table (sans supprimer la table elle-même)
DELETE FROM [table];

-- 30. Supprimer tous les enregistrements d’une table:
truncate table [table];

-- 31. Supprimer les colonnes d’une table:
ALTER TABLE [table] DROP COLUMN [colonne];

-- 32. Supprimer une table:
DROP TABLE [table];

-- 33. Supprimer une base de donnée:
DROP DATABASE [database];

-- 34. Créer un alias pour renommer temporairement une colonne:
SELECT [colonne] AS [col] FROM [table];

-- 35. Exporter un dump de base de données:
SELECT [colonne] AS [col] FROM [table];

-- 35. Exporter un dump de base de données:
mysqldump -u [username] -p [database] > backup.sql

-- 36. Importer un dump de base de données:
mysql -u [username] -p -h localhost [database] < backup.sql

-- 37. Trouvez l’adresse IP de l’hôte Mysql:
SHOW VARIABLES WHERE Variable_name = 'hostname';

-- 38. Faire un SELECT sur plusieurs tables:
SELECT [table1].[colonne], [table2].[colonne] FROM [table1], [table2];

-- 39. Lister tous les utilisateurs:
SELECT User FROM mysql.user;

-- 40. Créer un nouvel utilisateur:
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

-- 41. Accorder un accès complet à l’utilisateur pour * tables:
GRANT ALL PRIVILEGES ON database.* TO 'user'@'localhost';

-- Fonctions d’agrégation

-- 1. Sélectionnez des enregistrements sans doublons:
SELECT distinct nom, adresse FROM employe WHERE nom = "Alex";

-- 2. Calculer la somme des enregistrements:
SELECT SUM([colonne]) FROM [table];

-- 3. Calculer la somme des enregistrements de [col] et grouper par [catégorie]:
SELECT [column], SUM([col]) FROM [table] GROUP BY [catégorie];

-- 4. Récupérer la plus grande valeur dans une colonne.
SELECT MAX([colonne]) FROM [table];

-- 5. Récupérer la plus petite valeur dans une colonne.
SELECT MIN([colonne]) FROM [table];


-- 6. Récupérer la moyenne d’une colonne.
SELECT AVG([colonne]) FROM [table];

-- 7. Récupérer la moyenne arrondie et grouper par [catégorie]:
SELECT [colonne], ROUND(AVG([colonne]), 2) FROM [table] GROUP BY [catégorie];

































