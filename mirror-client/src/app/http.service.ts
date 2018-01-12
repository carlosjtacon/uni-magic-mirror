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

  getWeather() {
    return this.http.get('https://api.weatherbit.io/v2.0/forecast/hourly?city=Madrid&country=ES&key=3d9015a3d22148c8bae87ef088dfa45a')
      .map((res: Response) => res.json())
      .catch((error: any) => Observable.throw(error));
  }

}
