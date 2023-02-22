import { Component , OnInit } from '@angular/core';
import { BlogService } from './../services/blogservice/blog.service';
import {ActivatedRoute} from '@angular/router';
@Component({
  selector: 'app-blogdetails',
  templateUrl: './blogdetails.component.html',
  styleUrls: ['./blogdetails.component.css']
})
export class BlogdetailsComponent  implements OnInit  {
  public id:any
  public item:any = {}
  constructor(private _blogservice: BlogService , private route : ActivatedRoute) {}


  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      this.id = params['id'];
     this._blogservice.getBlogById(this.id).subscribe((res:any) => {
         this.item = res.data

     } )
    });
  }
}
