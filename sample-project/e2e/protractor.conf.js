// Protractor configuration file, see link for more information
// https://github.com/angular/protractor/blob/master/lib/config.ts

const { SpecReporter } = require('jasmine-spec-reporter');

exports.config = {
  allScriptsTimeout: 11000,

  specs: [
    './src/**/*.e2e-spec.ts'
  ],
  capabilities: {
    'browserName': 'chrome',
  },
  //   capabilities: { browserName: 'chrome', 
  //   chromeOptions: { args: [ "--headless", "--disable-gpu", "--window-size=800,600"] 
  // }
  //  },

  directConnect: true,
  baseUrl: 'http://localhost:4200/',
  framework: 'jasmine',
  jasmineNodeOpts: {
    showColors: true,
    defaultTimeoutInterval: 30000,
    print: function () { }
  },
  onPrepare() {
    require('ts-node').register({
      project: require('path').join(__dirname, './tsconfig.e2e.json'),
    });
    jasmine.getEnv().addReporter(new SpecReporter({
      spec: {
        displayStacktrace: false

      }
    }));
  },
};




















//   onPrepare: function() {
//     var jasmineReporters = require('jasmine-reporters');
//     require('ts-node').register({
//       project: require('path').join(__dirname, './tsconfig.e2e.json'),
//     });
//     jasmine.getEnv().addReporter(new jasmineReporters.JUnitXmlReporter({
//         consolidateAll: false,
//         savePath: 'TESTresults',
//         filePrefix: 'xmloutput'
//     }));
// }

