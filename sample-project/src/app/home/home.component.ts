import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  content(content: any) {
    throw new Error("Method not implemented.");
  }

  public userForm: FormGroup;
  submitted = false;

  constructor(private formBuilder: FormBuilder) {
  }
  ngOnInit() {
    this.userForm = this.formBuilder.group({
      name: ['', [Validators.required, Validators.pattern(/^[a-z][a-z\s]*$/), Validators.minLength(3), Validators.maxLength(15)]],
      password: ['', [Validators.required, Validators.minLength(6), Validators.maxLength(8)]],
      confirm_password: ['', [Validators.required]],
      email: ['', [Validators.email, Validators.required]],
      country: ['', [Validators.required]],
      gender: ['', Validators.required]
    },
      {
        validator: mustMatch('password', 'confirm_password')
      });
  }
  get formControls() {
    return this.userForm.controls;
  }
  public onSubmit() {
    this.submitted = true;
    if (this.userForm.valid) {
      console.log("The Form has been Submitted");
    }
  }
  public reSubmit() {
    this.userForm.reset();
    this.submitted = false;
  }
}
export function mustMatch(controlName: string, matchingControlName: string) {
  return (formGroup: FormGroup) => {
    const control = formGroup.controls[controlName];
    const matchingControl = formGroup.controls[matchingControlName];
    if (matchingControl.errors && !matchingControl.errors.mustMatch) {
      return;
    }
    if (control.value !== matchingControl.value) {
      matchingControl.setErrors({ mustMatch: true });
    } else {
      matchingControl.setErrors(null);
    }
  }
}



