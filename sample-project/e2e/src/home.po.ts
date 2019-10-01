import { browser, by, element } from 'protractor';

export class Homepage {
    private credentias = {
        username: 'kavi',
        password: '12345678',
        confirm_password: '12345678',
        email: 'kkk@gmail.com',
    };
    navigateTo() {
        return browser.get('/home');
    }
    FormSubmission() {
        var submit = element(by.id('onsubmit'))
        submit.click();
    }
    NameCredentials(credentias: any = this.credentias) {
        element(by.name("name")).sendKeys(credentias.username);
        element(by.id('onsubmit')).click();
    }
    PasswordCredentials(credentias: any = this.credentias) {
        element(by.id("password")).sendKeys(credentias.password);
        element(by.id('onsubmit')).click();
    }
    ConfirmPasswordCredentials(credentias: any = this.credentias) {
        element(by.id("confirm_password")).sendKeys(credentias.confirm_password);
        element(by.id('onsubmit')).click();
    }
    GenderCredendentialsFalse() {
        var radiobuttonmale = element(by.id('male'));
        var radiobuttonfemale = element(by.id('Female'))
        var submit = element(by.id('onsubmit'))
        submit.click();
        radiobuttonmale.isSelected().then(radiobuttonselected => {
            console.log('MALE radio button selected:', radiobuttonselected)
        })
        radiobuttonfemale.isSelected().then(radiobuttonselected => {
            console.log('FEMALE radio button selected:', radiobuttonselected)
        })
    }
    GenderCredendentialsTrue() {
        var radiobuttonmale = element(by.id('male'));
        var radiobuttonfemale = element(by.id('Female'))
        var submit = element(by.id('onsubmit'))

        radiobuttonmale.click()
        submit.click();
        radiobuttonmale.isSelected().then(radiobuttonselected => {
            console.log('MALE radio button selected:', radiobuttonselected)
        })
        radiobuttonfemale.isSelected().then(radiobuttonselected => {
            console.log('FEMALE radio button selected:', radiobuttonselected)
        })
    }
    EmailCredentials(credentias: any = this.credentias) {
        element(by.id("email")).sendKeys(credentias.email);
        element(by.id('onsubmit')).click();
    }
    CountyCredentialsFalse() {
        var submit = element(by.id('onsubmit'))

        element(by.id("country")).click()
        submit.click();
    }
    CountyCredentialsTrue() {
        var submit = element(by.id('onsubmit'))
        submit.click();
        element.all(by.cssContainingText('option', 'India')).click();
    }
    getErrorMessage() {
        return element(by.id('warn')).getText();
    }
    getcpErrorMessage() {
        return element(by.id('cpwarn')).getText();
    }
    getgenderErrorMessage() {
        return element(by.id('gwarn')).getText();
    }
    getCountryErrorMessage() {
        return element(by.id('swarn')).getText();
    }
    getNameField() {
        return element(by.name("name")).isDisplayed();
    }
    getPasswordField() {
        return element(by.name("password")).isDisplayed();
    }
    getConfirmPasswordField() {
        return element(by.name("confirm_password")).isDisplayed();
    }
    getEmailField() {
        return element(by.name("email")).isDisplayed();
    }
    getGenderField() {
        return element(by.name("GENDER")).isDisplayed();
    }
    getCountryField() {
        return element(by.name("country")).isDisplayed();
    }
    getSubmitButton() {
        return element(by.id("onsubmit")).isDisplayed();
    }
    getResetButton() {
        return element(by.id("onreset")).isDisplayed();
    }
}