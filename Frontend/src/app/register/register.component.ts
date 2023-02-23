import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Subject } from 'rxjs';
import { AuthService } from '../services/authservice/auth.service';
import { CheckPasswordMatch } from '../utilitis/directives/custom.validators'
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  private ngUnsubscribe: Subject<any> = new Subject();
  registerForm!: FormGroup;
  registerRequest: boolean = false

  constructor(private formbuilder: FormBuilder , private auth: AuthService ,private route : Router ) {
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
      password1: ['', Validators.required ],
      gender: ['', Validators.required],
      password2: ['', Validators.required],
      phone: ['', Validators.required]
    } ,{validator: CheckPasswordMatch('password1', 'password2')} )
  }

  ngOnInit(): void {


  }


  onSubmit() {
    this.registerRequest = true
    if (this.registerForm.invalid) {
      console.log('invlaid!!')
      return;
    }
    let data = {
      first_name: this.registerForm.get('firstname')?.value,
      last_name: this.registerForm.get('lastname')?.value,
      email: this.registerForm.get('email')?.value,
      username: this.registerForm.get('username')?.value,
      password: this.registerForm.get('password1')?.value,
      gender : this.registerForm.get('gender')?.value,
      contact_number : this.registerForm.get('phone')?.value,

    }
    console.log(data)
    this.auth.register(data).subscribe((res:any) => {
      this.registerRequest = false
      if(res.message){
        alert('User successfully created!!')
        this.route.navigate(['/login'])

      }
    }

)
  }
}
