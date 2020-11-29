import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { from, Observable } from 'rxjs';
import { AppConfig } from '../app.config';
import { Target } from '../models/target.model';

@Injectable({
  providedIn: 'root'
})
export class TargetsService {

  constructor(private http: HttpClient) { }

  getTargets(): Observable<Target[]> {
    return this.http.get<Target[]>(`${AppConfig.ENDPOINT}targets/list`);
  }
}
