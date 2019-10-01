import { AppPage } from './app.po';
import { browser, element, by } from 'protractor';
import { Homepage } from './home.po';




describe("Title message :", () => {
    let appPage: AppPage;
   
    beforeEach(() => {
        appPage = new  AppPage();
    });
   it("should display title message of the page",()=>{
       appPage.navigateTo()
    expect(appPage.getPageTitleText1()).toEqual('Welcome to sample-project!');
   })
})





































































// describe('workspace-project App', () => {
//   let page: AppPage;

//   beforeEach(() => {
//     page = new AppPage();
//   });

//   it('should display navigate message', () => {
//     page.navigateTo();
//   });

//   it('should display a h1 tag message of the page', () => {
//     expect(page.getPageTitleText()).toEqual('Welcome to sample-project!');
//   });
// })




//   it('should display a title message of the home page', () => {
//     expect(homepage.getPageTitleText()).toEqual(':form:');
//   });
//   it('Should check email validation by clicking Subscribe Button', () => {
//     browser.waitForAngularEnabled(false);
//     browser.driver.sleep(500);
//     homepage.getSubmitButton().click();
//     expect(homepage.getErrorMessage()).toMatch('Email is required!');
//     browser.driver.sleep(2000);

//     homepage.getEmailElement().sendKeys('test')
//     homepage.getSubmitButton().click();
//     expect(homepage.getErrorMessage()).toMatch('please..fill with avalid email');
//     browser.driver.sleep(2000);

//     homepage.getEmailElement().clear();
//     browser.driver.sleep(500);
//     homepage.getEmailElement().sendKeys('test@test.com');
//     homepage.getSubmitButton().click();
//     expect(homepage.getResponseMessage()).toBeDefined();
//     browser.driver.sleep(5000);
// });
// });

// })
