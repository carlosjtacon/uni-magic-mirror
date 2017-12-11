import { Component } from '@angular/core';
import { Observable } from 'rxjs/Rx';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HttpService]
})

export class AppComponent {
  controller = { status: 0, data: {} };
  clock = '';
  timer = 0;

  constructor(private httpService: HttpService) {
    // tenemos que decidir la cantidad de tiempo del intervalo de actualización
    Observable.interval(3000).subscribe(x => {
      this.httpService.getStatus()
        .subscribe(
          (data) => {
            this.controller = data;
            if (this.controller.status === 2) {
              this.timer = 180; // tres minutos
            }
          },
          (err) => { console.log(err); }
        );
    });

    Observable.interval(1000).subscribe(x => {
      const date = new Date();
      this.clock = date.getHours() + ':' + date.getMinutes();
      this.timer -= 1;
    });

  }

  getController() {
    // TODO: https://stackoverflow.com/questions/35316583/angular2-http-at-an-interval
    const c = { status: 0, data: { weather: { temperature: '35ºC' } } };
    c.status = Math.floor(Math.random() * 4); //random entre 0 y 3
    return c;
  }
}
