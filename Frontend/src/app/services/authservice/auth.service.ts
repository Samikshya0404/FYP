import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environments';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = environment.apiUrl;
  constructor( private http: HttpClient ) { }

  register(data:any) {
    return this.http.post(this.baseUrl + 'auth/register/' ,data);
  }

  login(data:any){
    return this.http.post(this.baseUrl + 'auth/login/', data )
  }

}
