import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Rx';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch'


@Injectable()
export class HttpService {

  constructor(private http: Http) { }

  getStatus() {
    return this.http.get('http://localhost:8000/status')
      .map((res: Response) => res.json())
      .catch((error: any) => Observable.throw(error));
  }

}
