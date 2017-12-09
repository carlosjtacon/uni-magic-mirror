import { Component } from '@angular/core';
import { Observable } from 'rxjs/Rx';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  controller = { status: 0, data: {} };
  clock = '';

  constructor() {
    Observable.interval(2000).subscribe(x => {
      this.controller = this.getController();
    });

    Observable.interval(1000).subscribe(x => {
      const date = new Date();
      this.clock = date.getHours() + ':' + date.getMinutes();
    });
  }

  getController() {
    // TODO: https://stackoverflow.com/questions/35316583/angular2-http-at-an-interval
    const c = { status: 0, data: {} }
    c.status = Math.floor(Math.random() * 2); //random entre 0 y 1
    return c;
  }
}
