import { style } from '@angular/animations';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { BlogComponent } from './blog/blog.component';
import { BlogdetailsComponent } from './blogdetails/blogdetails.component';
import { EventsComponent } from './events/events.component';
import { HiphopComponent } from './hiphop/hiphop.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { StylesComponent } from './styles/styles.component';
import { WorkoutsComponent } from './workouts/workouts.component';

const routes: Routes = [
  {
    path:'',
    component:HomeComponent,
    pathMatch: 'full'
  },
  {
    path:'login',
    component:LoginComponent
  },
  {
    path:'register',
    component:RegisterComponent
  },
  {
    path:'blog',
    component:BlogComponent
  },
  {
    path:'blog-details',
    component:BlogdetailsComponent
  },
  {
    path: 'styles',
    component:StylesComponent
  },
  {
    path: 'events',
    component:EventsComponent
  },

  {
    path: 'styles',
    component:StylesComponent
  },

  {
    path: 'about',
    component:AboutComponent
  },

  {
    path: 'hiphop',
    component:HiphopComponent
  },

  {
    path: 'workouts',
    component:WorkoutsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
