function LoginForm(){

    document.getElementById("forms-container").classList.remove('invisible');
    document.getElementById("forms-container").classList.add('visible');
}

function closeForm(){
    document.getElementById("forms-container").classList.remove('visible');
    document.getElementById("forms-container").classList.add('invisible');
}

function openRegistrationForm(){
    document.getElementById("form-container-registration").classList.remove('invisible');
    document.getElementById("form-container-registration").classList.add('visible');

}

function closeRegistrationForm(){
    document.getElementById("form-container-registration").classList.remove('visible');
    document.getElementById("form-container-registration").classList.add('invisible');
    alert('hello!')
    alert(session["UserName"])
}

