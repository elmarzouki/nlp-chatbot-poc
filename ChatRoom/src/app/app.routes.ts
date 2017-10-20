import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { InfoComponent } from './components/info/info.component';
import { LoginComponent } from './components/login/login.component';
import { ChatroomComponent } from './components/chatroom/chatroom.component';

const appRoutes: Routes = [
    { path: 'users/info', component: InfoComponent},
    { path: 'login', component: LoginComponent},
    { path: 'chatroom', component: ChatroomComponent},
    { path: '**', component: InfoComponent }
];

export const routing = RouterModule.forRoot(appRoutes);
