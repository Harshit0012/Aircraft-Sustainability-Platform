const listenSignUp = document.getElementById('switchToSignUp');
const accessForm = document.getElementById('access-form');
const signUpField = document.getElementById('signUpfield');
const loginBtn = accessForm.querySelector('button[type="submit"]');

listenSignUp.addEventListener('click', toggleFormFields);

function toggleFormFields(event){
    event.preventDefault();
    
    if (accessForm.classList.contains('sign-up')) {
        // toggle back to login form
        accessForm.classList.remove('sign-up');
        signUpField.innerHTML = '';
        loginBtn.textContent = 'Login';
        listenSignUp.textContent = 'Sign up';
        console.log('login')
        let submitBtn = document.getElementById('formSubmit') 
        submitBtn.setAttribute("class", "l btn btn-primary btn-block")
    } 
    else {
        // toggle to sign-up form
        accessForm.classList.add('sign-up');
        signUpField.innerHTML = `
        <div class="form-group">
            <label for="company">Company</label>
            <input class="form-control" id="company" name="company" placeholder="Enter company name" type="text" autocomplete="off" required>
        </div>
        `;
        loginBtn.textContent = 'Sign up';
        listenSignUp.textContent = 'Login';
        console.log('signup')
        let submitBtn = document.getElementById('formSubmit')
        submitBtn.setAttribute("class", "r btn btn-primary btn-block")

    }
}

const submitForm = document.getElementById('access-form');

submitForm.addEventListener('submit', submitAccessForm)

async function submitAccessForm(event) {
    event.preventDefault();
    
    const form = document.querySelector('#access-form');
    const formData = new FormData(form);
    let checkForm = document.getElementById('formSubmit').attributes[2].value;
    
    let apiUrl = '';
    if (checkForm[0] === 'l') {
      apiUrl = 'http://127.0.0.1:8000/' + formData.get('role') + '/signin';
    } else if (checkForm[0] === 'r') {
      apiUrl = 'http://127.0.0.1:8000/' + formData.get('role') + '/signup';
    }
  
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
          'Content-Type': 'application/json'
        }
      });
  
      if (response.status===200) {
        console.log('Form submitted successfully');
        const data = await response.json();
        form.reset();
  
        if(checkForm[0]==='l'){
          const { token } = data;
          // storing token and operator id for future use in authentication and for other use 
          sessionStorage.setItem('token', token); 
          sessionStorage.setItem('role', formData.get('role')); 

          console.log("foward")
          window.location.href = 'dashboard.html'; // navigate to the operaton page
        }
        else{
          alert(` Sucessfully registered - ${response.status}`);
        }
      } else {
        const errorText = await response.text();
        alert(` ${response.statusText} - ${response.status}`);
        console.log(response.statusText);
        throw new Error('Invalid Credentials');
      }
    } catch (error) {
      console.log('An error occurred while submitting the form:', error);
    }
  }
  

