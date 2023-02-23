import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Subject } from 'rxjs';
import { AuthService } from '../services/authservice/auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  private ngUnsubscribe: Subject<any> = new Subject();
  loginForm!: FormGroup;
  loginRequest: boolean = false;

  constructor(private formbuilder: FormBuilder, private auth: AuthService , private route: Router ) {
    this.loginForm = this.formbuilder.group({
      email: [
        '',
        Validators.required,
        Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$'),
      ],
      password: ['', Validators.required],
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    this.loginRequest = true;
    if (this.loginForm.invalid) {
      return;
    }

    this.auth.login(this.loginForm.value).subscribe((res: any) => {
      this.loginRequest = false;
      if(res) {
        localStorage.setItem('access_token', res.access)
        this.route.navigate(['/']);
      }
      console.log(res);
    });
  }
}
