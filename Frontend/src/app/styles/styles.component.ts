import { Component, OnInit } from '@angular/core';
import { StyleService } from './../services/styleservice/style.service';
@Component({
  selector: 'app-styles',
  templateUrl: './styles.component.html',
  styleUrls: ['./styles.component.css'],
})
export class StylesComponent implements OnInit {
  public styledata: any;

  constructor(private styleservice: StyleService) {}

  ngOnInit(): void {
    this.getStyleList()
  }

  getStyleList() {
    this.styleservice.getStyle().subscribe((res: any) => {
      this.styledata = res.data;
    });
  }
}
