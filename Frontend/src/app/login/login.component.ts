import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Subject } from 'rxjs';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  private ngUnsubscribe: Subject<any> = new Subject();
  loginForm!: FormGroup;
  loginRequest:boolean = false;


  constructor(private formbuilder: FormBuilder) {
    this.loginForm = this.formbuilder.group({
      username :['',Validators.required],
      password : ['',Validators.required]
    })
  }

  ngOnInit(): void {

  }


  onSubmit(){
    this.loginRequest = true;
  }

}
