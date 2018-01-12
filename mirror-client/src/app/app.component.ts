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

  Math: any;
  controller = { status: 0 };

  clock = '';
  timer = 0;
  weather = {};
  barChartLabels: string[];
  barChartData: any[];
  alerts = 'se proclama la república catalana y se cierran todas las fronteras';

  constructor(private httpService: HttpService) {
    this.Math = Math;

    this.httpService.getWeather()
      .subscribe(
        (w) => {
          this.weather = w;
          this.barChartLabels = ['1h', '2h', '3h', '4h', '5h', '6h', '7h'];
          this.barChartData = [
            { 
              data: [
                w.data[0].temp,
                w.data[1].temp,
                w.data[2].temp,
                w.data[3].temp,
                w.data[4].temp,
                w.data[5].temp,
                w.data[6].temp
              ], label: 'TEMPERATURA (ºC)'
            },
            {
              data: [
                w.data[0].pop,
                w.data[1].pop,
                w.data[2].pop,
                w.data[3].pop,
                w.data[4].pop,
                w.data[5].pop,
                w.data[6].pop
              ], label: 'PROBABILIDAD DE LLUVIA (%)'
            },
            {
              data: [
                w.data[0].clouds,
                w.data[1].clouds,
                w.data[2].clouds,
                w.data[3].clouds,
                w.data[4].clouds,
                w.data[5].clouds,
                w.data[6].clouds
              ], label: 'NUBES (%)'
            }
          ];
        },
        (err) => { console.log(err); }
      );

    Observable.interval(1000).subscribe(x => {
      this.httpService.getStatus()
        .subscribe(
          (data) => {
            if (this.controller.status !== 2 && data.status === 2) {
              this.timer = 180; // tres minutos
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
    });

  }

}
