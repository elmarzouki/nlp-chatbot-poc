import { Component, OnInit } from '@angular/core';

import { HttpService } from './../../services/http.service';

@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styles: []
})
export class InfoComponent implements OnInit {

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
