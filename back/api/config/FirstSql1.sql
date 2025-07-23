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


---modifiation pour voir les droits de ...

GRANT USAGE, CREATE ON SCHEMA public TO quiz_user;

-- Et optionnellement, pour donner tous les droits actuels et futurs :
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO quiz_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO quiz_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO quiz_user;