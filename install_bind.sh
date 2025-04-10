#!/bin/bash

# Script d'installation et configuration du service DNS BIND
# Ce script nécessite des privilèges root pour s'exécuter correctement

# Vérification des privilèges root
if [ "$(id -u)" -ne 0 ]; then
    echo "Ce script doit être exécuté en tant que root" >&2
    exit 1
fi

echo "Installation du service BIND..."
apt-get update
apt-get install -y bind9 bind9utils

# Création des répertoires nécessaires s'ils n'existent pas
echo "Création des répertoires nécessaires..."
mkdir -p /etc/bind
mkdir -p /var/lib/bind

# Création du fichier named.conf.local
echo "Création du fichier named.conf.local..."
cat > /etc/bind/named.conf.local << 'EOF'
zone "ns.local" {
        type master;
        file "/var/lib/bind/ns.local";
        allow-update { none; };
        notify yes;
};

zone "27.16.172.in-addr.arpa" {
        type master;
        file "/var/lib/bind/ns.local.rev";
        allow-update { none; };
        notify yes;
};
EOF

# Création du fichier ns.local
echo "Création du fichier ns.local..."
cat > /var/lib/bind/ns.local << 'EOF'
$TTL    604800
@       IN      SOA     ns.local. root.ns.local. (
                     2024120804         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@                       IN      NS      ns1.ns.local.
ns1.ns.local.           IN      A       172.16.27.140
googIe.com.             IN      A       172.16.27.140
EOF

# Création du fichier ns.local.rev
echo "Création du fichier ns.local.rev..."
cat > /var/lib/bind/ns.local.rev << 'EOF'
$TTL    604800
@       IN      SOA     ns.local. root.ns.local. (
                     2024120803         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      ns1.ns.local.
140     IN      PTR     ns1.ns.local.
140     IN      PTR     googIe.com.
EOF

# Attribution des permissions correctes
echo "Attribution des permissions correctes..."
chown -R bind:bind /var/lib/bind
chmod -R 755 /var/lib/bind

# Redémarrage du service BIND
echo "Redémarrage du service BIND..."
systemctl restart bind9

# Vérification du statut du service
echo "Vérification du statut du service BIND..."
systemctl status bind9

echo "Configuration DNS terminée avec succès!"