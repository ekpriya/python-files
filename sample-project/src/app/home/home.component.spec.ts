import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HomeComponent } from './home.component';
import { BrowserModule, By } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { DebugElement } from '@angular/core';

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;
  let de:DebugElement;
  let el:HTMLElement;


  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HomeComponent ],
        imports:[BrowserModule,FormsModule,ReactiveFormsModule]
      
    })
    .compileComponents().then(()=>{
      fixture= TestBed.createComponent(HomeComponent);
      component=fixture.componentInstance;
      de=fixture.debugElement.query(By.css('userForm'));
    });
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
