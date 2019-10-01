import { Homepage } from './home.po';
import { browser, element, by } from 'protractor';


describe("NAME field for user :", () => {
    let homepage: Homepage;
    const wrongCredentias =
    {
        username: "k",
    }
    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(1000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a input Name field for user', () => {
        homepage.navigateTo();
        expect(homepage.getNameField()).toBeTruthy;
    });
    it('on submit of name field...with valid details ,its submitted', () => {
        homepage.NameCredentials();
        homepage.navigateTo()
    })
    it('on submit of name field...with error it will be notified to user', () => {
        homepage.navigateTo()
        homepage.NameCredentials(wrongCredentias);
    })
})
describe("PASSWORD field for user :", () => {
    let homepage: Homepage;
    const wrongCredentias = {
        password: '11111',
    }
    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(2000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a input Password field for user', () => {
        expect(homepage.getPasswordField()).toBeTruthy();
    });
    it('on submit of password field...with valid detail ,its submitted', () => {
        homepage.navigateTo();
        homepage.PasswordCredentials();
    })
    it('on submit of password field...with error it will be notified to user', () => {
        homepage.navigateTo();
        homepage.PasswordCredentials(wrongCredentias);
        expect(homepage.getErrorMessage()).toEqual('please..fill with password of length 6 to 8 only');
    })
})
describe("CONFIRM PASSWORD field for user :", () => {
    let homepage: Homepage;
    const wrongCredentias ={
        confirm_password: '11111',
    }
    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(2000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a input Confirm Password field for user', () => {
        homepage.navigateTo();
        expect(homepage.getConfirmPasswordField()).toBeTruthy();
    });
    it('on submit of confirm password field...with valid details,its submitted', () => {
        homepage.navigateTo();
        homepage.PasswordCredentials();
        homepage.ConfirmPasswordCredentials();
        homepage.navigateTo();
    })
    it('on submit of confirm password field...with error it will be notified to user', () => {
        homepage.navigateTo();
        homepage.ConfirmPasswordCredentials(wrongCredentias);
        expect(homepage.getcpErrorMessage()).toEqual('please..check password is not matching');
    })
})
describe("Email field for user :", () => {
    let homepage: Homepage;
    const wrongCredentias = {
        email: "wrongemail",
    }
    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(2000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a input email field for user', () => {
        homepage.navigateTo();
        expect(homepage.getEmailField()).toBeTruthy;
    });
    it('on submit of email field...with valid detail, its submitted', () => {
        homepage.navigateTo();
        homepage.EmailCredentials();
    })
    it('on submit of email field...with error it will be notified to user', () => {
        homepage.navigateTo();
        homepage.EmailCredentials(wrongCredentias);
        expect(homepage.getErrorMessage()).toEqual('please..fill with a valid email');
    })
})
describe("Gender field for user :", () => {
    let homepage: Homepage;
    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(2000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a input Gender field for user', () => {
        homepage.navigateTo();
        expect(homepage.getGenderField()).toBeTruthy;
    });
    it("on submit of gender field...without selecting any option ,it will be notified to user", function () {
        homepage.navigateTo();
        homepage.GenderCredendentialsFalse();
        expect(homepage.getgenderErrorMessage()).toEqual('please..select one');
    })
    it("on submit of gender field...with option selected ,its valid", function () {
        homepage.navigateTo();
        homepage.GenderCredendentialsTrue();
    })
})
describe("Country dropdown field for user :", () => {
    let homepage: Homepage;

    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(2000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a input Country field for user', () => {
        homepage.navigateTo();
        expect(homepage.getCountryField()).toBeTruthy;
    });
    it("on submit of country field...without selecting any option ,it will be notified to user", function () {
        homepage.navigateTo();
        homepage.CountyCredentialsFalse();
        expect(homepage.getCountryErrorMessage()).toEqual('please..select one');
    })
    it("on submit of country field...with option selected ,its valid", function () {
        homepage.navigateTo();
        homepage.CountyCredentialsTrue();
    })
})
describe("the FORM submission  for user :", () => {
    let homepage: Homepage;

    beforeEach(() => {
        homepage = new Homepage();
        browser.sleep(2000);
    });
    afterEach(() => {
        browser.sleep(1000);
    })
    it('should display a Submit Button for user', () => {
        homepage.navigateTo();
        expect(homepage.getSubmitButton()).toBeTruthy;
    });
    it("on submit of FORM ..with empty fields or invalid details,it will be notified to user", function () {
        homepage.navigateTo();
        homepage.FormSubmission();
    })
    it("on submit of FORM ..with valid details ,it is submitted successfully ", function () {
        homepage.navigateTo();
        homepage.NameCredentials();
        homepage.PasswordCredentials();
        homepage.ConfirmPasswordCredentials();
        homepage.GenderCredendentialsTrue();
        homepage.EmailCredentials();
        homepage.CountyCredentialsTrue();
        homepage.FormSubmission();

    })
})

















































