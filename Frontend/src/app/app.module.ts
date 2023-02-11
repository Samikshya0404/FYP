import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './common/header/header.component';
import { FooterComponent } from './common/footer/footer.component';
import { BlogComponent } from './blog/blog.component';
import { MenuComponent } from './common/menu/menu.component';
import { StylesComponent } from './styles/styles.component';
import { AboutComponent } from './about/about.component';
import { EventsComponent } from './events/events.component';
import { HouseComponent } from './house/house.component';
import { WorkoutsComponent } from './workouts/workouts.component';
import { BlogdetailsComponent } from './blogdetails/blogdetails.component';
import { ClickoutsideDirective } from './utilitis/directives/clickoutside.directive';
import { StyledetailsComponent } from './styledetails/styledetails.component';
import { PlayerComponent } from './player/player.component';
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    HomeComponent,
    HeaderComponent,
    FooterComponent,
    BlogComponent,
    MenuComponent,
    StylesComponent,
    AboutComponent,
    EventsComponent,
    HouseComponent,
    WorkoutsComponent,
    BlogdetailsComponent,
    ClickoutsideDirective,
    StyledetailsComponent,
    PlayerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
