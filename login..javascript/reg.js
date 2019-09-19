function check_for_emptyfield(fields) {
    if (document.getElementById(fields).value.length == 0) {
        document.getElementById("warning_" + fields).innerHTML = "field is empty!";
        return true;
    }
}
function toValidateName() {
    var userName = document.registration.username;
    var letters = /^[A-Za-z]+$/;
    if (check_for_emptyfield("username") || !userName.value.match(letters)) {
        document.getElementById("warning_username").innerHTML = "Enter the username with characters only...!";
        return false;
    } else {
        document.getElementById("warning_username").innerHTML = " ";
        return true;
    }
}
function toValidatePassword() {
    var passWord = document.registration.password;
    var passwordLength = passWord.value.length;
    if (check_for_emptyfield("password") || passwordLength <= 5 || passwordLength > 12) {
        document.getElementById("warning_password").innerHTML = "Enter a password of length between 6 to 12...!";
        return false;
    } else {
        document.getElementById("warning_password").innerHTML = " ";
        return true;
    }
}
function toValidateCountry() {
    var UserCountry = document.registration.country;
    if (UserCountry.value == "Default") {
        document.getElementById("warning_select").innerHTML = "select your country...! ";
        return false;
    } else {
        document.getElementById("warning_select").innerHTML = " ";
        return true;
    }
}
function toValidateEmail() {
    var UserEmail = document.registration.email;
    var MailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (check_for_emptyfield("email") || !UserEmail.value.match(MailFormat)) {

        document.getElementById("warning_email").innerHTML = "Enter a valid email address...!";
        return false;
    } else {
        document.getElementById("warning_email").innerHTML = " ";
        return true;
    }
}
function toValidateGender() {
    var option = document.getElementsByName("gender");
    if (!(option[0].checked || option[1].checked)) {
        document.getElementById("warning_gender").innerHTML = "select your gender...!";
        return false;
    }
    else if (((option[0].checked) || (option[1].checked))) {
        document.getElementById("warning_gender").innerHTML = "";
        return true;
    }

}

function on_submit() {
    toValidateName()
    toValidatePassword()
    toValidateCountry()
    toValidateEmail()
    toValidateGender()
    return false;
}






