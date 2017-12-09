import { Component } from '@angular/core';
import { Observable } from 'rxjs/Rx';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  clock = '';

  constructor() {
    Observable.interval(1000).subscribe(x => {
      const date = new Date();
      this.clock = date.getHours() + ':' + date.getMinutes();
    });
  }
}
