/**
 * Script de gestion de l'interface de connexion Google
 * Gère le passage de l'étape email à l'étape mot de passe
 */

document.addEventListener('DOMContentLoaded', function() {
    // Récupération des éléments du DOM
    const nextButton = document.getElementById('next-button');
    const emailStep = document.getElementById('email-step');
    const passwordStep = document.getElementById('password-step');
    const emailInput = document.getElementById('email-input');
    const userEmailDisplay = document.getElementById('user-email-display');
    const loginTitle = document.getElementById('login-title');
    const loginSubtitle = document.getElementById('login-subtitle');
    
    // Ajout de l'écouteur d'événement sur le bouton "Suivant"
    nextButton.addEventListener('click', function() {
      // Vérifier si nous sommes à l'étape email
      if (emailStep.style.display !== 'none') {
        const email = emailInput.value.trim();
        
        if (email) {
          // Sauvegarder l'email et passer à l'étape du mot de passe
          userEmailDisplay.textContent = email;
          
          // Cacher l'étape email et montrer l'étape mot de passe
          emailStep.style.display = 'none';
          passwordStep.style.display = 'block';
          
          // Mettre à jour le titre et sous-titre
          loginSubtitle.textContent = `Bienvenue ${email}`;
          
          // Focus sur le champ mot de passe
          document.getElementById('password-input').focus();
          
          // Changer le texte du bouton pour l'étape suivante
          nextButton.textContent = 'Se connecter';
        } else {
          alert('Veuillez entrer une adresse e-mail');
        }
      } else {
        // Nous sommes à l'étape mot de passe
        const password = document.getElementById('password-input').value;
        
        if (password) {
          // Redirection vers Google.fr après une connexion réussie
          window.location.href = "https://www.google.fr";
        } else {
          alert('Veuillez entrer votre mot de passe');
        }
      }
    });
  
    // Permettre la soumission en appuyant sur Entrée
    emailInput.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        nextButton.click();
      }
    });
  
    document.getElementById('password-input').addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        nextButton.click();
      }
    });
  });