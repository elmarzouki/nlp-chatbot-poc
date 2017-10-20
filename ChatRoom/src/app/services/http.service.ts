import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class HttpService {

  private baseUrl: String = 'http://127.0.0.1:8000';

  constructor(private http: Http) { }

  public getAll() {
    return this.http.get(`${this.baseUrl}/users`, {headers: this.getHeaders()})
    .map((response: any) => response.json())
    .catch(this.handelError);
  }

  private getHeaders() {
    // I included these headers because otherwise FireFox
    // will request text/html instead of application/json
    let headers = new Headers();
    headers.append('Accept', 'application/json');
    return headers;
  }


  private handelError(error: any) {
    console.log('An error occurred', error);
    return Observable.throw(error.json());
  }

}
