import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Subject } from 'rxjs';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  private ngUnsubscribe: Subject<any> = new Subject();
  registerForm!: FormGroup;

  constructor(private formbuilder: FormBuilder) {
    this.registerForm = this.formbuilder.group({
      firstname: ['', Validators.required],
      lastname: ['', Validators.required],
      email: [
        '',
        [
          Validators.required,
          Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$'),
        ],
      ],
      username: ['', Validators.required],
      password1: ['', Validators.required],
      gender: ['', Validators.required],
      password2: ['', Validators.required],
      phone : ['',Validators.required]
    })
  }

  ngOnInit(): void {

  }

  onSubmit() {
    console.log('submitted !!')
  }
}
