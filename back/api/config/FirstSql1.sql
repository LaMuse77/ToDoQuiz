-- Création de la base de données
CREATE DATABASE quiz;

-- Création de l'utilisateur
CREATE USER quiz_user WITH PASSWORD 'Database123';

-- Configurations recommandées
ALTER ROLE quiz_user SET client_encoding TO 'UTF8';
ALTER ROLE quiz_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE quiz_user SET timezone TO 'UTC';

-- Donner tous les droits à l'utilisateur sur la base
GRANT ALL PRIVILEGES ON DATABASE quiz TO quiz_user;

-- Quitter
\q
