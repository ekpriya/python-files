// import { AppPage, Homepage } from './app.po';
// import { browser } from 'protractor';


// describe('workspace-project App', () => {
//   let page: AppPage;
//   let homepage: Homepage;

//   beforeEach(() => {
//     page = new AppPage();
//     homepage = new Homepage();
//   });

//   it('should display navigate message', () => {
//     page.navigateTo();
//   });

//   it('should display a title message of the page', () => {
//     expect(page.getPageTitleText()).toEqual('FILL THE FORM');
//   });

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
