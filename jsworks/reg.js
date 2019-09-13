function toValidateName()
{ 
    var userName = document.registration.username;
    var letters = /^[A-Za-z]+$/;   
    if(check_for_emptyfield("username"))
    {
        return false;
    
    }
    else if(!userName.value.match(letters))
    {
        document.getElementById("warning_username").innerHTML = "Username must have  characters only";	
        return false;
    }
    else
    {
        document.getElementById("warning_username").innerHTML =" ";
        return true; 
    }
}




function toValidatePassword()
{
    var passWord = document.registration.password;
    var passwordLength = passWord.value.length;
    
    if(check_for_emptyfield("password"))
    {
        return false;
    }
    else if (passwordLength <= 7 || passwordLength > 12 )
    {
        document.getElementById("warning_password").innerHTML = "password should be of length 12  ";
        return false;
    }
    else{
        document.getElementById("warning_password").innerHTML = " ";
        return true;
    }
}



function check_for_emptyfield(fields)
{
    if(document.getElementById(fields).value.length == 0)
    {
        document.getElementById("warning_" + fields).innerHTML="field is empty";
        return true;
    }  
}



function toValidateCountry()
{
    var UserCountry = document.registration.country;
    if(UserCountry.value == "Default"){
        document.getElementById("select").innerHTML = "select your country ";
        return false;
    }
    else
    {
        document.getElementById("select").innerHTML =" ";
        return true;
    }
}




function toValidateEmail()
{
    var UserEmail = document.registration.email;
    var MailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    
    if(check_for_emptyfield("email"))
    {
        return false;
    }
    else if(UserEmail.value.match(MailFormat))
    {
        document.getElementById("warning_email").innerHTML =" ";
        return true;
    }
    else
    {
        document.getElementById("warning_email").innerHTML = "You have entered an invalid email address!";
        return false;
    }
}



function toValidateGender()
{
    var genderM= document.registration.male;    
    var genderF= document.registration.female; 
    
    
    if(genderM.checked==false && genderF.checked==false )
    {
        
        document.getElementById("gender").innerHTML = " choose one !";
        return false;
    }   else
    {
        document.getElementById("gender").innerHTML =" ";
        return true;
    }
}


