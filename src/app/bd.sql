DROP TABLE IF EXISTS utilisateur;
DROP TABLE IF EXISTS template_site;
DROP TABLE IF EXISTS cible;
DROP TABLE IF EXISTS campagne;


-- Table des utilisateurs de la plateforme (admin, formateurs)
CREATE TABLE utilisateur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') NOT NULL,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table des templates de sites de phishing
CREATE TABLE template_site (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    url_redirection VARCHAR(255)
);

CREATE TABLE cible (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(100),
    nom VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255), 
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
    site_id INT,
    FOREIGN KEY (site_id) REFERENCES template_site(id) ON DELETE SET NULL
);
-- Table des campagnes
CREATE TABLE campagne (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    date_lancement DATETIME DEFAULT CURRENT_TIMESTAMP,
    utilisateur_id INT,
    template_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateur(id) ON DELETE SET NULL,
    FOREIGN KEY (template_id) REFERENCES template_site(id) ON DELETE SET NULL
);
