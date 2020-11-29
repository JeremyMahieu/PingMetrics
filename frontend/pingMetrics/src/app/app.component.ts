import { Component, OnInit } from '@angular/core';
import { TargetsService } from 'src/app/services/targets.service';
import { Target } from 'src/app/models/target.model';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'pingMetrics';
  targets$ = this.targetsService.getTargets();

  constructor(private targetsService: TargetsService) { }

  ngOnInit() {
  }

}
