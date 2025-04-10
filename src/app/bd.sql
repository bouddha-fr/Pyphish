DROP TABLE IF EXISTS campagne;
DROP TABLE IF EXISTS cible;
DROP TABLE IF EXISTS template_site;
DROP TABLE IF EXISTS utilisateur;


CREATE TABLE utilisateur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE template_site (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE cible (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(100),
    nom VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(255), 
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
    site_id INT,
    FOREIGN KEY (site_id) REFERENCES template_site(id) ON DELETE SET NULL
);

CREATE TABLE campagne (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    date_debut DATETIME DEFAULT CURRENT_TIMESTAMP,
    etat VARCHAR(255) NOT NULL,
    utilisateur_id INT,
    template_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(id) ON DELETE SET NULL,
    FOREIGN KEY (template_id) REFERENCES template_site(id) ON DELETE SET NULL
);

INSERT INTO utilisateur  (email, mot_de_passe) VALUES ("admin@gophish.fr", "admin");
INSERT INTO template_site (nom) VALUES ("google"), ("facebook");
INSERT INTO campagne (nom, date_debut, etat, utilisateur_id, template_id) VALUES
  ('Campagne Phishing 1', '2025-04-01 00:00:00', 'Actif', 1, 1),
  ('Campagne Phishing 2', '2025-03-01 00:00:00', 'Terminé', 1, 1),
  ('Campagne Phishing 3', '2025-04-05 00:00:00', 'Actif', 1, 2),
  ('Campagne Phishing 4', '2025-02-10 00:00:00', 'Terminé', 1, 2);
