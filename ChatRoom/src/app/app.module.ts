import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';

import { routing } from './app.routes';

import { MaterializeModule } from 'angular2-materialize';

import { AppComponent } from './app.component';
import { HttpService } from './services/http.service';
import { InfoComponent } from './components/info/info.component';
import { LoginComponent } from './components/login/login.component';
import { ChatroomComponent } from './components/chatroom/chatroom.component';

@NgModule({
  declarations: [
    AppComponent,
    InfoComponent,
    LoginComponent,
    ChatroomComponent
  ],
  imports: [
    BrowserModule,
    MaterializeModule,
    HttpModule,
    routing
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
