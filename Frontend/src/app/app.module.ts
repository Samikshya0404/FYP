import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

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
import { HiphopComponent } from './hiphop/hiphop.component';
import { PoppingComponent } from './popping/popping.component';
import { HouseComponent } from './house/house.component';
import { WorkoutsComponent } from './workouts/workouts.component';

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
    HiphopComponent,
    PoppingComponent,
    HouseComponent,
    WorkoutsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
