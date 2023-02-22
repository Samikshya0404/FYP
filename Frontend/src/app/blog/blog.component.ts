import { BlogService } from './../services/blogservice/blog.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-blog',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css'],
})
export class BlogComponent implements OnInit {
  public data: any;

  constructor(private _blogservice: BlogService) {}

  ngOnInit(): void {
    this.getBlogs();
  }

  getBlogs() {
    this._blogservice.getBlog().subscribe((res: any) => {
      this.data = res.data
    });
  }
}
