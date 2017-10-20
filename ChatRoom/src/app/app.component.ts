import { Component, OnInit } from '@angular/core';

import { HttpService } from './services/http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  public error: String;
  public users: any[] = [];

  constructor(private httpService: HttpService) {}

  ngOnInit() {
    this.httpService.getAll().subscribe(
      data => {
        this.users = data.results;
      },
      error => {
        this.error = error.detail;
      }
    );
}
}
