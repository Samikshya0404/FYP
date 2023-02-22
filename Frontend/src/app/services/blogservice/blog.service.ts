import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environments';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root',
})
export class BlogService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getBlog() {
    return this.http.get(this.baseUrl + 'blogs/get_blog_list');
  }

  getBlogById(id:any){
    return this.http.get(this.baseUrl + 'blogs/get_blog_details/' + id )
  }
}
