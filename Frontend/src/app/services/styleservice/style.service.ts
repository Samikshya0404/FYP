import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environments';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class StyleService {
  private baseUrl = environment.apiUrl;


  constructor( private http: HttpClient ) { }

  getStyle(){
    return this.http.get(this.baseUrl + 'get_styles_list/')
  }
}
