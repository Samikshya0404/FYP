import { GuardsService } from './utilitis/directives/guard/guard.service';
import { style } from '@angular/animations';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { BlogComponent } from './blog/blog.component';
import { BlogdetailsComponent } from './blogdetails/blogdetails.component';
import { EventsComponent } from './events/events.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { StyledetailsComponent } from './styledetails/styledetails.component';
import { StylesComponent } from './styles/styles.component';
import { WorkoutsComponent } from './workouts/workouts.component';
import { PlayerComponent } from './player/player.component';
const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  {
    path: 'blog',
    component: BlogComponent
  },
  {
    path: 'blog-details/:id',
    component: BlogdetailsComponent
  },
  {
    path: 'styles',
    component: StylesComponent
  },
  {
    path: 'styledetails',
    component: StyledetailsComponent
  },
  {
    path: 'events',
    component: EventsComponent
  },

  {
    path: 'styles',
    component: StylesComponent
  },

  {
    path: 'about',
    component: AboutComponent
  },
  {
    path: 'workouts',
    component: WorkoutsComponent
  },
  {
    path: 'watch',
    component: PlayerComponent,
    canActivate: [GuardsService]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
