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

  controller = { status: 0 };

  clock = '';
  timer = 0;
  timerStr = '';
  weather = {
    temperature: 28,
    units: 'º C',
    rain: true
  };
  alerts = 'se proclama la república catalana y se cierran todas las fronteras';

  constructor(private httpService: HttpService) {
    // tenemos que decidir la cantidad de tiempo del intervalo de actualización
    Observable.interval(1000).subscribe(x => {
      this.httpService.getStatus()
        .subscribe(
          (data) => {
            if (this.controller.status !== 2 && data.status === 2) {
              this.timer = 180; // tres minutos
              this.timerStr = '0' + Math.floor(this.timer / 60) + ':' + (this.timer % 60 < 10 ? '0' + this.timer % 60 : this.timer % 60);
            }
            this.controller = data;
          },
          (err) => { console.log(err); }
        );
    });

    Observable.interval(1000).subscribe(x => {
      const date = new Date();
      const hours = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
      const minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()
      this.clock = hours + ':' + minutes;
      this.timer -= 1;
      this.timerStr = '0' + Math.floor(this.timer / 60) + ':' + (this.timer % 60 < 10 ? '0' + this.timer % 60 : this.timer % 60);
    });

  }

  getController() {
    // TODO: https://stackoverflow.com/questions/35316583/angular2-http-at-an-interval
    const c = { status: 0, data: { weather: { temperature: '35ºC' } } };
    c.status = Math.floor(Math.random() * 4); //random entre 0 y 3
    return c;
  }
}
