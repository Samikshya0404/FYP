import { Component } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
public profile:any = false


handleProfile(){
  this.profile= !this.profile
}
clickedOutside(){
  this.profile = false
}
}
