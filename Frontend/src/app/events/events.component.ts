import { Component, OnInit } from '@angular/core';
import { EventService } from './../services/eventservice/event.service';
@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css'],
})
export class EventsComponent {
  public eventdata:any

  constructor(private eventservice: EventService) {}

  ngOnInit(): void {
    this.getEventList();
  }
  getEventList() {
    this.eventservice.getEvent().subscribe((res: any) => {
      this.eventdata = res.data
    
    });
  }
}
