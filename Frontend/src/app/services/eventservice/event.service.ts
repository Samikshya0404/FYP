import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environments';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class EventService {

  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

   getEvent(){
    return this.http.get(this.baseUrl + 'events/get_event_list')
   }

}
